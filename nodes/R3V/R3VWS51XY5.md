---
tag: R3VWS51XY5
kind: definition
name: Hurwitz-stable matrix
msc: [15A18, 34D20]
defines: 9A3TBBHRFA
uses: [0JXZKX526R, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz-stable_matrix
---

## Definition

Let $A$ be an $n \times n$ [[square matrix|0JXZKX526R]] with real or complex entries.
The matrix $A$ is *Hurwitz-stable* if every [[eigenvalue|0BQAA2BK3Q]] $\lambda$ of $A$ satisfies $\operatorname{Re} \lambda < 0$.

## Remarks

Equivalently, $e^{tA} \to 0$ as $t \to \infty$, that is, the origin is asymptotically stable for $x' = Ax$.
Then there are $C \ge 1$ and $\alpha > 0$ with $\norm{e^{tA}} \le C e^{-\alpha t}$ for all $t \ge 0$.
A real matrix $A$ is Hurwitz-stable if and only if, for one (equivalently, every) positive definite matrix $Q$, the [[Lyapunov equation|92GVPZH9FT]] $A^T P + P A = -Q$ has a positive definite solution $P$.

Example: $A = \begin{pmatrix} -1 & 2 \\ 0 & -3 \end{pmatrix}$.
It is triangular, so its eigenvalues are its diagonal entries $-1$ and $-3$, both with negative real part.

Non-example: $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
Its eigenvalues are $\pm i$, with real part $0$, so $A$ is not Hurwitz-stable; the solutions of $x' = Ax$ are rotations that do not decay.

For a real matrix, the condition can be tested on the coefficients of the characteristic polynomial by the Routh–Hurwitz criterion.
