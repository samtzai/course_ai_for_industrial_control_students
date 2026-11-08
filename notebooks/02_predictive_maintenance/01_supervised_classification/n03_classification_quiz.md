# Classification Tutorial - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Classification with Iris Dataset using PyTorch

---

## Section 1: Theoretical Understanding

### 1.1 Basic Concepts

**Question 1**: What is the main difference between classification and regression tasks?
- a) Classification predicts continuous values, regression predicts categories
- b) Classification predicts categories, regression predicts continuous values
- c) Classification uses neural networks, regression uses linear models
- d) There is no difference between them

**Question 2**: In the Iris dataset tutorial, what are the parameters w and b in a neural network layer `y = wx + b`?
- w: ________________________________
- b: ________________________________

**Question 3**: List three evaluation metrics used in the classification tutorial and briefly explain when each is most important:
1. ________________________________
2. ________________________________
3. ________________________________

**Question 4**: What is the purpose of feature scaling (StandardScaler) in our classification pipeline? Explain why this preprocessing step is crucial for neural networks.

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

### 1.2 Training Process

**Question 5**: Describe the four main steps of the PyTorch training loop for classification:
1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________

**Question 6**: What is CrossEntropyLoss and why is it preferred over MSE for multi-class classification problems?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

**Question 7**: Explain the difference between training accuracy and test accuracy. Why might test accuracy be lower than training accuracy?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

### 1.3 Model Architecture

**Question 8**: Compare the three model architectures explored in the tutorial:

| Architecture | Number of Parameters | Best Use Case | Activation Functions |
|--------------|---------------------|---------------|---------------------|
| Linear-only  |                     |               |                     |
| Hidden layers|                     |               |                     |
| Deep network |                     |               |                     |

**Question 9**: What is overfitting in classification? How can you detect it using the confusion matrix and accuracy metrics shown in the tutorial?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

**Question 10**: If your model shows 95% training accuracy but only 75% test accuracy, what does this indicate about your model?

_Your answer:_
_______________________________________________________________________________

---

## Section 2: Practical Application

### 2.1 Dataset Analysis

**Question 11**: About the Iris dataset used in the tutorial:
- a) How many classes? ________________________________
- b) How many features? ________________________________
- c) Which species is most easily separable? ________________________________
- d) Which features are most discriminative? ________________________________
- e) Why is this dataset good for learning classification? ________________________________

**Question 12**: Explain how the decision boundary visualization helps understand the classification process. What do the colored regions represent?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

### 2.2 Evaluation Metrics

**Question 13**: Calculate accuracy from this confusion matrix:

```
           Predicted
Actual   Setosa  Versicolor  Virginica
Setosa      15       0          0
Versicolor   0      12          3  
Virginica    0       2         13
```

**Accuracy = ____________**

**Show calculation:** ________________________________________________

**Question 14**: A quality control classifier for industrial parts has:
- Correctly identified defective parts: 45
- False alarms (good parts classified as defective): 8
- Missed defects (defective parts classified as good): 5
- Correctly identified good parts: 142

**Calculate:**
- Precision = ____________
- Recall = ____________
- F1-Score = ____________

**Which metric is most critical for safety and why?**
_______________________________________________________________________________

---

## Section 3: Problem Solving

### 3.1 Scenario Analysis

**Question 15**: You're training a 3-class classifier and observe:
- Training accuracy increases to 98% over 200 epochs
- Test accuracy peaks at 85% after 50 epochs, then decreases
- Confusion matrix shows perfect classification on training data

Analyze this scenario:
1. Is the model learning properly? ________________________________
2. What problem is occurring? ________________________________
3. At what epoch should you stop training? ________________________________
4. What techniques could prevent this issue? ________________________________

**Question 16**: A student tests different neural network architectures on the Iris dataset. The following test accuracies are illustrative:
- Linear model (4 → 3, no hidden layers): Test accuracy = 95%, 15 parameters
- `IrisClassifier(hidden_size=10)` (two hidden layers of 10): Test accuracy = 97%, 193 parameters
- Dynamic classifier with one hidden layer of 10: Test accuracy = 97%, 83 parameters
- Dynamic classifier with three hidden layers of 50: Test accuracy = 93%, 5503 parameters

Which model would you recommend and why? Consider performance, complexity, and generalization. Compare these examples with your own test results.

_Your recommendation and justification:_
_______________________________________________________________________________
_______________________________________________________________________________

### 3.2 Code Understanding

**Question 17**: In the PyTorch classification implementation, what does this code sequence accomplish?
```python
model.eval()
with torch.no_grad():
    outputs = model(X_test)
    _, predicted = torch.max(outputs, 1)
```

_Your explanation:_
_______________________________________________________________________________
_______________________________________________________________________________

**Question 18**: Why do we use `torch.max(outputs, 1)` in classification? What do the outputs represent before and after this operation?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

---

## Section 4: Critical Thinking

### 4.1 Real-World Applications

**Question 19**: Give three examples of industrial classification scenarios where this tutorial's concepts apply, and explain the specific classification task.

1. ________________________________
   Classification task: ________________________________

2. ________________________________
   Classification task: ________________________________

3. ________________________________
   Classification task: ________________________________

**Question 20**: What limitations of the Iris dataset might not represent real industrial classification challenges? How would you adapt the approach for industrial applications?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

### 4.2 Reflection and Learning

**Question 21**: What was the most valuable insight you gained from the interactive visualizations (decision boundaries, confusion matrices, training curves)? How did they enhance your understanding?

_Your reflection:_
_______________________________________________________________________________
_______________________________________________________________________________

**Question 22**: If you were to teach classification to another student, what would be the three most important concepts to emphasize and why?

1. ________________________________
   Why: ________________________________

2. ________________________________
   Why: ________________________________

3. ________________________________
   Why: ________________________________

---
