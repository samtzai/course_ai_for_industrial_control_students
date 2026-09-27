import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from torch.utils.data import DataLoader

from .dataset import DATASET_ROOT, HieroglyphsDataset
from .model import HieroglyphClassifier
from .train import get_device


def evaluate_model(
    output_folder: Path,
    device: torch.device,
    root_dir: Path = DATASET_ROOT,
    batch_size: int = 64,
    seed: int = 42,
    min_images_per_class: int = 15,
):
    checkpoint_path = output_folder / "best_model.pth"
    if not checkpoint_path.is_file():
        raise FileNotFoundError(f"Model checkpoint not found: {checkpoint_path}")

    test_dataset = HieroglyphsDataset(root_dir, "test", seed, min_images_per_class)
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=True)
    if checkpoint["class_names"] != test_dataset.class_names:
        raise ValueError("Checkpoint classes do not match the test dataset classes")

    model = HieroglyphClassifier(
        num_classes=checkpoint["num_classes"],
        input_channels=checkpoint["input_channels"],
    ).to(device)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    targets = []
    predictions = []
    with torch.no_grad():
        for images, labels in test_loader:
            logits = model(images.to(device))
            predictions.extend(logits.argmax(dim=1).cpu().tolist())
            targets.extend(labels.tolist())

    class_names = test_dataset.class_names
    report = classification_report(
        targets,
        predictions,
        labels=list(range(len(class_names))),
        target_names=class_names,
        output_dict=True,
        zero_division=0,
    )
    metrics = {
        "accuracy": accuracy_score(targets, predictions),
        "macro_f1": f1_score(targets, predictions, average="macro", zero_division=0),
        "weighted_f1": f1_score(targets, predictions, average="weighted", zero_division=0),
    }
    output_folder.mkdir(parents=True, exist_ok=True)
    with (output_folder / "test_metrics.json").open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=2)
    pd.DataFrame(report).transpose().to_csv(output_folder / "test_classification_report.csv")

    ordered_classes = sorted(class_names, key=lambda name: report[name]["f1-score"])
    positions = np.arange(len(ordered_classes))
    bar_height = 0.25
    figure, axis = plt.subplots(figsize=(12, max(8, len(ordered_classes) * 0.35)))
    axis.barh(
        positions - bar_height,
        [report[name]["precision"] for name in ordered_classes],
        height=bar_height,
        label="Precision",
    )
    axis.barh(
        positions,
        [report[name]["recall"] for name in ordered_classes],
        height=bar_height,
        label="Recall",
    )
    axis.barh(
        positions + bar_height,
        [report[name]["f1-score"] for name in ordered_classes],
        height=bar_height,
        label="F1 score",
    )
    axis.set_yticks(positions, ordered_classes)
    axis.set_xlim(0, 1)
    axis.set_xlabel("Score")
    axis.set_title("Per-class test metrics (ordered by F1 score)")
    axis.invert_yaxis()
    axis.legend(loc="lower right")
    figure.tight_layout()
    figure.savefig(output_folder / "per_class_metrics.png", dpi=160)
    plt.close(figure)

    matrix = confusion_matrix(targets, predictions, labels=list(range(len(class_names))))
    figure, axis = plt.subplots(figsize=(16, 14))
    display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=class_names)
    display.plot(ax=axis, xticks_rotation="vertical", colorbar=False, values_format="d")
    axis.set_title("Test-set confusion matrix")
    figure.tight_layout()
    figure.savefig(output_folder / "confusion_matrix.png", dpi=160)
    plt.close(figure)

    print("Test metrics:", metrics)
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Evaluate the hieroglyph classifier")
    parser.add_argument("--root-dir", type=Path, default=DATASET_ROOT)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-images-per-class", type=int, default=15)
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    args = parser.parse_args()

    output_folder = Path(__file__).resolve().parents[2] / "outs" / "project_2627"
    evaluate_model(
        output_folder,
        get_device(args.device),
        args.root_dir,
        args.batch_size,
        args.seed,
        args.min_images_per_class,
    )


if __name__ == "__main__":
    main()
