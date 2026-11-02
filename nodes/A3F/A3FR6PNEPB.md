---
tag: A3FR6PNEPB
kind: statement
role: theorem
name: Generalized minimal residual method
msc: [65F10]
uses: [0EB9N0S33C, QB45PCGQPV, CJ5EC820S7, 0BYTQ4X1HC, AB3S6MHJ8X, 0BQAA2BK3Q, AFXZGQB4EN, KE98SW3SBD, 2RPE77ACER]
about: [2RPE77ACER, QB45PCGQPV]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_minimal_residual_method
same_as:
  wikidata: Q1432976
  wikipedia: Generalized minimal residual method
---

## Statement

Let $A$ be an [[invertible|0EB9N0S33C]] complex $n \times n$ matrix, let $b \in \C^n$, let $x_0 \in \C^n$, and let $r_0 = b - A x_0 \ne 0$.
For $k \ge 1$, the $k$-th iterate of the *generalized minimal residual method* (GMRES) is the vector $x_k \in x_0 + \mathcal{K}_k(A, r_0)$ that minimizes $\norm{b - A x}_2$ there.
Here $\mathcal{K}_k$ is the [[Krylov subspace|QB45PCGQPV]].

1. $x_k$ exists and is unique, and $\norm{r_k}_2 \le \norm{r_{k-1}}_2$, where $r_k = b - A x_k$.
2. Run $k$ steps of the [[Arnoldi iteration|CJ5EC820S7]] from $r_0$, giving $Q_{k+1}$ and $\tilde{H}_k$, and let $\beta = \norm{r_0}_2$. Then $x_k = x_0 + Q_k y_k$, where $y_k$ minimizes $\norm{\beta e_1 - \tilde{H}_k y}_2$ over $y \in \C^k$.
3. Some $r_k$ with $k \le n$ is zero, so GMRES finds $A^{-1} b$ in at most $n$ steps in exact arithmetic.
4. Let $P_k$ be the set of polynomials $p$ of degree at most $k$ with $p(0) = 1$. If $A = V \Lambda V^{-1}$ with $\Lambda$ diagonal, then $$\frac{\norm{r_k}_2}{\norm{r_0}_2} \le \kappa_2(V) \min_{p \in P_k} \max_{\lambda} \abs{p(\lambda)},$$ where $\lambda$ runs over the eigenvalues of $A$.

## Remarks

Every $x \in x_0 + \mathcal{K}_k(A, r_0)$ has residual $p(A) r_0$ for a polynomial $p$ of degree at most $k$ with $p(0) = 1$, which gives clause 4.
Clause 1 holds because the search spaces grow, and clause 2 follows from $A Q_k = Q_{k+1} \tilde{H}_k$ and the orthonormality of the columns of $Q_{k+1}$.
For clause 3, if $\mathcal{K}_k(A, r_0)$ becomes invariant under $A$, then it contains $A^{-1} r_0$ and the residual vanishes.
Clause 2 turns the large minimization into a small [[least squares|0BYTQ4X1HC]] problem with a Hessenberg matrix, solved by Givens rotations.
Example: if $A = I + N$ with $N^2 = 0$, then $p(t) = (1 - t)^2$ vanishes on $A$, so $r_2 = 0$ for any $b$.
The constant $\kappa_2(V)$ is the [[condition number|AB3S6MHJ8X]] of the eigenvector matrix; for normal $A$ it equals $1$.
For highly non-normal $A$, the eigenvalues alone do not decide the convergence.

## Explanations

### L1 human

GMRES looks at all vectors it can build from the starting residual by repeated multiplication with $A$.
Among them it picks the one whose residual is as small as possible.
The residual can never grow, and with exact arithmetic the method reaches the solution after at most $n$ steps.
It works for any invertible matrix, symmetric or not.

### L2 human

GMRES is the residual-minimizing [[iterative method|2RPE77ACER]] for general nonsymmetric systems, while the [[conjugate gradient method|AFXZGQB4EN]] minimizes the energy norm for symmetric positive definite ones.
Since Arnoldi needs all basis vectors, the cost per step grows; restarted GMRES($m$) throws them away every $m$ steps, and it may then stagnate.
It is almost always used with a [[preconditioner|KE98SW3SBD]], often an incomplete LU factorization.
The method is due to Saad and Schultz.
