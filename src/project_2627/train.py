import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.utils.data import DataLoader

from .dataset import DATASET_ROOT, HieroglyphsDataset
from .model import HieroglyphClassifier


def get_device(force: str = "auto") -> torch.device:
    force = force.lower()
    if force not in {"auto", "cpu", "cuda"}:
        raise ValueError("force must be 'auto', 'cpu', or 'cuda'")
    if force == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA was requested but is not available")
    if force == "auto":
        force = "cuda" if torch.cuda.is_available() else "cpu"
    return torch.device(force)


def train_model(
    output_folder: Path,
    device: torch.device,
    root_dir: Path = DATASET_ROOT,
    epochs: int = 10,
    batch_size: int = 64,
    learning_rate: float = 0.001,
    seed: int = 42,
    min_images_per_class: int = 15,
):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    train_dataset = HieroglyphsDataset(
        root_dir=root_dir,
        split="train",
        seed=seed,
        min_images_per_class=min_images_per_class,
    )
    val_dataset = HieroglyphsDataset(
        root_dir=root_dir,
        split="val",
        seed=seed,
        min_images_per_class=min_images_per_class,
    )

    generator = torch.Generator().manual_seed(seed)
    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        generator=generator,
    )
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    model = HieroglyphClassifier(num_classes=len(train_dataset.class_names)).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    output_folder.mkdir(parents=True, exist_ok=True)
    best_model_path = output_folder / "best_model.pth"
    train_losses = []
    val_losses = []
    best_val_loss = float("inf")

    for epoch in range(epochs):
        model.train()
        train_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            logits = model(images)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
            train_loss += loss.item() * labels.size(0)
        train_loss /= len(train_dataset)

        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                logits = model(images)
                val_loss += criterion(logits, labels).item() * labels.size(0)
        val_loss /= len(val_dataset)
        train_losses.append(train_loss)
        val_losses.append(val_loss)
        print(f"Epoch {epoch + 1}/{epochs}: train loss={train_loss:.4f}, val loss={val_loss:.4f}")

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(
                {
                    "model_state_dict": model.state_dict(),
                    "class_names": train_dataset.class_names,
                    "num_classes": len(train_dataset.class_names),
                    "input_channels": 1,
                },
                best_model_path,
            )

    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(train_losses, label="Train")
    axis.plot(val_losses, label="Validation")
    axis.set(xlabel="Epoch", ylabel="Cross-entropy loss", title="Training history")
    axis.legend()
    figure.tight_layout()
    figure.savefig(output_folder / "loss_plot.png")
    plt.close(figure)
    print(f"Best validation loss: {best_val_loss:.4f}; checkpoint: {best_model_path}")
    return {"train_loss": train_losses, "val_loss": val_losses}


def main():
    parser = argparse.ArgumentParser(description="Train the hieroglyph classifier")
    parser.add_argument("--root-dir", type=Path, default=DATASET_ROOT)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.001)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-images-per-class", type=int, default=15)
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    args = parser.parse_args()

    output_folder = Path(__file__).resolve().parents[2] / "outs" / "project_2627"
    device = get_device(args.device)
    print(f"Using device: {device}")
    train_model(
        output_folder,
        device,
        args.root_dir,
        args.epochs,
        args.batch_size,
        args.learning_rate,
        args.seed,
        args.min_images_per_class,
    )


if __name__ == "__main__":
    main()
