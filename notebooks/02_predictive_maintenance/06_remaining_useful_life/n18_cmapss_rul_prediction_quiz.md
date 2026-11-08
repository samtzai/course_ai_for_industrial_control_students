# Remaining Useful Life with NASA C-MAPSS (n18) - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:: se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF. Cuando una pregunta pida cifras, cópialas de **vuestra** ejecución (y, si habéis cambiado algún parámetro, indicad cuál).

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: RUL prediction on FD001: hand-crafted features + MLP vs. 1D-CNN vs. LSTM

## 📋 Instructions
Run `n18_cmapss_rul_prediction.ipynb` completely with `QUICK_RUN = False`. When a question asks for numbers or figures, use **your** run.

---

## Section 1: Problem and Data Preparation

**Question 1**: Why is RUL estimation a **regression** problem and not a classification problem? Give an industrial example (different from turbofans) where it would be useful.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 2**: The training and validation targets are clipped at `RUL_CAP = 125`, while test metrics use the original RUL values. Explain with the target plot why clipping can be reasonable for training. What changes when evaluating against the un-clipped test RUL?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 3**: The notebook splits training and validation **by engine** and not by window. What would happen to the validation RMSE if we split by window? Why?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 4**: Which sensors were dropped in your run based on the training engines only, and why? Look at the sensor plot: describe the trend of two of the sensors you kept when the engine approaches failure.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 5**: What is a sliding window? Indicate the shape of the training tensor printed by your notebook and explain each dimension.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 2: Models

**Question 6**: Explain in your own words how each model "sees" the time information:

| Model | How does it use the 30 cycles of the window? | Parameters (your run) |
|---|---|---|
| Hand-crafted + MLP | | |
| 1D-CNN | | |
| LSTM | | |

**Question 7**: In the 1D-CNN the input is transposed from `(batch, time, sensors)` to `(batch, sensors, time)`. Why? What plays the role of the "channels" here, compared with an RGB image?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 8**: The LSTM uses only the hidden state of the **last** time step to predict the RUL. Why is that enough? What does the hidden state contain?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 3: Your Results and the Asymmetric Metric

**Question 9**: Copy the final results table of **your** run, keeping validation and test metrics clearly separate. Validation targets are clipped; test metrics use the original, un-clipped RUL:

| Model | Val RMSE | Val NASA score | Test RMSE (raw RUL) | Test NASA score (raw RUL) | Training time (s) |
|---|---:|---:|---:|---:|---:|
| Hand-crafted + MLP | | | | | |
| 1D-CNN | | | | | |
| LSTM | | | | | |

Which model was selected using validation NASA score (with validation RMSE as tie-breaker)? Compare its validation and test results. Explain why test results must not be used to select a model.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 10**: Explain the NASA scoring function with an example: compute the penalty of one engine predicted **10 cycles early** and of one predicted **10 cycles late**. Why does the metric penalise late predictions more?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 11**: Look at the RUL trajectories of the test and validation engines. Where do the models make the largest errors (beginning, middle or end of life)? Is this good or bad from a maintenance point of view?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 12**: In the "safety margin" section, which margin was chosen using validation in your run? Report the final test RMSE and NASA score before and after applying it, against the original test RUL. Why can a worse RMSE be acceptable?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---

## Section 4: Experiments and Reflection

**Question 13**: Change **one** of these parameters, re-run and compare with your original results: `WINDOW` (15 or 50), `RUL_CAP` (100 or 150) or `EPOCHS`. Explain the change you observe.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 14**: Propose how to train the model so that it is late less often, **without** adding a margin after training (hint: the loss function). Write the idea or the PyTorch code.

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

**Question 15**: FD001 has a single operating condition and a single failure mode. What would change in a real fleet (several operating conditions, sensors with different drift, few run-to-failure examples)? What would you do?

_Your answer:_

_______________________________________________________________________________

_______________________________________________________________________________

---
