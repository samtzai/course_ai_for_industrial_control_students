# Overfitting and Underfitting Tutorial - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Overfitting and Underfitting in Neural Networks

---

## Section 1: Fundamentals

### 1.1 Basic Concepts

**Question 1**: What is the primary characteristic of an overfitted model?
- a) High training error and high validation error
- b) Low training error and high validation error
- c) High training error and low validation error
- d) Low training error and low validation error

**Question 2**: Which of the following is NOT a common regularization technique?
- a) Dropout
- b) L2 regularization
- c) Early stopping
- d) Increasing model complexity

**Question 3**: Adding more training data can help reduce overfitting.
- **True/False**: ___________

_Explanation:_
_______________________________________________________________________________

**Question 4**: What does the bias-variance trade-off describe?
- a) The relationship between model accuracy and training time
- b) The balance between model simplicity and flexibility
- c) The trade-off between training and validation loss
- d) The relationship between dataset size and model performance

**Question 5**: Fill in the blanks: A model with high bias and low variance is likely to exhibit __________, while a model with low bias and high variance is likely to exhibit __________.

_Your answer:_
_______________________________________________________________________________

---

## Section 2: Noise and Dataset Size Effects

### 2.1 Model Architecture and Data Complexity

**Question 6**: When training a neural network on noisy data, which model architecture is most likely to overfit?
- a) Simple model (5 neurons)
- b) Medium model (32-16 neurons)
- c) Complex model (128-64-32 neurons)
- d) All models overfit equally

**Question 7**: With a very small dataset (e.g., 20 samples), which strategy is most effective?
- a) Use a complex model with heavy regularization
- b) Use a simple model with light regularization
- c) Increase the number of training epochs
- d) Remove regularization entirely

---

## Section 3: Regularization Techniques

### 3.1 Regularization Methods

**Question 8**: Compare the effectiveness of dropout vs L2 regularization. When would you choose one over the other?

_Your answer:_
- Dropout: _______________________________________________________________________________
- L2 regularization: ______________________________________________________________________
- When to use each: ______________________________________________________________________

**Question 9**: Early stopping can be considered a form of regularization.
- **True/False**: ___________

_Explanation:_
_______________________________________________________________________________
_______________________________________________________________________________

---

## Section 4: Industrial Applications

### 4.1 Practical Implementation

**Question 10**: In an industrial monitoring system using neural networks, list three strategies you would implement to prevent overfitting when sensor data is noisy and limited.

_Strategies:_
1. _______________________________________________________________________________
2. _______________________________________________________________________________
3. _______________________________________________________________________________

**Question 11**: For a real-time industrial control system, which factor is most critical when selecting a model?
- a) Highest possible accuracy on training data
- b) Balance between accuracy and generalization
- c) Fastest training time
- d) Most complex architecture

---

## Section 5: Critical Analysis

### 5.1 Calculation and Analysis

**Question 12**: Given the following training results for a neural network:

```
Training MSE: 0.05
Validation MSE: 0.25
Test MSE: 0.30
```

Calculate the overfitting ratio (Validation MSE / Training MSE) and interpret what this indicates about the model.

**Overfitting Ratio:** ___________

_Interpretation:_
_______________________________________________________________________________
_______________________________________________________________________________

### 5.2 Problem Solving

**Question 13**: You are developing a neural network for predictive maintenance in a manufacturing plant. The training dataset is small (100 samples) and noisy due to sensor limitations.

Describe your complete strategy for:
1. Model architecture selection
2. Regularization approach
3. Training procedure
4. Validation strategy

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---
