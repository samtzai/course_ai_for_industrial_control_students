# Q-Learning Grid Robot Navigation Tutorial - Evaluation Questionnaire

- **Grupo:** ________________________________
- **Nombres:** ________________________________
- **Uso de IA: no / sí, para…** ________________________________

Criterio de corrección:se valora sobre todo que entendáis los conceptos y los expliquéis con vuestras palabras y vuestros resultados.

Entrega el cuestionario en formato `.md`, no PDF.

## Student Information
- **Date**: ________________________________
- **Course**: Applications of AI for Industrial Control
- **Tutorial**: Q-Learning for 2D Grid Robot Navigation

---

## Section 1: Basic Concepts

### 1.1 Environment Understanding

**Question 1**: What is the main goal of the robot in the grid world environment?
- a) Reach the goal position while avoiding traps
- b) Visit every cell in the grid exactly once
- c) Reach the goal position in the minimum number of steps
- d) Stay in the start position and avoid moving

**Question 2**: In the 5x5 grid world setup, identify the correct configuration:
- Start position: ________________________________
- Goal position: ________________________________
- Goal reward: ________________________________
- Trap positions: ________________________________
- Step cost: ________________________________

**Question 3**: What does the Q-value Q(s,a) represent in Q-learning?
- a) The immediate reward for taking action a in state s
- b) The expected cumulative reward for taking action a in state s and following the optimal policy thereafter
- c) The probability of taking action a in state s
- d) The number of times action a has been taken in state s

**Question 4**: What are the four possible actions available to the robot in the grid world?
1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________

### 1.2 Basic Q-Learning Mechanics

**Question 5**: What happens when the robot tries to move outside the grid boundaries?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

---

## Section 2: Q-Learning Algorithm

### 2.1 Mathematical Foundations

**Question 6**: Complete the Q-learning update rule equation:

Q(s, a) ← Q(s, a) + α [________________________________]

Where:
- s: ________________________________
- a: ________________________________
- α: ________________________________
- γ: ________________________________
- r: ________________________________

**Question 7**: Explain the role of each hyperparameter in Q-learning:

**Learning rate (α = 0.1):**
_______________________________________________________________________________

**Discount factor (γ = 0.9):**
_______________________________________________________________________________

**Initial epsilon (ε = 1.0):**
_______________________________________________________________________________

### 2.2 Training Process

**Question 8**: Describe the four main steps of the Q-learning training loop in order:
1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________

**Question 9**: What is the epsilon-greedy policy and why is it important?

_Definition:_
_______________________________________________________________________________

_Importance:_
_______________________________________________________________________________

---

## Section 3: Exploration vs Exploitation

### 3.1 Strategy Understanding

**Question 10**: If epsilon = 0.2, what percentage of the time will the agent:
- Explore (random action): ________________________________%
- Exploit (best known action): ________________________________%

**Question 11**: Why does epsilon typically decay during training?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

**Question 12**: What would happen if we set:
- **Learning rate α = 0** : ________________________________
- **Discount factor γ = 0** : ________________________________

### 3.2 Performance Analysis

**Question 13**: Why might the success rate be low in early episodes but improve over time?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

---

## Section 4: Training Process and Results

### 4.1 Performance Monitoring

**Question 14**: What information is tracked during training to monitor the agent's performance?

List at least 4 metrics:
1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________

**Question 15**: What does it mean when the Q-values "converge" during training?

_Your answer:_
_______________________________________________________________________________
_______________________________________________________________________________

### 4.2 Critical Analysis

**Question 16**: You observe during training that:
- Episode rewards increase steadily for 200 episodes then plateau
- Success rate reaches 85% by episode 150
- Q-values for optimal state-action pairs stabilize around episode 180
- Epsilon has decayed from 1.0 to 0.1

Analyze this scenario and explain what this indicates about the learning process:

_Your analysis:_
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---
