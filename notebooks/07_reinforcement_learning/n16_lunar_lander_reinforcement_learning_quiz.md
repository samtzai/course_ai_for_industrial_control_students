# Lunar Lander Reinforcement Learning Tutorial - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Deep Q-Network (DQN) for Lunar Lander

---

## Section 1: Environment Understanding

### 1.1 Task Definition

**Question 1**: What is the goal of the Lunar Lander reinforcement learning task?
- a) Reach the highest altitude possible
- b) Land the spacecraft safely while minimizing fuel consumption
- c) Collect as many points as possible by staying in the air
- d) Crash the lander as quickly as possible

**Question 2**: Complete the Lunar Lander environment specifications:
- **State space size**: ________________________________ (number of continuous values)
- **Action space size**: ________________________________ (number of discrete actions)
- **Landing reward**: ________________________________
- **Crash penalty**: ________________________________

### 1.2 Environment Details

**Question 3**: What do the 4 discrete actions represent in the Lunar Lander environment?
- Action 0: ________________________________
- Action 1: ________________________________
- Action 2: ________________________________
- Action 3: ________________________________

**Question 4**: List at least 5 components of the 8-dimensional state vector:
1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________
5. ________________________________

---

## Section 2: Deep Q-Network (DQN) Architecture

### 2.1 Architecture Design

**Question 5**: Why is a neural network used instead of a Q-table in the Lunar Lander problem?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

**Question 6**: What is the purpose of the target network in DQN?
- a) To speed up training
- b) To reduce correlation between Q-value updates and targets
- c) To increase exploration
- d) To reduce memory usage

### 2.2 Network Structure

**Question 7**: In the DQN implementation, what is the typical neural network architecture used?
- Input layer size: ________________________________
- Hidden layers: ________________________________
- Output layer size: ________________________________

**Question 8**: What activation function is used in the hidden layers of the DQN, and why?

_Activation function:_ ________________________________

_Reason:_ _______________________________________________________________________________

---

## Section 3: Training Components

### 3.1 Experience Replay

**Question 9**: Explain the purpose and benefits of Experience Replay in DQN training:

_Purpose:_
_______________________________________________________________________________

_Benefits (list at least 2):_
1. ________________________________
2. ________________________________

**Question 10**: What happens during each training step of the DQN algorithm?

List the 4 main steps in order:
1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________

### 3.2 Loss Function and Updates

**Question 11**: Complete the DQN loss function equation:

Loss = MSE(________________________________, ________________________________)

Where the target is calculated as:
Target = r + γ × ________________________________

**Question 12**: Why is the target network updated less frequently than the main Q-network?

_Your answer:_
_______________________________________________________________________________

---

## Section 4: Hyperparameters and Advanced Concepts

### 4.1 Hyperparameter Analysis

**Question 13**: Match the hyperparameter with its typical value and purpose:

- Learning rate (α): _______ → Controls _________________
- Discount factor (γ): _______ → Controls _________________
- Batch size: _______ → Controls _________________

**Question 14**: Describe the epsilon-greedy strategy used in DQN training:

_Strategy:_
_______________________________________________________________________________

_Why does epsilon decay over time?_
_______________________________________________________________________________

**Question 15**: What does it mean when the Lunar Lander environment is "solved"?

_Criterion:_ _______________________________________________________________________________

### 4.2 Advanced Analysis

**Question 16**: What is the main improvement that Double DQN provides over standard DQN?

_Your answer:_
_______________________________________________________________________________

**Question 17**: During performance analysis, which action would you expect a well-trained agent to use most frequently, and why?

_Most frequent action:_ ________________________________

_Reason:_ _______________________________________________________________________________

---
