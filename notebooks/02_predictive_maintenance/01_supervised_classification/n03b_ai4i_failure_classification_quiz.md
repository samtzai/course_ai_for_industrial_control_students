# P4a (Part 2) - Machine Failure Prediction with AI4I 2020 (n03b) - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:: se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF. Cuando una pregunta pida cifras, cópialas de **vuestra** ejecución (y, si habéis cambiado algún parámetro, indicad cuál).

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Imbalanced classification, PR/ROC curves and cost-based threshold with AI4I 2020

## 📋 Instructions
This is the **second part of P4a** (the first part is the Iris quiz `n03_classification_quiz.md`). Run `n03b_ai4i_failure_classification.ipynb` completely. When a question asks for numbers, copy them from **your** run.

---

## Section 1: Data and Leakage

**Question 1**: What percentage of records are failures in AI4I 2020? What accuracy does a "model" that **always** predicts "no failure" obtain on your test set, and how many failures does it detect? What does this tell you about using accuracy here?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 2**: The notebook excludes `UDI`, `Product ID`, `TWF`, `HDF`, `PWF`, `OSF` and `RNF` from the inputs. Explain **with the cross-table printed by the notebook** why the failure-mode columns would be data leakage. Why are the IDs also excluded?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 3**: Give one example, in a real factory, of a variable that would also be leakage when predicting a machine failure (something only known after the failure).

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 4**: Why is the `StandardScaler` fitted only on the training set, and why is the split stratified?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 2: Imbalance and Curves

**Question 5**: Copy the validation metrics at threshold 0.5 of **your** two models:

| Model | Accuracy | Precision | Recall | F1 | ROC AUC | PR AUC (AP) |
|---|---|---|---|---|---|---|
| A - no weighting | | | | | | |
| B - pos_weight | | | | | | |

Which `pos_weight` value did you use? Explain in your own words how `pos_weight` changes the training and why model A has a lower recall at 0.5.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 6**: Looking at **your** ROC and PR curves: which model is better *independently of the threshold*? Why is the PR curve more informative than the ROC curve when only ~3 % of the samples are positive?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 7**: What does the horizontal dotted line of the PR curve represent?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 3: Cost-Based Threshold

**Question 8**: Write the cost function used in the notebook and explain what `COST_FN` and `COST_FP` represent in a milling machine. Are the default values (10,000 € and 500 €) reasonable? Propose your own values and justify them.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 9**: Fill the test table of **your** run (thresholds chosen on validation):

| Threshold | t | TP | FN | FP | Recall | Precision | Cost (€) |
|---|---|---|---|---|---|---|---|
| Default 0.5 | 0.5 | | | | | | |
| Max F1 (val) | | | | | | | |
| Min cost (val) | | | | | | | |
| Never intervene | - | | | | | | |
| Always intervene | - | | | | | | |

Which threshold would you deploy? Justify it **with your numbers**, not with a general rule.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 10**: Is the threshold with minimum cost on **validation** also the one with minimum cost on **test** in your run? If not, why can this happen? (Think about how many failures there are in the validation set.)

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 11**: Change `COST_FN` and/or `COST_FP` (e.g. ratio 5:1 and 50:1), re-run the threshold cells and report how the chosen threshold, the FN and the FP change. Relate it to the plot *optimal threshold vs. cost ratio*.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 12**: For calibrated probabilities, theory says the optimal threshold is $t^* = C_{FP}/(C_{FP}+C_{FN})$. Compute it for your costs. Is it close to the threshold found for model A? And for model B? Why are they different?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 4: Improvements and Reflection

**Question 13**: Set `USE_ENGINEERED_FEATURES = True`, re-run the notebook and compare ROC AUC, PR AUC and the minimum test cost with your original run. Why can features such as power (torque × speed) or temperature difference help a small neural network?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 14**: Explain to the maintenance manager, in 5–8 lines and with **your** figures, what the model does, how many failures it would detect out of every 100, how many unnecessary stops it would cause, and what the expected saving is compared with "never intervene".

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---
