# Complex Function Fitting - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ______________________________
- **Course**: Applications of AI for Industrial Control

---

## Section 1: Theoretical Understanding

### Question 1
What is the mathematical relationship of the target function used in this tutorial?
- a) y = 3*sin(x) + 2*cos(x) - 0.5
- b) y = 3*sin(x) + 2*cos(10x) - 0.5
- c) y = sin(3x) + cos(2x) - 0.5
- d) y = 3x + 2*cos(10x) - 0.5

### Question 2
Why is a simple linear model insufficient for fitting the target function? 
1. ______________________________
2. ______________________________
3. ______________________________

### Question 3
Complete the ComplexNet architecture table:

| Component | Purpose | Configuration |
|-----------|---------|---------------|
| Input Layer | | |
| Hidden Layers | | |
| Activation Functions | | |
| Output Layer | | |

### Question 4
How does increasing hidden layers affect model performance? What are the trade-offs?

*Answer:*
__________________________________________________________________________
__________________________________________________________________________

---

## Section 2: Practical Application

### Question 5
How does noise level affect training? What would happen if noise increased from 0.5 to 2.0?

*Answer:*
__________________________________________________________________________
__________________________________________________________________________

### Question 6
Why might the model perform differently on training range (-4, 4) versus extrapolation beyond this range?

*Answer:*
__________________________________________________________________________
__________________________________________________________________________

### Question 7
Analyze hyperparameter effects:

| Hyperparameter | Too Small | Optimal | Too Large |
|----------------|-----------|---------|-----------|
| Hidden Size | | | |
| Learning Rate | | | |


### Question 8
You observe: Training loss = 0.001, Test loss increases after epoch 500, Training R² = 0.98, Test R² = 0.75

**Diagnosis:** __________________________________________________________________________

**Solutions:** __________________________________________________________________________

---

## Section 3: Problem Solving

### Question 9
**Scenario:** You need to fit a function with higher frequency components: y = sin(x) + 0.5sin(20x) + 0.2sin(100x)

How would you modify the neural network architecture?

**Network depth:** __________________________________________________________________________

**Network width:** __________________________________________________________________________

**Training strategy:** __________________________________________________________________________

**Justification:** __________________________________________________________________________

### Question 10
A neural network produces unrealistic oscillations between data points despite low training/test losses.

**Possible causes:** __________________________________________________________________________

**Solutions:** __________________________________________________________________________

### Question 11
Suggest three optimization strategies for faster training without changing model architecture:

1. __________________________________________________________________________
2. __________________________________________________________________________
3. __________________________________________________________________________

---

## Section 4: Industrial Applications

### Question 12
Provide three real-world industrial scenarios where complex non-linear function fitting is essential:

1. **Scenario:** __________________________________________________________________________
   **Why needed:** __________________________________________________________________________

2. **Scenario:** __________________________________________________________________________
   **Why needed:** __________________________________________________________________________

3. **Scenario:** __________________________________________________________________________
   **Why needed:** __________________________________________________________________________
