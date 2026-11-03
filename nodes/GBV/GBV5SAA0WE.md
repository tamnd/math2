---
tag: GBV5SAA0WE
kind: statement
role: theorem
name: Lyapunov criterion for Hurwitz matrices
msc: [93D05, 15A24, 34D20]
uses: [9A3TBBHRFA, 92GVPZH9FT, 0KX66CZMBB, 0VR671PHE5, 01REYCJ371]
about: [9A3TBBHRFA, 92GVPZH9FT]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_equation
---

## Statement

Let $A$ be a real $n \times n$ matrix.
The following are equivalent.

1. $A$ is [[Hurwitz-stable|9A3TBBHRFA]]: every eigenvalue of $A$ has negative real part.
2. For every [[symmetric|0VR671PHE5]] [[positive definite|0KX66CZMBB]] $n \times n$ matrix $Q$, the [[Lyapunov equation|92GVPZH9FT]] $A^T P + P A = -Q$ has a unique solution $P$, and $P$ is symmetric positive definite.
3. There is a symmetric positive definite matrix $P$ such that $A^T P + P A$ is negative definite.

## Remarks

If $A$ is Hurwitz, the solution in (2) is $P = \int_0^\infty e^{A^T t} Q e^{A t} \, dt$; the integral converges because $e^{At}$ decays exponentially, and $x^T P x = \int_0^\infty \abs{Q^{1/2} e^{At} x}^2 \, dt > 0$ for $x \ne 0$.
Uniqueness holds because the map $P \mapsto A^T P + PA$ has eigenvalues $\lambda_i + \lambda_j$ for eigenvalues $\lambda_i, \lambda_j$ of $A$, and these are nonzero.
Condition (2) with $Q = I$ gives (3).
For (3) implies (1), $V(x) = x^T P x$ is a [[Lyapunov function|01REYCJ371]] for $x' = Ax$: along solutions $V' = x^T (A^T P + PA) x < 0$ for $x \ne 0$, so every solution tends to $0$.

Example: for $A = \begin{pmatrix} -1 & 1 \\ 0 & -2 \end{pmatrix}$ and $Q = I$, write $P = \begin{pmatrix} p & q \\ q & r \end{pmatrix}$.
The equation $A^T P + PA = -I$ gives $-2p = -1$, $p - 3q = 0$ and $2q - 4r = -1$, so $p = 1/2$, $q = 1/6$, $r = 1/3$.
Then $p > 0$ and $pr - q^2 = 1/6 - 1/36 > 0$, so $P$ is positive definite, as the theorem predicts.

In (3), negative definite cannot be weakened to negative semidefinite.
For $A = 0$ and $P = I$, the matrix $A^T P + PA = 0$ is negative semidefinite, but $A$ is not Hurwitz.

## Explanations

### L1 human

The linear system $x' = Ax$ comes to rest exactly when it has a quadratic energy $x^T P x$ that strictly decreases along every motion.
The theorem says that such an energy can be found by solving a linear equation for $P$.
So a question about eigenvalues becomes a question about solving linear equations and checking positivity.

### L2 human

This is the linear case of Lyapunov's direct method, and the converse direction is exact: for linear systems a quadratic Lyapunov function always exists.
Condition (3) is a linear matrix inequality in $P$, which is the starting point of computational methods for stability and robust control.
The discrete-time analogue says that every eigenvalue of $A$ has absolute value less than $1$ if and only if $A^T P A - P = -Q$ has a positive definite solution for every positive definite $Q$.
