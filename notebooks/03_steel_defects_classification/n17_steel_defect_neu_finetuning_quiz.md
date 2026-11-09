# Fine-Tuning for Steel Inspection with Few Images (n17) - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:: se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF. Cuando una pregunta pida cifras, cópialas de **vuestra** ejecución (y, si habéis cambiado algún parámetro, indicad cuál).

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: P6 (II) - Pre-trained ResNet18 (feature extractor and fine-tuning) vs. training from scratch on NEU

## 📋 Instructions
Run `n17_steel_defect_neu_finetuning_resnet18.ipynb` completely (with a GPU if possible) with `QUICK_RUN = False`. If you had to change any parameter (epochs, image size...), say so. For multiple-choice questions, choose one option **and justify it**.

---

## Section 1: Concepts

**Question 1**: Explain in your own words the difference between the three strategies. Fill the table using the numbers printed by **your** notebook:

| Strategy | Initial weights | Which layers are trained | Trainable parameters (your run) |
|---|---|---|---|
| From scratch | | | |
| Feature extractor | | | |
| Fine-tuning | | | |

**Question 2**: ResNet18 was pre-trained on ImageNet (photos of animals, objects, vehicles...). Why can its filters be useful for gray images of steel surfaces? Which layers do you expect to be more "generic" and which more "specific"?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 3**: In fine-tuning, the backbone uses a learning rate 10 times smaller than the new head. Why? What could happen with a large learning rate?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 4**: NEU images are gray (1 channel) but ResNet18 expects 3 channels normalised with the ImageNet mean and std. How does the notebook solve it, and why is it important to use the ImageNet normalisation?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 5**: For the feature extractor the notebook computes the features of all the images **only once**. Why is this correct only when the backbone is frozen? What is the practical advantage?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 6**: Why does the notebook guarantee a minimum number of weight updates (`MIN_STEPS`) instead of only a fixed number of epochs?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 2: Your Results

**Question 7**: Copy the results table of **your** run (test accuracy):

| Strategy | 10 images/class | 50 images/class | 180 images/class | Training time (all sizes) |
|---|---|---|---|---|
| From scratch | | | | |
| Feature extractor | | | | |
| Fine-tuning | | | | |

Insert or describe your plot *accuracy vs. number of images*.

**Question 8**: Using your plot: how does the advantage of the pre-trained models over training from scratch change when the number of images grows? Why?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 9**: With **10 images per class**, look at the three confusion matrices. Which classes are most confused by each strategy? Is it the same pair as in n13?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 10**: Compare the **validation** and **test** accuracy of your experiments. Are they close? With only 10 images/class, why can the result change a lot if we pick other 10 images? (Optional: run with `REPEATS = 3` and report mean ± std.)

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 11**: Compare the training time of the three strategies in your run. Which strategy would you choose if you had to retrain the model every week on an industrial PC without a GPU? Justify with your numbers.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 3: Experiments and Industrial Reflection

**Question 12**: Choose one experiment and report it compared with your original run:
- unfreeze also `layer2`, or
- use the same learning rate (1e-3) for the backbone, or
- remove the flips.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 13**: A new production line will start next month and you can label at most 20 images per defect type during the first week. Which strategy would you use to have a first model, and how would you improve it over time? Base your answer on your results.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 14**: Which statement best summarises **your** results?

A) Training from scratch is always the best option if we train long enough  
B) With few images, starting from pre-trained weights gives much better results than starting from random weights  
C) Pre-training only helps if the new images are similar to ImageNet photos  
D) Fine-tuning always beats the feature extractor  

_Justification with your numbers:_ ______________________________________________________________

---
