---
tag: 24YCKE2RPH
kind: statement
role: theorem
name: Conjugate residual method
msc: [65F10]
uses: [0KX66CZMBB, QB45PCGQPV, AFXZGQB4EN, 3HRHSHTG9C, 2RPE77ACER]
about: [2RPE77ACER]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_residual_method
same_as:
  wikidata: Q5161159
  wikipedia: Conjugate residual method
---

## Statement

Let $A$ be a real symmetric [[positive definite|0KX66CZMBB]] $n \times n$ matrix, let $b \in \R^n$, and let $x_0 \in \R^n$.
The *conjugate residual method* sets $r_0 = b - A x_0$ and $p_0 = r_0$, and for $k = 0, 1, \dots$ while $r_k \ne 0$ computes
$$\alpha_k = \frac{r_k^T A r_k}{(A p_k)^T (A p_k)}, \quad x_{k+1} = x_k + \alpha_k p_k, \quad r_{k+1} = r_k - \alpha_k A p_k,$$
$$\beta_k = \frac{r_{k+1}^T A r_{k+1}}{r_k^T A r_k}, \quad p_{k+1} = r_{k+1} + \beta_k p_k, \quad A p_{k+1} = A r_{k+1} + \beta_k A p_k.$$
In exact arithmetic the following hold.

1. $r_k = b - A x_k$, and $x_k$ minimizes $\norm{b - A x}_2$ over $x \in x_0 + \mathcal{K}_k(A, r_0)$, where $\mathcal{K}_k$ is the [[Krylov subspace|QB45PCGQPV]].
2. The residuals are $A$-conjugate, $r_i^T A r_j = 0$ for $i \ne j$, and the vectors $A p_i$ are mutually orthogonal.
3. Some $r_k$ with $k \le n$ is zero.

## Remarks

The method is the [[conjugate gradient method|AFXZGQB4EN]] with the inner product $\ip{u}{v} = u^T A v$ in place of $u^T v$.
Conjugate gradients in this inner product minimize $\norm{x - x^*}_{A^2}$, and $\norm{x - x^*}_{A^2} = \norm{A(x - x^*)}_2 = \norm{b - A x}_2$, which gives clause 1.
Clause 2 is the image of the orthogonality and conjugacy relations of conjugate gradients under the change of inner product.
The update of $A p_{k+1}$ saves a product with $A$, so each step needs one product, $A r_{k+1}$.
Example: if $r_0$ is an eigenvector of $A$ for $\lambda$, then $\alpha_0 = \lambda r_0^T r_0 / \lambda^2 r_0^T r_0 = 1 / \lambda$ and $r_1 = 0$.
For a symmetric indefinite $A$ the same formulas can be run, but $r_k^T A r_k$ can vanish and the method then breaks down.
The [[MINRES|3HRHSHTG9C]] method avoids this breakdown.

## Explanations

### L1 human

The conjugate residual method looks like conjugate gradients, but it chooses each step to make the residual, rather than the energy error, as small as possible.
So the size of the residual never grows from one step to the next.
It costs about the same as conjugate gradients, with one extra stored vector.

### L2 human

For symmetric positive definite systems, conjugate residuals and conjugate gradients minimize different norms over the same Krylov spaces.
In practice the residual norm of conjugate residuals is monotone, which is convenient for stopping tests.
For indefinite symmetric systems [[MINRES|3HRHSHTG9C]] is the robust choice, and for nonsymmetric systems the generalizations GCR and GMRES apply.
Like all Krylov [[iterative methods|2RPE77ACER]], it is normally combined with a preconditioner.
