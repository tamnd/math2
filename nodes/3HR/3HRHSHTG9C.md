---
tag: 3HRHSHTG9C
kind: statement
role: theorem
name: Minimal residual method
msc: [65F10]
uses: [0VR671PHE5, 0EB9N0S33C, QB45PCGQPV, 7RRB4PCRJB, DARX1KZRHZ, 0BQAA2BK3Q, A3FR6PNEPB, AFXZGQB4EN, 2RPE77ACER]
about: [2RPE77ACER, QB45PCGQPV]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_residual_method
same_as:
  wikidata: Q1453478
  wikipedia: Minimal residual method
---

## Statement

Let $A$ be a real [[symmetric|0VR671PHE5]] [[invertible|0EB9N0S33C]] $n \times n$ matrix, possibly indefinite, let $b \in \R^n$, and let $x_0 \in \R^n$ with $r_0 = b - A x_0$.
For $k \ge 1$, the $k$-th iterate of the *minimal residual method* (MINRES) is the vector $x_k \in x_0 + \mathcal{K}_k(A, r_0)$ that minimizes $\norm{b - A x}_2$ there.
Here $\mathcal{K}_k$ is the [[Krylov subspace|QB45PCGQPV]].

1. The iterates can be computed by recurrences of fixed length. Each step costs one product with $A$ and a number of vector operations that does not depend on $k$.
2. Let $r_k = b - A x_k$, and let $P_k$ be the set of polynomials $p$ of degree at most $k$ with $p(0) = 1$. Then $$\norm{r_k}_2 = \min_{p \in P_k} \norm{p(A) r_0}_2 \le \min_{p \in P_k} \max_{\lambda} \abs{p(\lambda)} \, \norm{r_0}_2,$$ where $\lambda$ runs over the eigenvalues of $A$.
3. In exact arithmetic some $r_k$ with $k \le n$ is zero.

## Remarks

The [[Lanczos algorithm|7RRB4PCRJB]] gives an orthonormal basis $Q_{k+1}$ of $\mathcal{K}_{k+1}(A, r_0)$ with $A Q_k = Q_{k+1} \tilde{T}_k$, where $\tilde{T}_k$ is $(k+1) \times k$ and [[tridiagonal|DARX1KZRHZ]].
The minimization reduces to a small least squares problem with $\tilde{T}_k$.
A QR factorization of $\tilde{T}_k$ by Givens rotations can be updated with each new column, and this yields the short recurrences of clause 1.
Clause 2 uses that $A$ is orthogonally diagonalizable, so $\norm{p(A)}_2 = \max_\lambda \abs{p(\lambda)}$.
Example: if $A$ has only the [[eigenvalues|0BQAA2BK3Q]] $1$ and $-1$, then $p(t) = 1 - t^2$ gives $r_2 = 0$.
For a nonsymmetric $A$ the Lanczos recurrence no longer produces an orthonormal basis, and one needs [[GMRES|A3FR6PNEPB]] with its long recurrences.

## Explanations

### L1 human

MINRES solves symmetric systems that need not be positive definite, such as saddle point problems.
At each step it picks, among the vectors it can reach with the matrix, the one that makes the residual as small as possible.
Thanks to symmetry, it only needs to remember a few vectors.

### L2 human

MINRES is mathematically [[GMRES|A3FR6PNEPB]] specialized to symmetric matrices, where the Arnoldi process becomes the Lanczos process.
It fills the gap left by the [[conjugate gradient method|AFXZGQB4EN]], which can break down when $A$ is indefinite.
For symmetric positive definite $A$ both apply: conjugate gradients minimize the energy norm of the error, MINRES the Euclidean norm of the residual.
Like other Krylov [[iterative methods|2RPE77ACER]], it is used with a preconditioner, which must be symmetric positive definite to keep the symmetry.
The method is due to Paige and Saunders.
