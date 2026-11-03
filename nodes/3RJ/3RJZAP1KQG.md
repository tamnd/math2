---
tag: 3RJZAP1KQG
kind: statement
role: theorem
name: Duality of controllability and observability
msc: [93B05, 93B07, 93C05]
uses: [A9WFM77Z4P, C4HN3EAQWM, 9NSCZ2KBEB, 09DXWYRD43, 0ZC9YTXZRY, 703MCKB5SZ, 9YEW705KHA]
about: [A9WFM77Z4P, C4HN3EAQWM]
sources:
  - url: https://en.wikipedia.org/wiki/Observability
---

## Statement

Let $n, m, p \ge 1$, and let $A$, $B$, $C$ be real matrices of sizes $n \times n$, $n \times m$ and $p \times n$.

1. The system $x' = Ax + Bu$ is [[controllable|A9WFM77Z4P]] if and only if the system $z' = A^T z$, $w = B^T z$ is [[observable|C4HN3EAQWM]].
2. The system $x' = Ax$, $y = Cx$ is observable if and only if the system $z' = A^T z + C^T v$ is controllable.

Here $A^T$, $B^T$, $C^T$ are the [[transposes|09DXWYRD43]].

## Remarks

By the [[Kalman rank condition|9NSCZ2KBEB]], controllability of $(A, B)$ means that $\begin{pmatrix} B & AB & \cdots & A^{n-1} B \end{pmatrix}$ has [[rank|0ZC9YTXZRY]] $n$.
Observability of $(B^T, A^T)$ means that the matrix with block rows $B^T, B^T A^T, \ldots, B^T (A^T)^{n-1}$ has rank $n$.
This matrix is the transpose of the first one, since $(A^k B)^T = B^T (A^T)^k$, and a matrix and its transpose have the same rank; part 2 is part 1 applied to $(A^T, C^T)$.
The same duality holds for the Gramians: the [[controllability Gramian|703MCKB5SZ]] of $(A, B)$ equals the [[observability Gramian|9YEW705KHA]] of the pair $A^T$, $B^T$.
Example: $x_1' = x_2$, $x_2' = u$ is controllable, so $z_1' = 0$, $z_2' = z_1$, $w = z_2$ is observable; indeed $w(t) = z_2(0) + t z_1(0)$ determines $z(0)$.

## Explanations

### L1 human

Controllability asks whether the input can reach every direction of the state.
Observability asks whether the output can see every direction of the state.
Transposing the matrices swaps these two questions.
So every fact about one of them gives a fact about the other for free.

### L2 human

Duality is used all the time in linear control.
The [[Kalman rank condition|9NSCZ2KBEB]] for controllability gives the rank test for observability.
Pole placement by state feedback gives the design of observers, since the eigenvalues of $A - LC$ are those of $A^T - C^T L^T$.
In the same way stabilizability and detectability are dual, and the Riccati equations of optimal control and of Kalman filtering are dual to each other.
The duality is algebraic and also holds for discrete-time systems $x_{k+1} = A x_k + B u_k$.
