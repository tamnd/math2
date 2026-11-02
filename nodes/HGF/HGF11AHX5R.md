---
tag: HGF11AHX5R
kind: statement
role: theorem
name: Biconjugate gradient method
msc: [65F10]
uses: [0EB9N0S33C, 09DXWYRD43, QB45PCGQPV, AFXZGQB4EN, 0KX66CZMBB, 2RPE77ACER]
about: [2RPE77ACER]
sources:
  - url: https://en.wikipedia.org/wiki/Biconjugate_gradient_method
same_as:
  wikidata: Q855169
  wikipedia: Biconjugate gradient method
---

## Statement

Let $A$ be a real [[invertible|0EB9N0S33C]] $n \times n$ matrix, let $b \in \R^n$, and let $x_0 \in \R^n$ with $r_0 = b - A x_0$.
Choose a *shadow residual* $\tilde{r}_0 \in \R^n$ with $\tilde{r}_0^T r_0 \ne 0$, and set $p_0 = r_0$ and $\tilde{p}_0 = \tilde{r}_0$.
The *biconjugate gradient method* (BiCG) computes, for $k = 0, 1, \dots$,
$$\alpha_k = \frac{\tilde{r}_k^T r_k}{\tilde{p}_k^T A p_k}, \quad x_{k+1} = x_k + \alpha_k p_k, \quad r_{k+1} = r_k - \alpha_k A p_k, \quad \tilde{r}_{k+1} = \tilde{r}_k - \alpha_k A^T \tilde{p}_k,$$
$$\beta_k = \frac{\tilde{r}_{k+1}^T r_{k+1}}{\tilde{r}_k^T r_k}, \quad p_{k+1} = r_{k+1} + \beta_k p_k, \quad \tilde{p}_{k+1} = \tilde{r}_{k+1} + \beta_k \tilde{p}_k,$$
where $A^T$ is the [[transpose|09DXWYRD43]].
Suppose that the denominators $\tilde{p}_k^T A p_k$ and $\tilde{r}_k^T r_k$ are nonzero up to step $m$.
Then in exact arithmetic, for $i, j \le m$:

1. $r_k = b - A x_k$, and $x_k \in x_0 + \mathcal{K}_k(A, r_0)$, where $\mathcal{K}_k$ is the [[Krylov subspace|QB45PCGQPV]];
2. (biorthogonality) $\tilde{r}_i^T r_j = 0$ for $i \ne j$;
3. (biconjugacy) $\tilde{p}_i^T A p_j = 0$ for $i \ne j$.

## Remarks

Clauses 2 and 3 say that $r_k$ is orthogonal to $\mathcal{K}_k(A^T, \tilde{r}_0)$, a Petrov–Galerkin condition.
Suppose no breakdown occurs up to step $n$.
Then $\tilde{r}_0, \dots, \tilde{r}_{n-1}$ are linearly independent, since $\tilde{r}_i^T r_j$ is zero for $i \ne j$ and nonzero for $i = j$.
So $r_n$ is orthogonal to all of $\R^n$, and $r_n = 0$.
Example: if $A$ is symmetric and $\tilde{r}_0 = r_0$, then $\tilde{r}_k = r_k$ and $\tilde{p}_k = p_k$ for all $k$.
Then BiCG is the [[conjugate gradient method|AFXZGQB4EN]], which never breaks down when $A$ is [[positive definite|0KX66CZMBB]].
For a general $A$ the method can break down when $\tilde{r}_k^T r_k = 0$ with $r_k \ne 0$, and its residual norms can oscillate wildly.

## Explanations

### L1 human

Conjugate gradients rely on symmetry to keep short recurrences.
BiCG regains short recurrences for a nonsymmetric matrix by running a second, shadow iteration with the transpose alongside the first.
Each new residual is made orthogonal to the earlier shadow residuals, instead of to its own earlier residuals as in conjugate gradients.
The price is two matrix-vector products per step, one with $A$ and one with $A^T$, and less robust convergence.

### L2 human

BiCG is the linear-system counterpart of the nonsymmetric Lanczos process.
Unlike GMRES it has no minimization property, but its memory and work per step do not grow with $k$.
Its weaknesses, breakdowns and erratic residuals, and the need for $A^T$, motivated the transpose-free variants CGS and BiCGSTAB and the smoother QMR method.
It is one of the Krylov [[iterative methods|2RPE77ACER]] for nonsymmetric systems.
