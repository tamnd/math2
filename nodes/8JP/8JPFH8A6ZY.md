---
tag: 8JPFH8A6ZY
kind: definition
name: Partially observable Markov decision process
msc: [90C40, "93E20", "93E11"]
defines: B7XZ76EX1T
uses: [EC0HKSBVQ7, 0NM6E9VW04, HJVM390354]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process
    locator: Definition
---

## Definition

A *partially observable Markov decision process* is a tuple $(S, A, P, r, \Omega, O, \gamma)$ where:

1. $(S, A, P, r, \gamma)$ is a discounted [[Markov decision process|WCNHWTJXYD]] with finite sets $S$ of states and $A$ of actions;
2. $\Omega$ is a finite set of observations;
3. $O$ gives, for each $a \in A$ and $s' \in S$, a probability distribution $O(\cdot \mid s', a)$ on $\Omega$.

The state evolves as in the Markov decision process, but the controller does not see it.
After action $a_t$ leads to state $s_{t+1}$, the controller receives an observation $o_{t+1}$ drawn from $O(\cdot \mid s_{t+1}, a_t)$.
A policy chooses $a_t$ as a function of an initial distribution $b_0$ on $S$ and of the past actions and observations $a_0, o_1, \dots, a_{t-1}, o_t$ only.
The aim is to maximize $\mathbb{E}\big[\sum_{t \ge 0} \gamma^t r(s_t, a_t)\big]$, where $s_0$ has law $b_0$.

## Remarks

The *belief* $b_t$ is the conditional law of $s_t$ given $b_0$ and the past actions and observations.
By [[Bayes' theorem|0NM6E9VW04]], after action $a$ and observation $o$ it updates to
$$b'(s') = \frac{O(o \mid s', a) \sum_{s \in S} P(s' \mid s, a) \, b(s)}{\sum_{s'' \in S} O(o \mid s'', a) \sum_{s \in S} P(s'' \mid s, a) \, b(s)}$$
whenever the denominator is positive.
The beliefs form a Markov decision process on the simplex of distributions on $S$, the belief MDP.
Optimal policies can be taken to depend on the history only through $b_t$.

Example: the tiger problem has $S = \set{\text{left}, \text{right}}$ for the side of a hidden tiger, actions listen, open left, open right, and observations "hear left", "hear right".
Listening leaves the state unchanged and gives the correct side with probability $0.85$; clauses 1 to 3 hold.

Non-example: suppose the observation law depends on a quantity outside $S$ and $A$, such as a hidden sensor fault that is not part of the state.
This fails clause 3, and the model must be repaired by adding that quantity to the state.
