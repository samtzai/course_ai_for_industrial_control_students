# Steel Defect Classification - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección: se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF. Cuando una pregunta pida cifras, copia las de vuestra ejecución e indica cualquier cambio de parámetros.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Steel defect classification with CIFAR-10 examples and data augmentation

## Instructions
Run notebooks 12, 13 and 14. They use CIFAR-10 as a proxy for steel defects, not real steel images. Use your own results for questions about performance; results can differ with the split, seed, training settings and runtime.

---

## Section 1: Dataset and Binary Classification

**Question 1**: Which two CIFAR-10 classes does notebook 12 use to simulate defective and non-defective steel? Why is this only a proxy task?

_Your answer:_

_______________________________________________________________________________

**Question 2**: What is the shape and meaning of one image tensor after preprocessing? Explain the roles of the channel, height and width dimensions.

_Your answer:_

_______________________________________________________________________________

**Question 3**: Which output activation and loss function are used for binary classification? Explain why they fit the target labels.

_Your answer:_

_______________________________________________________________________________

**Question 4**: Report the binary model's validation and test metrics from your run. Which errors would be most important to investigate in an industrial inspection line, and why?

| Metric | Validation | Test |
|---|---:|---:|
| Accuracy | | |
| Precision / recall (as reported) | | |

_Your explanation:_

_______________________________________________________________________________

---

## Section 2: Multiclass Classification

**Question 5**: What does each row and column represent in the confusion matrix? What do the diagonal and off-diagonal cells tell you?

_Your answer:_

_______________________________________________________________________________

**Question 6**: Notebook 13 maps the CIFAR-10 classes to simulated defect categories. Copy the per-class results or confusion matrix from your run. Which class was easiest and which was most difficult to classify? Support your answer with the relevant values.

_Your answer:_

_______________________________________________________________________________

**Question 7**: Report the validation and test accuracy for your binary and multiclass runs. Explain, using your own results and the number and nature of the classes, why the figures differ in your experiment. Do not assume one task must always have higher accuracy.

| Task | Validation accuracy | Test accuracy |
|---|---:|---:|
| Binary | | |
| Multiclass | | |

_Your explanation:_

_______________________________________________________________________________

**Question 8**: If one defect category is much rarer than the others, why can accuracy be misleading? Name a metric or training strategy that could help.

_Your answer:_

_______________________________________________________________________________

---

## Section 3: Data Augmentation and Results

**Question 9**: What is data augmentation, and how can it help a vision model generalise to new images?

_Your answer:_

_______________________________________________________________________________

**Question 10**: Which augmentations did notebook 14 apply? For each, describe a plausible change in image appearance it is intended to represent.

_Your answer:_

_______________________________________________________________________________

**Question 11**: Report validation accuracy, test accuracy and training time with and without augmentation from your run. Which differences do you observe?

| Run | Validation accuracy | Test accuracy | Training time |
|---|---:|---:|---:|
| Without augmentation | | | |
| With augmentation | | | |

**Question 12**: Which of your runs achieved the highest test accuracy, and by how much did the results differ? Explain in your own words why that happened in your experiment. Consider the data split, training variability and whether the transformations preserve defect cues; do not generalise beyond your results.

_Your explanation:_

_______________________________________________________________________________

**Question 13**: Compare the training and validation curves in both runs. What evidence, if any, do you see of overfitting, and how did augmentation change it?

_Your answer:_

_______________________________________________________________________________

**Question 14**: Which augmentation would you remove or adjust if moving from CIFAR-10 examples to real steel images? Explain how it might distort a feature that matters for classifying defects.

_Your answer:_

_______________________________________________________________________________

---

## Section 4: Implementation and Industrial Applications

**Question 15**: In PyTorch, how should transforms differ between training and validation/testing? Why should random augmentation not be applied to the test set?

_Your answer:_

_______________________________________________________________________________

**Question 16**: What information does dropout provide during training, and why can it complement data augmentation?

_Your answer:_

_______________________________________________________________________________

**Question 17**: For a high-speed steel manufacturing line, which image changes might occur in production? Propose an augmentation that could represent one of them without erasing defect information.

_Your answer:_

_______________________________________________________________________________

**Question 18**: Describe one limitation of evaluating these models on CIFAR-10 proxy images before deployment at a real plant or camera station. How would you test or mitigate it?

_Your answer:_

_______________________________________________________________________________

**Question 19**: Based on your experiments, what should be the next step before deploying a defect classifier? Refer to a result, failure mode or limitation from your own run.

_Your answer:_

_______________________________________________________________________________

**Question 20**: If you could run one additional experiment, what would you change and which metric or plot would you use to decide whether it helped?

_Your answer:_

_______________________________________________________________________________
