---
tag: FV1E09CJQN
kind: definition
name: Riccati differential equation of optimal control
msc: [49N10, 34A34, 93C05]
defines: Y4V154JWR7
uses: [0VR671PHE5, 01MMVW8CKC, 0KX66CZMBB, 0VT2QK6X6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Riccati_equation
---

## Definition

Let $n, m \ge 1$ and $T > 0$.
Let $A$ be a real $n \times n$ matrix and $B$ a real $n \times m$ matrix.
Let $Q$ and $F$ be [[symmetric|0VR671PHE5]] [[positive semidefinite|01MMVW8CKC]] $n \times n$ matrices, and let $R$ be a symmetric [[positive definite|0KX66CZMBB]] $m \times m$ matrix.
The *Riccati differential equation* of the associated linear-quadratic problem is the terminal value problem
$$-P'(t) = A^{T} P(t) + P(t) A - P(t) B R^{-1} B^{T} P(t) + Q, \qquad P(T) = F,$$
for a differentiable function $P \colon (-\infty, T] \to \R^{n \times n}$ with symmetric values.

## Remarks

Under these hypotheses the solution exists on all of $(-\infty, T]$, and $P(t)$ is symmetric positive semidefinite for every $t$.
Example: $n = m = 1$, $A = 0$, $B = Q = R = 1$ and $F = 0$ give $-P' = 1 - P^2$, $P(T) = 0$.
The solution is $P(t) = \tanh(T - t)$: indeed $P'(t) = -(1 - \tanh^2(T - t)) = -(1 - P(t)^2)$ and $P(T) = 0$.
As $t \to -\infty$, $P(t) \to 1$, the positive solution of the algebraic equation $1 - P^2 = 0$.
Non-example: the linear equation $-P' = A^{T} P + P A + Q$ is a Lyapunov differential equation, not a Riccati equation, since it lacks the quadratic term.
It gives the cost of the zero control; with $A - BK$ in place of $A$ and $Q + K^{T} R K$ in place of $Q$ it gives the cost of a fixed linear feedback $u = -Kx$.
The quadratic term of the Riccati equation accounts for optimizing the control.
For $n = 1$ the equation is a scalar [[Riccati equation|0VT2QK6X6Q]] $P' = q_0 + q_1 P + q_2 P^2$ with constant coefficients.
