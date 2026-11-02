---
tag: AFXZGQB4EN
kind: statement
role: theorem
name: Conjugate gradient method
msc: [65F10, 65F08]
uses: [0GT4WWGWH2, 0KX66CZMBB, QB45PCGQPV, AB3S6MHJ8X, 2RPE77ACER, KE98SW3SBD, QYYCFQ8E5D, PE5H892XVS]
about: [2RPE77ACER, QB45PCGQPV]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_gradient_method
same_as:
  wikidata: Q1191895
  wikipedia: Conjugate gradient method
---

## Statement

Let $A$ be a real symmetric [[positive definite|0KX66CZMBB]] $n \times n$ matrix, let $b \in \R^n$, and let $x^* = A^{-1} b$.
For $v \in \R^n$ write $\norm{v}_A = \sqrt{v^T A v}$.
The *conjugate gradient method* starts from $x_0 \in \R^n$ with $r_0 = b - A x_0$ and $p_0 = r_0$, and for $k = 0, 1, \dots$ while $r_k \ne 0$ sets
$$\alpha_k = \frac{r_k^T r_k}{p_k^T A p_k}, \quad x_{k+1} = x_k + \alpha_k p_k, \quad r_{k+1} = r_k - \alpha_k A p_k,$$
$$\beta_k = \frac{r_{k+1}^T r_{k+1}}{r_k^T r_k}, \quad p_{k+1} = r_{k+1} + \beta_k p_k.$$
In exact arithmetic the following hold.

1. $r_k = b - A x_k$, and $x_k$ is the unique minimizer of $\norm{x - x^*}_A$ over $x \in x_0 + \mathcal{K}_k(A, r_0)$, where $\mathcal{K}_k$ is the [[Krylov subspace|QB45PCGQPV]].
2. The residuals are mutually orthogonal, $r_i^T r_j = 0$ for $i \ne j$, and the directions are $A$-conjugate, $p_i^T A p_j = 0$ for $i \ne j$.
3. Some $r_k$ with $k \le n$ is zero, so the method finds $x^*$ in at most $n$ steps.
4. With $\kappa = \lambda_{\max} / \lambda_{\min}$ the ratio of the extreme eigenvalues of $A$, for every $k$, $$\norm{x_k - x^*}_A \le 2 \left( \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1} \right)^k \norm{x_0 - x^*}_A.$$

## Remarks

Clause 1 implies $x_k - x^* = q(A)(x_0 - x^*)$ for the polynomial $q$ of degree at most $k$ with $q(0) = 1$ that minimizes the $A$-norm.
So $\norm{x_k - x^*}_A \le \max_\lambda \abs{q(\lambda)} \norm{x_0 - x^*}_A$ for every such $q$, with $\lambda$ over the eigenvalues of $A$.
Choosing the scaled Chebyshev polynomial of [[Chebyshev iteration|PE5H892XVS]] gives clause 4.
Choosing $q$ that vanishes at all eigenvalues shows more: if $A$ has only $m$ distinct eigenvalues, the method stops after at most $m$ steps.
Example: for $A$ with rows $(2, 1)$ and $(1, 2)$ and $b = (3, 3)$, start at $x_0 = 0$.
Then $r_0 = (3, 3)$ is an eigenvector of $A$ for the eigenvalue $3$, so $\alpha_0 = 1/3$ and $x_1 = (1, 1) = x^*$ after one step.
Without symmetry or positive definiteness the coefficients can break down, and the minimization property is lost.

## Explanations

### L1 human

Solving $A x = b$ for a symmetric positive definite $A$ is the same as finding the bottom of the bowl $f(x) = \frac12 x^T A x - b^T x$.
Plain steepest descent zigzags down a narrow valley.
The conjugate gradient method picks each new direction so that it never spoils the progress made along the old ones.
Each step needs one matrix-vector product and a few vector operations, and memory for only four vectors.

### L2 human

Conjugate gradients is the standard [[iterative method|2RPE77ACER]] for large sparse symmetric positive definite systems, such as those from discretized elliptic equations.
In floating point the finite termination of clause 3 is lost, and the method is used as an iterative method with the rate of clause 4.
The rate depends on $\sqrt{\kappa}$, where $\kappa$ is the [[condition number|AB3S6MHJ8X]], so one usually applies it to a preconditioned system.
With a symmetric positive definite [[preconditioner|KE98SW3SBD]] $P$, such as an [[incomplete Cholesky factorization|QYYCFQ8E5D]], the same bounds hold with $P^{-1} A$ in place of $A$.
The method is due to Hestenes and Stiefel.
