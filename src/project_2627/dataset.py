"""Download, inspect, and split the hieroglyph image dataset.

Run this module once to download the data and create an example image plot::

    uv run python -m src.project_2627.dataset

Create each split with the same seed and class threshold. This ensures that
the three datasets use the same class-to-index mapping and partition::

    from torch.utils.data import DataLoader
    from src.project_2627.dataset import HieroglyphsDataset

    train_dataset = HieroglyphsDataset(split="train", seed=42)
    val_dataset = HieroglyphsDataset(split="val", seed=42)
    test_dataset = HieroglyphsDataset(split="test", seed=42)

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

Each item is a grayscale image tensor of shape ``(1, 64, 64)`` and an integer
class label. Get the corresponding class name from ``dataset.class_names``::

    image, label = train_dataset[0]
    class_name = train_dataset.class_names[label]

    # Plot one representative training image for every retained class.
    train_dataset.plot()

The default split is 70% train, 15% validation, and 15% test. Classes with
fewer than 15 images are excluded by default. Use validation data for model
selection and reserve test data for final evaluation.
"""

import random
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms

DATASET_ROOT = Path(__file__).resolve().parents[2] / "data" / "project_2627" / "hieroglyphs-dataset"
KAGGLE_DATASET = "ayatollahelkolally/hieroglyphs-dataset"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp"}
SPLIT_RATIOS = {"train": 0.70, "val": 0.15, "test": 0.15}


def download_dataset(root_dir: str | Path = DATASET_ROOT) -> Path:
    """Download the Kaggle dataset into the repository's data directory."""
    import kagglehub

    root = Path(root_dir)
    root.parent.mkdir(parents=True, exist_ok=True)
    downloaded_path = kagglehub.dataset_download(KAGGLE_DATASET, output_dir=str(root))
    return Path(downloaded_path)


def _split_counts(sample_count: int) -> dict[str, int]:
    counts = {name: int(sample_count * ratio) for name, ratio in SPLIT_RATIOS.items()}
    remaining = sample_count - sum(counts.values())
    priority = sorted(
        SPLIT_RATIOS,
        key=lambda name: sample_count * SPLIT_RATIOS[name] - counts[name],
        reverse=True,
    )
    for name in priority[:remaining]:
        counts[name] += 1
    return counts


class HieroglyphsDataset(Dataset):
    """Image dataset with a reproducible, stratified train/validation/test split."""

    def __init__(
        self,
        root_dir: str | Path = DATASET_ROOT,
        split: str = "train",
        seed: int = 42,
        min_images_per_class: int = 15,
        transform=None,
    ):
        if split not in SPLIT_RATIOS:
            raise ValueError(f"split must be one of {tuple(SPLIT_RATIOS)}, got {split!r}")
        if min_images_per_class < 3:
            raise ValueError("min_images_per_class must be at least 3 for three-way splitting")

        self.root_dir = Path(root_dir)
        if not self.root_dir.is_dir():
            raise FileNotFoundError(
                f"Dataset not found at {self.root_dir}. "
                "Run `python -m src.project_2627.dataset` first."
            )

        class_files = {}
        for class_dir in sorted(path for path in self.root_dir.iterdir() if path.is_dir()):
            files = sorted(
                path
                for path in class_dir.iterdir()
                if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
            )
            if len(files) >= min_images_per_class:
                class_files[class_dir.name] = files
        if not class_files:
            raise ValueError(
                f"No classes have at least {min_images_per_class} images in {self.root_dir}"
            )

        self.class_names = sorted(class_files)
        self.class_to_idx = {name: index for index, name in enumerate(self.class_names)}
        self.class_counts = {name: len(class_files[name]) for name in self.class_names}
        self.transform = transform or transforms.Compose(
            [transforms.Resize((64, 64)), transforms.ToTensor()]
        )

        samples_by_class = defaultdict(list)
        all_samples = []
        for class_name in self.class_names:
            label = self.class_to_idx[class_name]
            for image_path in class_files[class_name]:
                samples_by_class[label].append(len(all_samples))
                all_samples.append((image_path, label))

        rng = random.Random(seed)
        split_indices = {name: [] for name in SPLIT_RATIOS}
        for label in range(len(self.class_names)):
            class_indices = samples_by_class[label]
            rng.shuffle(class_indices)
            counts = _split_counts(len(class_indices))
            train_end = counts["train"]
            val_end = train_end + counts["val"]
            split_indices["train"].extend(class_indices[:train_end])
            split_indices["val"].extend(class_indices[train_end:val_end])
            split_indices["test"].extend(class_indices[val_end:])

        self.samples = [all_samples[index] for index in split_indices[split]]
        self.split = split

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        image_path, label = self.samples[index]
        with Image.open(image_path) as image:
            image_tensor = self.transform(image.convert("L"))
        return image_tensor, label

    def list_classes(self) -> dict[str, int]:
        """Return retained class names and their total image counts."""
        return self.class_counts.copy()

    def plot(self, filepath: str | Path | None = None):
        """Plot one image from every class in this split and return the figure."""
        indices_by_label = defaultdict(list)
        for index, (_, label) in enumerate(self.samples):
            indices_by_label[label].append(index)

        missing_classes = [
            self.class_names[label]
            for label in range(len(self.class_names))
            if label not in indices_by_label
        ]
        if missing_classes:
            raise ValueError(f"Classes missing from the {self.split!r} split: {missing_classes}")

        rng = random.Random(42)
        indices = [rng.choice(indices_by_label[label]) for label in range(len(self.class_names))]
        columns = min(4, len(indices))
        rows = (len(indices) + columns - 1) // columns
        figure, axes = plt.subplots(rows, columns, figsize=(3 * columns, 3 * rows), squeeze=False)

        for axis, index in zip(axes.flat[: len(indices)], indices, strict=True):
            image, label = self[index]
            axis.imshow(image.squeeze(0), cmap="gray")
            axis.set_title(self.class_names[label])
            axis.axis("off")
        for axis in axes.flat[len(indices) :]:
            axis.axis("off")

        figure.tight_layout()
        if filepath is not None:
            filepath = Path(filepath)
            filepath.parent.mkdir(parents=True, exist_ok=True)
            figure.savefig(filepath, bbox_inches="tight")
        return figure


if __name__ == "__main__":
    dataset_path = download_dataset()
    print(f"Dataset files: {dataset_path}")

    datasets = {
        split: HieroglyphsDataset(
            root_dir=dataset_path,
            split=split,
            seed=42,
            min_images_per_class=15,
        )
        for split in SPLIT_RATIOS
    }
    train_dataset = datasets["train"]
    val_dataset = datasets["val"]
    test_dataset = datasets["test"]

    print(f"Retained classes: {len(train_dataset.class_names)}")
    print(f"Class mapping: {train_dataset.class_to_idx}")
    print(
        f"Split sizes: train={len(train_dataset)}, val={len(val_dataset)}, test={len(test_dataset)}"
    )
    print(f"Images per retained class: {train_dataset.list_classes()}")

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
    images, labels = next(iter(train_loader))
    print(f"Training batch shape: {tuple(images.shape)}")
    print(f"First training label: {train_dataset.class_names[labels[0].item()]}")
    print(f"Validation batches: {len(val_loader)}, test batches: {len(test_loader)}")

    output_folder = Path(__file__).resolve().parents[2] / "outs" / "project_2627"
    train_dataset.plot(filepath=output_folder / "dataset_examples.png")
