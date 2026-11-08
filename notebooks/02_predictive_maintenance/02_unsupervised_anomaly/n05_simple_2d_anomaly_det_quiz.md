# Simple 2D Anomaly Detection Tutorial - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Simple 2D Gaussian Anomaly Detection

---

## Section 1: Theoretical Understanding

### 1.1 Gaussian Model Fundamentals

**Question 1**: What are the main parameters that define a Gaussian multivariate distribution for 2D data?
- a) Only the mean vector
- b) Only the covariance matrix
- c) Mean vector and covariance matrix
- d) Standard deviation and correlation coefficient

**Question 2**: In the tutorial dataset, what were the three types of anomalies generated?
- a) High temperature, Low pressure, Medium values
- b) High temperature, High pressure, Low temperature-pressure
- c) Overheating, Undercooling, Normal operation
- d) Temperature spikes, Pressure drops, Random noise

**Question 3**: True/False: The Gaussian anomaly detector requires labeled anomaly data during training.

Answer: ___________

Explanation: ________________________________________________

### 1.2 Anomaly Scoring

**Question 4**: What does a higher anomaly score indicate?
- a) Higher probability of being normal
- b) Lower probability of being normal
- c) Data point is closer to the mean
- d) Data point has higher variance

**Question 5**: The anomaly score is calculated as `-log(density + 1e-10)`. Explain why a lower probability density results in a higher anomaly score.

Answer: ________________________________________________

---

## Section 2: Visualization and Interpretation

### 2.1 2D Visualization

**Question 6**: Explain what probability contours represent in your 2D visualization, why the Gaussian decision boundary is elliptical (quadratic), and how the contours help you understand your results.

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

**Question 7**: In the tutorial, what happened to the decision boundary when the threshold percentile was increased from 85% to 95%?
- a) The boundary became more restrictive (smaller normal region)
- b) The boundary became less restrictive (larger normal region)
- c) The boundary shape changed but size remained the same
- d) No change occurred in the boundary

**Question 8**: Describe the difference between True Positives, False Positives, True Negatives, and False Negatives in the context of anomaly detection.

- True Positives: _____________________________________________
- False Positives: ____________________________________________
- True Negatives: _____________________________________________
- False Negatives: ____________________________________________

---

## Section 3: Performance Metrics

### 3.1 Metrics Calculation

**Question 9**: What does the F1-score represent in anomaly detection?
- a) The accuracy of the model
- b) The harmonic mean of precision and recall
- c) The area under the ROC curve
- d) The correlation between features

**Question 10**: Given the following confusion matrix for an anomaly detection model:

```
              Predicted
              Normal  Anomaly
Actual Normal   450      50
       Anomaly   15      35
```

Calculate:
- Precision: ___________
- Recall: ___________
- F1-Score: ___________

Show your calculations:
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

**Question 11**: What is the trade-off when selecting threshold percentiles?
- a) High percentile: More false positives, fewer false negatives
- b) High percentile: Fewer false positives, more false negatives
- c) Low percentile: Fewer false positives, more false negatives
- d) Percentile has no effect on false positives/negatives

---

## Section 4: Industrial Applications

### 4.1 Real-World Applications

**Question 12**: List three real-world industrial applications where 2D Gaussian anomaly detection could be effectively used. For each application, specify the two variables that would be monitored.

Applications:
1. _______________________________________________________________________________
2. _______________________________________________________________________________
3. _______________________________________________________________________________

**Question 13**: Which of the following is NOT a limitation of the Gaussian multivariate method?
- a) Assumes data follows Gaussian distribution
- b) Cannot represent arbitrary complex anomaly patterns with one elliptical boundary
- c) Requires large amounts of labeled training data
- d) Sensitive to outliers in training data

---

## Section 5: Critical Thinking

### 5.1 Implementation Strategy

**Question 14**: You are implementing anomaly detection for a manufacturing process that monitors motor temperature and vibration. Based on the tutorial concepts:

1. How would you collect and prepare training data?
2. What threshold selection strategy would you use and why?
3. How would you handle the trade-off between false alarms and missed anomalies?
4. What additional considerations would you have for a real industrial deployment?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---
