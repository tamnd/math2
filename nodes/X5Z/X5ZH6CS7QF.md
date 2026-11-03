---
tag: X5ZH6CS7QF
kind: definition
name: Rayleigh dissipation function
msc: [70H03, 70F40]
defines: YYVBQ68CXQ
uses: [BCF1EX9W2M, 9WQT2RMGTZ, BEM454AYTT, 0QQCG3JWJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_dissipation_function
---

## Definition

Let a mechanical system have [[generalized coordinates|BCF1EX9W2M]] $q = (q_1, \ldots, q_n)$ and Lagrangian $L(q, \dot q, t)$.
A *Rayleigh dissipation function* is a function of the form
$$F(q, \dot q) = \frac{1}{2} \sum_{i, j = 1}^n c_{ij}(q) \, \dot q_i \dot q_j,$$
where $C(q) = (c_{ij}(q))$ is a symmetric positive semidefinite $n \times n$ matrix for each $q$.
The dissipative [[generalized forces|9WQT2RMGTZ]] are $Q_i = -\partial F / \partial \dot q_i$, and the [[Lagrange equations|BEM454AYTT]] become
$$\frac{d}{dt} \frac{\partial L}{\partial \dot q_i} - \frac{\partial L}{\partial q_i} = -\frac{\partial F}{\partial \dot q_i}, \qquad i = 1, \ldots, n.$$

## Remarks

Since $F$ is homogeneous of degree $2$ in $\dot q$, the power of the dissipative forces is $\sum_i Q_i \dot q_i = -2F \le 0$.
For $L = T - V$ with $T$ quadratic in $\dot q$ and $V = V(q)$, the energy $E = T + V$ therefore satisfies $\dot E = -2F$.

Example: $L = \frac{1}{2} m \dot x^2 - \frac{1}{2} k x^2$ and $F = \frac{1}{2} c \dot x^2$ with $c \ge 0$.
The matrix $(c)$ is positive semidefinite, and the equation is $m \ddot x + c \dot x + k x = 0$, the [[damped harmonic oscillator|0RNXVVTJTJ]].

Non-example: $F = \dot q_1 \dot q_2$ has the matrix with $c_{12} = c_{21} = 1$ and $c_{11} = c_{22} = 0$, which is not positive semidefinite, since its eigenvalues are $\pm 1$ (compare [[positive definite matrices|0QQCG3JWJ4]]).
For $\dot q_1 = 1$, $\dot q_2 = -1$ it gives $F = -1$, so these forces would feed energy into the system.
