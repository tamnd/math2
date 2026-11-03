---
tag: Q13W8D9PCH
kind: definition
name: Replicator equation
msc: [91A22, 37N25, 92D25]
defines: 42AC07NXK0
uses: [0NT64JV96A, YX1DJK2QAG, 5MZTZRC3CZ]
sources:
  - url: https://en.wikipedia.org/wiki/Replicator_equation
---

## Definition

Let $A$ be a real $n \times n$ matrix, the payoff matrix of a symmetric two-player [[normal-form game|5MZTZRC3CZ]].
Let $\Delta_n = \set{x \in \R^n : x_i \ge 0 \text{ for all } i, \ x_1 + \cdots + x_n = 1}$ be the standard [[simplex|YX1DJK2QAG]], whose points are population states.
The *replicator equation* is the system of [[ordinary differential equations|0NT64JV96A]]
$$\dot x_i = x_i \big( (A x)_i - x^T A x \big), \quad i = 1, \dots, n,$$
for $x \in \Delta_n$.
Here $(A x)_i$ is the payoff of strategy $i$ against the population state $x$, and $x^T A x$ is the average payoff in the population.

## Remarks

The sum $\sum_i \dot x_i = x^T A x - x^T A x \cdot \sum_i x_i$ vanishes on $\Delta_n$, and $\dot x_i = 0$ whenever $x_i = 0$.
So the simplex and each of its faces are invariant: a strategy that is absent stays absent.
More generally, for fitness functions $f_i$ one writes $\dot x_i = x_i (f_i(x) - \bar f(x))$ with $\bar f(x) = \sum_j x_j f_j(x)$.
Adding the same constant to a column of $A$ does not change the solutions.

Example: for the Hawk–Dove matrix $A = \begin{pmatrix} -1 & 2 \\ 0 & 1 \end{pmatrix}$, write $x$ for the share of hawks.
The payoffs are $2 - 3x$ for Hawk and $1 - x$ for Dove, and the equation reduces to $\dot x = x (1 - x)(1 - 2x)$.
For $0 < x < 1/2$ the share grows and for $1/2 < x < 1$ it shrinks, so every interior solution tends to $1/2$.

Non-example: the system $\dot x_i = (A x)_i$ is not the replicator equation.
It does not keep $\sum_i x_i = 1$, so solutions leave the simplex and no longer describe population shares.
