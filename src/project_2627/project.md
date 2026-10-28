# Hieroglyph Classification Project

## Goal

Build and evaluate an image classifier that recognizes the hieroglyph classes in the provided dataset. Your goal is to develop a well-justified solution and analyze its behavior, not simply to maximize one score.

## Dataset

The dataset is downloaded from Kaggle by running:

```powershell
uv run python -m src.project_2627.dataset
```

The script stores the images under `data/project_2627/hieroglyphs-dataset/`. The downloaded images are excluded from version control. KaggleHub may require you to accept the dataset's terms or configure Kaggle access before downloading.

Images are grouped into folders named after their class. The shared loader retains classes with at least 15 images; smaller classes are excluded so each retained class can contribute examples to all three partitions. The retained data is split deterministically and stratified by class into 70% training, 15% validation, and 15% test data (with integer rounding per class). The default seed is 42. The class-to-index mapping is sorted and shared across the splits. Images are converted to grayscale and resized to 64 by 64 pixels by default.

Evaluation uses this same retained class list for the classification report, per-class metric plot, F1 scores, and confusion matrix. Classes below the image threshold are absent from the test split and are not included in these evaluation outputs.

Inspect the labels and sample images with:

```python
from src.project_2627.dataset import HieroglyphsDataset

dataset = HieroglyphsDataset(split="train")
print(dataset.list_classes())
dataset.plot()
```

## Project Structure

Use the same separation of responsibilities as Exercise 1:

- `dataset.py`: downloading, loading, class labels, splits, and dataset visualization.
- `model.py`: the neural network architecture and forward pass.
- `train.py`: reproducible training, validation, and selection/saving of the best model.
- `evaluate.py`: final evaluation and result visualization using the test set.

The starter is intentionally simple: `model.py` contains a single linear layer over flattened pixels, and `train.py` provides a basic supervised training loop. Treat these as baselines to improve. You may modify or replace the model and training strategy, but keep the module responsibilities clear and document significant changes.

Run a baseline training and evaluation with:

```powershell
uv run python -m src.project_2627.train
uv run python -m src.project_2627.evaluate
```

Outputs, including the best checkpoint, loss curve, test metrics, per-class metrics plot and report, and confusion matrix, are written to `outs/project_2627/`.

## Requirements

1. **Establish a baseline first.** Train the supplied linear model with the starter training script before changing it. Record the configuration, chosen metrics, training/validation curves, and validation results. This is your reference point, not your final solution.
2. **Diagnose what needs improvement.** Inspect the training and validation curves, per-class metrics, confusion matrix, and representative errors. Decide whether the evidence suggests underfitting, overfitting, class imbalance, or specific class confusions. State a hypothesis for what might improve the result.
3. **Run and document improvement experiments.** Change one main factor at a time where practical, then compare its validation results with the baseline. Possible experiments include learning rate or optimizer, loss function or class weighting, training duration or regularization, data augmentation, and model architecture. Explain the reason for each change and whether the evidence supported keeping it. It is acceptable for an experiment to perform worse; report what you learned and whether you reverted it.
4. **Select appropriate metrics.** Choose and justify a primary metric for model selection and any supporting metrics. Explain how the choice fits the task and the imbalanced class distribution; accuracy alone may hide poor performance on less frequent classes. Consider macro-averaged F1 or balanced accuracy, weighted F1, and per-class precision, recall, and F1. You may add or replace metrics in `evaluate.py` when needed. Use the same primary validation metric when comparing experiments.
5. **Analyze overfitting explicitly.** Compare training and validation curves and discuss the gap between them. If you observe overfitting, try at least one relevant response, such as augmentation, regularization, early stopping, or a smaller model, and report its measured effect. If overfitting is not evident, explain what the curves show instead.
6. **Treat the test set as held out.** Use training data to fit models and validation data to compare experiments and make decisions. After choosing the final approach, evaluate it on the test set for the final report; do not use test results to select models or tune hyperparameters.
7. **Keep experiments reproducible.** Record the seed, split, model settings, optimizer, learning rate, batch size, epoch count, loss, augmentation, and any class-weighting choices for every experiment you compare.
8. **Discuss limitations and class imbalance.** Explain how the 15-image class threshold affects the task, identify failure cases and computational constraints, and propose realistic next steps. Do not claim generalization to real-world hieroglyph data unless your evaluation supports that claim.

## Deliverables

- Working `dataset.py`, `model.py`, `train.py`, and `evaluate.py` modules.
- A trained checkpoint and saved evaluation outputs in `outs/project_2627/`.
- A PowerPoint presentation describing:
  - The task, data, class filtering, and motivation.
  - The baseline model, its initial results, and what you observed was wrong or limited.
  - The metric or metrics you selected, why they are appropriate, and how you used them to compare experiments.
  - The sequence of improvement experiments: the hypothesis, the change made, validation evidence, and the decision to keep or revert each change. Include learning rate, augmentation, architecture, loss, or other experiments you actually tried; do not present only the final model.
  - Training/validation evidence used to identify or rule out overfitting and the effect of any response you tried.
  - The final architecture and training setup, explaining how it differs from the baseline and why.
  - Final held-out test results, per-class behavior, and representative errors.
  - Limitations, computational or data constraints, and proposed next steps.

Show the development path in chronological order: baseline, diagnosis, experiments, and final choice. Include plots or a compact experiment comparison table and enough configuration detail for another student to understand and reproduce your conclusions. Clearly distinguish validation results used during development from the final test results.