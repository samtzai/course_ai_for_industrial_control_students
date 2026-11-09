# Steel Defect Classification with NEU (n12, n13, n14) - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección: se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF. Cuando una pregunta pida cifras, cópialas de **vuestra** ejecución (y, si habéis cambiado algún parámetro, indicad cuál).

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Steel defect classification with the NEU Surface Defect Database (binary, multiclass and data augmentation)

## 📋 Instructions

This quiz covers the three steel defect notebooks:
- **n12**: Binary classification (critical defect vs. other defect)
- **n13**: Multiclass classification (6 NEU defect types)
- **n14**: Data augmentation with a fair comparison (same train set, fixed validation, separate test)

For multiple-choice questions, choose one option **and justify it in one or two sentences**.

---

## Section 1: Data and Binary Classification (n12)

**Question 1**: NEU has no "defect-free" class. Explain in your own words which binary task n12 solves, why it makes sense on a steel inspection line, and which class you used as critical (`CRITICAL_CLASS`).

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 2**: The split is done by **blocks of 10 consecutive images** instead of picking images completely at random. What problem does this avoid and what would happen to the test accuracy if we did not do it?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 3**: Why is the normalisation (mean and std) computed only with the training images?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 4**: The binary model has a single output and uses `BCEWithLogitsLoss(pos_weight=...)`.
a) Why is there no sigmoid inside the model?
b) Which `pos_weight` value did your run print and how is it computed?
c) What would you expect to happen to the recall of the critical class without `pos_weight`?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 5**: Copy from **your** run the test results with threshold 0.5 and with the threshold chosen on validation:

| Threshold | Value | Accuracy | Precision | Recall | FN | FP |
|---|---|---|---|---|---|---|
| Default | 0.5 | | | | | |
| Chosen on validation | | | | | | |

Which one would you deploy on the line and why? Talk about the cost of a FN and of a FP in this process.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 6**: Why do we choose the threshold on the **validation** set and not on the test set?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 7**: Look at the misclassified images of **your** run. Which non-critical classes are confused with the critical one? Describe what they have in common visually.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 2: Multiclass Classification (n13)

**Question 8**: What changes in the output layer, the loss function and the decision rule between n12 and n13?

| | n12 (binary) | n13 (multiclass) |
|---|---|---|
| Output neurons | | |
| Loss | | |
| How the class is decided | | |

**Question 9**: Copy your test accuracy and the **two most frequent confusions** of your confusion matrix. Why can these classes look similar? (Look at the example images.)

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 10**: Which class has the lowest recall in your run? If that class were the most dangerous defect for your customer, what would you change (data, model, decision)?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 11**: The model uses **Global Average Pooling** before the last linear layer. What does this layer do and what advantage does it have compared with `Flatten` of the whole feature map?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 12**: In the training curves of n13, at which epoch was the best validation loss reached in your run? Is there any sign of overfitting? Justify it with your curves.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 3: Data Augmentation (n14)

**Question 13**: Explain in your own words why the comparison in n14 is **fair**. Mention at least three things that are kept identical between the two models.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 14**: Fill the table with **your** results:

| Images/class | Augmentation | Best val acc | Test acc | Train-val gap (last) | Time (s) |
|---|---|---|---|---|---|
| 30 | No | | | | |
| 30 | Yes | | | | |
| all | No | | | | |
| all | Yes | | | | |

In which case did augmentation help more (or hurt)? Propose an explanation based on the amount of data.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 15**: The training accuracy **with** augmentation is usually lower than without it. Does this mean the augmented model is worse? Explain.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 16**: How much extra training time did augmentation cost in your run (in % or seconds)? Where does this extra time come from?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 17**: For each transformation used in n14, say whether you think it is realistic for steel strips and why. Propose **one** transformation that would **not** make sense for this problem and explain what it could break.

| Transformation | Realistic? Why? |
|---|---|
| Horizontal / vertical flip | |
| Rotation ±15° | |
| Random resized crop | |
| Translation | |
| Brightness / contrast | |

**Question 18**: Why must validation and test images **never** be augmented?

A) Because augmentation is too slow to apply at inference  
B) Because we want to measure performance on images like the real ones, always in the same way  
C) Because PyTorch does not allow it  
D) Because augmented images have a different size  

_Justification:_ ______________________________________________________________

**Question 19**: Choose **one** experiment from the "Things you can try" list of n14 (e.g. remove one transformation, change `TRAIN_SIZES`, add a non-realistic transformation), run it and report the result compared with the original run.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 4: Industrial Reflection

**Question 20**: NEU images were taken with a single setup and the classes are balanced (300 images each). Give two reasons why the accuracy you obtained could be **lower** on a real production line, and what you would do before deploying the model.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 21**: Your plant manager asks: *"Is the model ready to replace the human inspector?"* Answer in 4–6 lines using **your** numbers (recall of the critical class, number of FN in test, most frequent confusions).

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---
