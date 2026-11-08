# Wine Quality Regression Tutorial - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Wine Quality Regression for Continuous Quality Assessment

---

## Section 1: Theoretical Understanding

### 1.1 Regression vs Classification

**Question 1**: Why is regression better than multiclass classification for wine quality prediction in industrial quality control?
- a) Regression models are faster to train
- b) Regression provides continuous, precise quality scores rather than discrete categories, enabling more nuanced quality assessment
- c) Classification models require more data
- d) Regression uses less computational resources

**Question 2**: What is the primary difference in output between classification and regression for wine quality?
- a) Classification: 3.2, 5.7, 6.8; Regression: 3, 5, 6, 7
- b) Classification: 3, 4, 5, 6, 7, 8, 9; Regression: 3.2, 5.7, 6.8, 7.3
- c) Both produce the same output format
- d) Classification uses probabilities, regression uses integers

**Question 3**: Which loss function is most appropriate for the wine quality regression task?
- a) Cross-Entropy Loss
- b) Mean Squared Error (MSE)
- c) Binary Cross-Entropy
- d) Hinge Loss

**Question 4**: Which activation function is used in the output layer of the regression neural network?
- a) ReLU
- b) Sigmoid
- c) Softmax
- d) Linear (no activation)

### 1.2 Model Architecture and Training

**Question 5**: What is the purpose of scaling both features (X) and target (y) in the regression model?
- a) To make training faster only
- b) To facilitate neural network convergence and improve gradient flow for both inputs and outputs
- c) To reduce memory usage
- d) To prevent overfitting only

**Question 6**: The WineQualityRegressor includes dropout layers for:
- a) Faster training
- b) Uncertainty quantification and overfitting prevention
- c) Better gradient flow
- d) Memory optimization

**Question 7**: What is the purpose of the `predict_with_uncertainty()` method in the regression model?
- a) To make predictions faster
- b) To provide confidence intervals and uncertainty estimates for predictions
- c) To improve model accuracy
- d) To reduce computational cost

**Question 8**: What does the difference between MSE and MAE as regression metrics represent?
- a) MSE and MAE are identical
- b) MSE penalizes large errors more heavily (squared), MAE treats all errors equally (absolute)
- c) MSE is for classification, MAE is for regression
- d) MAE is always larger than MSE

---

## Section 2: Model Evaluation

### 2.1 Regression Metrics

**Question 9**: Which metric is most appropriate for evaluating the overall performance of a regression model?
- a) Accuracy
- b) F1-Score
- c) R² (coefficient of determination)
- d) Precision

**Question 10**: What does an R² score of 0.85 indicate?
- a) 85% of data points are correctly classified
- b) 85% of the variance in quality scores is explained by the model
- c) The model has 15% error rate
- d) 85% accuracy in predictions

**Question 11**: The residual analysis in regression helps to:
- a) Speed up training
- b) Identify prediction patterns and model bias
- c) Reduce model complexity
- d) Increase accuracy

### 2.2 Industrial Applications

**Question 12**: In the context of continuous quality scoring, what advantage does regression provide for industrial applications? Provide specific examples of how precise quality measurements benefit manufacturing processes.

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---

## Section 3: Practical Implementation

### 3.1 Uncertainty Quantification

**Question 13**: Describe the uncertainty quantification approach used in the wine quality regressor. How does the model provide confidence intervals for its predictions and why is this important for industrial applications?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

### 3.2 Loss Function Selection

**Question 14**: Compare the advantages and disadvantages of using MSE vs MAE as loss functions for wine quality regression. When would you choose one over the other in an industrial setting?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---

## Section 4: Critical Thinking

### 4.1 Industrial Implementation Strategy

**Question 15**: You're deploying this regression model in a winery that produces 10,000 bottles per day. The quality team wants to use your model to optimize blending decisions (mixing different batches to achieve target quality scores). Design a strategy that uses the regression model's continuous predictions and uncertainty estimates to make optimal blending recommendations.

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---
