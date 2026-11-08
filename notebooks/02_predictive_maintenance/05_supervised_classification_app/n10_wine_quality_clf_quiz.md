# Wine Quality Classification Tutorial - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Wine Quality Classification for Industrial Quality Control

---

## Section 1: Theoretical Understanding

### 1.1 Classification Fundamentals

**Question 1**: What is the primary goal of the wine quality classification tutorial?
- a) To predict wine prices based on quality
- b) To classify wine quality based on physicochemical properties for industrial quality control
- c) To identify wine grape varieties
- d) To predict wine aging potential

**Question 2**: The wine quality dataset uses a quality scale from:
- a) 1-5
- b) 0-10
- c) 3-9
- d) 1-10

**Question 3**: What type of loss function is used for the multi-class wine quality classification?
- a) Mean Squared Error (MSE)
- b) Binary Cross-Entropy
- c) Cross-Entropy Loss with class weights
- d) Hinge Loss

**Question 4**: For industrial quality control, wines with quality scores ≥6 are considered:
- a) Poor quality
- b) Average quality
- c) Acceptable/High quality
- d) Premium quality only

### 1.2 Neural Network Architecture

**Question 5**: Which preprocessing technique is essential for neural networks in this classification task?
- a) One-hot encoding
- b) Feature standardization/scaling
- c) Principal Component Analysis (PCA)
- d) Data augmentation

**Question 6**: Which neural network architecture component helps prevent overfitting in the WineQualityClassifier?
- a) Batch Normalization only
- b) Dropout layers only
- c) Both Batch Normalization and Dropout
- d) ReLU activation functions

**Question 7**: The class weighting in the loss function is used to:
- a) Speed up training
- b) Handle imbalanced quality distribution in the dataset
- c) Reduce model complexity
- d) Improve gradient flow

**Question 8**: Which feature importance method is used for the neural network model?
- a) Gini importance
- b) Permutation importance
- c) Gradient-based importance
- d) SHAP values

---

## Section 2: Practical Applications

### 2.1 Industrial Implementation

**Question 9**: Explain why class weighting is important in this wine quality classification problem. How is it calculated and what problem does it solve?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

**Question 10**: The model shows that 'alcohol content' and 'volatile acidity' are the most important features for quality prediction. However, a domain expert argues that 'pH' should be more important. How would you investigate this discrepancy and what might explain it?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---

## Section 3: Critical Thinking

### 3.1 Model Evaluation and Improvement

**Question 11**: You're implementing this wine quality classification system in a real winery. The production team needs to make binary decisions (accept/reject) based on your multi-class model predictions. Design a decision-making strategy that considers both the predicted quality class and the model's confidence. Include potential actions for uncertain predictions.

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---
