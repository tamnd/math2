---
tag: 7RRB4PCRJB
kind: statement
role: theorem
name: Lanczos algorithm
msc: [65F15, 65F10]
uses: [0VR671PHE5, QB45PCGQPV, DARX1KZRHZ, 0S9GGTR0EX, 0BQAA2BK3Q]
about: [HCJ2ETX89Z, QB45PCGQPV]
sources:
  - url: https://en.wikipedia.org/wiki/Lanczos_algorithm
same_as:
  wikidata: Q366640
  wikipedia: Lanczos algorithm
---

## Statement

Let $A \in \R^{n \times n}$ be [[symmetric|0VR671PHE5]], and let $q_1 \in \R^n$ be a unit vector.
The *Lanczos algorithm* sets $q_0 = 0$, $\beta_0 = 0$, and for $j = 1, 2, \dots$ computes
$$w_j = A q_j - \beta_{j-1} q_{j-1}, \quad \alpha_j = q_j^T w_j, \quad w_j' = w_j - \alpha_j q_j, \quad \beta_j = \norm{w_j'}, \quad q_{j+1} = w_j' / \beta_j,$$
stopping when $\beta_j = 0$.
Suppose that in exact arithmetic $\beta_1, \dots, \beta_{m-1}$ are nonzero, and let $Q_m = (q_1 \mid \cdots \mid q_m)$.
Then:

1. the columns of $Q_m$ form an [[orthonormal basis|0S9GGTR0EX]] of the [[Krylov subspace|QB45PCGQPV]] $\mathcal{K}_m(A, q_1) = \mathrm{span}\set{q_1, A q_1, \dots, A^{m-1} q_1}$;
2. $Q_m^T A Q_m = T_m$, the symmetric [[tridiagonal|DARX1KZRHZ]] matrix with diagonal $\alpha_1, \dots, \alpha_m$ and off-diagonal $\beta_1, \dots, \beta_{m-1}$;
3. $A Q_m = Q_m T_m + \beta_m q_{m+1} e_m^T$, where $e_m$ is the last standard basis vector of $\R^m$.

If $\beta_m = 0$, then $\mathcal{K}_m(A, q_1)$ is invariant under $A$ and every eigenvalue of $T_m$ is an [[eigenvalue|0BQAA2BK3Q]] of $A$.

## Remarks

The proof is by induction on $j$.
The vector $A q_j$ is orthogonal to $q_1, \dots, q_{j-2}$ because $q_i^T A q_j = (A q_i)^T q_j$ and $A q_i \in \mathcal{K}_{i+1}$, which is orthogonal to $q_j$ for $i + 1 < j$.
So only the two most recent vectors must be subtracted, and the short recurrence suffices; this is the [[Arnoldi iteration|CJ5EC820S7]] specialized to symmetric matrices.

The eigenvalues of $T_m$, called Ritz values, approximate eigenvalues of $A$, and the extreme ones converge first, often long before $m$ reaches $n$.
Example: for $A = \mathrm{diag}(1, 2, 3)$ and $q_1 = (1, 1, 1)/\sqrt{3}$, one gets $\alpha_1 = 2$ and $w_1' = (-1, 0, 1)/\sqrt{3}$, so $\beta_1 = \sqrt{2/3}$ and the Ritz values of $T_2$ are $2 \pm \sqrt{2/3}$, approaching $1$ and $3$.
In floating point arithmetic the vectors $q_j$ lose orthogonality once a Ritz value converges, and copies of converged eigenvalues appear.
Paige's analysis explains this, and practical codes use selective or full reorthogonalization.

## Explanations

### L1 human

The Lanczos algorithm squeezes a huge symmetric matrix into a small tridiagonal one by looking at it only through repeated multiplications with a starting vector.
The eigenvalues of the small matrix approximate the largest and smallest eigenvalues of the big one.
It needs only matrix-vector products, so it works for matrices too large to store as a full array.

### L2 human

The algorithm builds an orthonormal basis of a Krylov subspace with a three-term recurrence, which is cheap in memory and time.
Applied to linear systems with a symmetric positive definite matrix, the same recurrence underlies the [[conjugate gradient method|AFXZGQB4EN]].
Its convergence for extreme eigenvalues is described by the Kaniel–Paige theory using Chebyshev polynomials, and the gap between eigenvalues controls the speed.
For nonsymmetric matrices one uses the Arnoldi iteration or a two-sided Lanczos process.
