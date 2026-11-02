---
tag: 1SYY57DCWT
kind: statement
role: proposition
name: Derivation of the conjugate gradient method
msc: [65F10]
uses: [0KX66CZMBB, 0DTY8B9HMS, QB45PCGQPV, AFXZGQB4EN, 0VT6P0GNQR, CJ5EC820S7, 7RRB4PCRJB]
about: [AFXZGQB4EN]
sources:
  - url: https://en.wikipedia.org/wiki/Derivation_of_the_conjugate_gradient_method
same_as:
  wikidata: Q5262612
  wikipedia: Derivation of the conjugate gradient method
---

## Statement

Let $A$ be a real symmetric [[positive definite|0KX66CZMBB]] $n \times n$ matrix, let $b \in \R^n$, let $x^* = A^{-1} b$, and let $x_0 \in \R^n$.
Write $\norm{v}_A = \sqrt{v^T A v}$ and $r(x) = b - A x$.

1. (Conjugate directions) Let $p_0, \dots, p_{m-1}$ be nonzero vectors with $p_i^T A p_j = 0$ for $i \ne j$. Define $x_{k+1} = x_k + \alpha_k p_k$ with $\alpha_k = p_k^T r(x_k) / p_k^T A p_k$. Then for each $k \le m$, the residual $r(x_k)$ is orthogonal to $p_0, \dots, p_{k-1}$. Moreover $x_k$ minimizes $\norm{x - x^*}_A$ over $x_0 + \operatorname{span} \set{p_0, \dots, p_{k-1}}$. If $m = n$, then $x_n = x^*$.
2. (Short recurrence) Let $r_k = r(x_k)$, and suppose $r_0, \dots, r_k$ are nonzero. Let the directions arise by $A$-orthogonalizing the residuals. That is, $p_0 = r_0$, and $p_k$ is $r_k$ minus its $A$-orthogonal projection onto $\operatorname{span} \set{p_0, \dots, p_{k-1}}$. Then $\operatorname{span} \set{p_0, \dots, p_{k-1}} = \mathcal{K}_k(A, r_0)$, and $p_k = r_k + \beta_{k-1} p_{k-1}$ with $\beta_{k-1} = r_k^T r_k / r_{k-1}^T r_{k-1}$. Also $\alpha_k = r_k^T r_k / p_k^T A p_k$.

## Remarks

For clause 1, the function $f(x) = \frac12 \norm{x - x^*}_A^2$ restricted to $x_0 + \operatorname{span}\set{p_0, \dots, p_{k-1}}$ separates into one quadratic in each coordinate, by conjugacy.
The step $\alpha_k$ minimizes the quadratic in the $k$-th coordinate, and later steps do not change the earlier coordinates.
For clause 2, the residual $r_k$ is orthogonal to $\mathcal{K}_k(A, r_0)$ by clause 1.
Since $A p_j \in \mathcal{K}_{j+2}(A, r_0)$, the vector $r_k$ is $A$-orthogonal to $p_j$ for $j < k - 1$.
So only the last direction enters the [[Gram–Schmidt|0VT6P0GNQR]] step, and this gives the two-term recurrence.
Clause 2 with clause 1 is exactly the [[conjugate gradient method|AFXZGQB4EN]].
Example: with $p_i = e_i$ and $A$ diagonal, the directions are conjugate, and the method of clause 1 solves the $i$-th equation at step $i$.

## Explanations

### L1 human

If the search directions do not interfere with each other in the geometry defined by $A$, then minimizing along each direction once gives the minimum over all of them together.
Building such directions in general costs a lot of memory.
The miracle of conjugate gradients is that, when the directions come from the residuals, each new one only needs to be corrected against the previous one.

### L2 human

There is a second derivation from the [[Lanczos algorithm|7RRB4PCRJB]].
The [[Arnoldi iteration|CJ5EC820S7]] applied to a symmetric $A$ gives an orthonormal basis of $\mathcal{K}_k(A, r_0)$ in which $A$ becomes a tridiagonal matrix $T_k$.
The Galerkin condition $r_k \perp \mathcal{K}_k(A, r_0)$ asks to solve a system with $T_k$.
Updating an $L D L^T$ factorization of $T_k$ step by step gives the same recurrences.
This view explains the link between conjugate gradients and the Lanczos process for eigenvalues.
