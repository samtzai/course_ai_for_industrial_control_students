import torch.nn as nn


class HieroglyphClassifier(nn.Module):
    """Minimal linear baseline operating on flattened 64-by-64 grayscale images."""

    def __init__(self, num_classes: int, input_channels: int = 1):
        super().__init__()
        self.classifier = nn.Linear(input_channels * 64 * 64, num_classes)

    def forward(self, images):
        flattened_images = images.flatten(start_dim=1)
        return self.classifier(flattened_images)
