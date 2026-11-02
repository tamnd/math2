---
tag: V9R8K4JCVM
kind: definition
name: Numerical methods for linear least squares
msc: [65F20, 62J05]
defines: AWQA2Y30N4
uses: [0BYTQ4X1HC, 0YY8VX28JR, 0ERWG4NXQ9, 0WKG8CYY6A]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_methods_for_linear_least_squares
---

## Definition

Let $A \in \R^{m \times n}$ and $b \in \R^m$.
The *linear least squares problem* is to find $x \in \R^n$ that minimizes $\norm{Ax - b}_2$.
When $A$ has rank less than $n$, one asks for the minimizer of smallest norm.
This is $x = A^\dagger b$, with $A^\dagger$ the [[Moore–Penrose inverse|0YY8VX28JR]].
A *numerical method for linear least squares* is an algorithm that computes this minimizer from $A$ and $b$.
It is exact in exact arithmetic, and accurate up to rounding errors in floating point arithmetic.
The standard methods are:

1. the normal equations $A^T A x = A^T b$, solved by a [[Cholesky decomposition|0WKG8CYY6A]] of $A^T A$ when $A$ has full column rank;
2. a [[QR decomposition|0ERWG4NXQ9]] $A = QR$ with $Q \in \R^{m \times n}$ having orthonormal columns and $R$ upper triangular, when $A$ has full column rank, followed by the solution of $R x = Q^T b$;
3. the singular value decomposition $A = U \Sigma V^T$, followed by $x = V \Sigma^\dagger U^T b$.

## Remarks

Example: for fitting a line $y = c_0 + c_1 t$ to the points $(0, 0)$, $(1, 1)$, $(2, 1)$, take $A$ with rows $(1, 0)$, $(1, 1)$, $(1, 2)$ and $b = (0, 1, 1)$.
Then $A^T A = \begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix}$ and $A^T b = (2, 3)$, so $c_0 = 1/6$ and $c_1 = 1/2$; the residual $(-1/6, 1/3, -1/6)$ is orthogonal to both columns of $A$, as it must be.
Non-example: solving the square system formed by the first $n$ rows of $Ax = b$ fits those rows exactly, but it does not give the minimizer in general.
Here it gives $c_0 = 0$, $c_1 = 1$, with residual norm $1$ instead of $1/\sqrt{6}$.
The normal equations are the cheapest method but square the condition number, $\kappa(A^T A) = \kappa(A)^2$.
Householder QR is backward stable and is the standard choice for dense full-rank problems; the SVD is the most robust for rank-deficient problems, at a higher cost.
For large sparse problems one uses iterative methods such as LSQR or the conjugate gradient method applied to the normal equations.

## Explanations

### L1 human

All these methods compute the same answer in exact arithmetic: the best fit in the sense of squared errors.
They differ in speed and in how many digits they lose to rounding.
