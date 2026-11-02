---
tag: P1ECPTAG8F
kind: statement
role: proposition
name: LOBPCG
msc: [65F15, 65F08]
uses: [0VR671PHE5, 0KX66CZMBB, 06WHP8SE98, KE98SW3SBD, 0BQAA2BK3Q, G11NE3AT6E]
about: [HCJ2ETX89Z]
sources:
  - url: https://en.wikipedia.org/wiki/LOBPCG
same_as:
  wikidata: Q6459462
  wikipedia: LOBPCG
---

## Statement

Let $A, B \in \R^{n \times n}$ be [[symmetric|0VR671PHE5]] with $B$ [[positive definite|0KX66CZMBB]], and let $\lambda_1 \le \cdots \le \lambda_n$ be the [[eigenvalues|0BQAA2BK3Q]] of the pencil $A x = \lambda B x$.
Let $T \in \R^{n \times n}$ be symmetric positive definite (the [[preconditioner|KE98SW3SBD]]), and let $\rho(x) = x^T A x / x^T B x$ be the [[Rayleigh quotient|06WHP8SE98]] for $x \ne 0$.
Consider the single-vector *locally optimal block preconditioned conjugate gradient method* (LOBPCG).
It starts from $x_0 \ne 0$, and for $k \ge 0$ it sets
$$r_k = A x_k - \rho(x_k) B x_k, \qquad w_k = T r_k, \qquad S_k = \mathrm{span}\set{x_k, w_k, x_{k-1}}$$
with $x_{-1}$ omitted for $k = 0$.
The next iterate $x_{k+1}$ is a vector that minimizes $\rho$ over $S_k \setminus \set{0}$, computed by the Rayleigh–Ritz method on $S_k$.
Then for every $k$:

1. $\lambda_1 \le \rho(x_{k+1}) \le \rho(x_k)$;
2. $\rho(x_{k+1}) \le \min_{t \in \R} \rho(x_k + t w_k)$, so each step is at least as good as one step of preconditioned steepest descent with the optimal step length;
3. if $r_k = 0$, then $x_k$ is an eigenvector and $\rho(x_k)$ is an eigenvalue of the pencil.

## Remarks

Parts 1 and 2 hold because $x_k$ and every $x_k + t w_k$ lie in $S_k$, over which $x_{k+1}$ minimizes $\rho$; the lower bound $\lambda_1$ is the [[min-max theorem|G11NE3AT6E]] for the pencil.
The Rayleigh–Ritz step reduces to a generalized eigenvalue problem of size at most $3$, the projections of $A$ and $B$ onto $S_k$.
The original method uses a direction $p_k$, a combination of $w_{k-1}$ and $p_{k-1}$, in place of $x_{k-1}$; the span $S_k$ is the same, and $p_k$ gives a better conditioned basis.

The block version iterates a block of $m$ vectors and approximates the $m$ smallest eigenvalues, with Rayleigh–Ritz on a subspace of dimension at most $3m$.
Since LOBPCG improves on preconditioned steepest descent, the convergence bounds of preconditioned inverse iteration (Knyazev and Neymeyr) apply to it.
Example: with $T = I$, $B = I$ and $x_{-1}$ dropped, the method becomes steepest descent for the Rayleigh quotient, since $r_k$ is a multiple of the gradient of $\rho$ at $x_k$.

## Explanations

### L1 human

LOBPCG looks for the smallest eigenvalue of a large symmetric problem by minimizing the Rayleigh quotient.
At each step it searches for the best vector in a three-dimensional space built from the current guess, the preconditioned residual, and the previous guess.
Because the search space contains the steepest descent step, the method can never do worse than steepest descent, and in practice it behaves like a conjugate gradient method.

### L2 human

LOBPCG was introduced by Andrew Knyazev in 2001.
It needs only products with $A$, $B$ and $T$, so it suits large sparse problems such as discretized PDE eigenproblems.
There a good preconditioner, for example [[multigrid|AC9PY6FBYF]], makes the convergence nearly independent of the mesh size.
Compared with the [[Lanczos algorithm|7RRB4PCRJB]], it uses a preconditioner directly and keeps a fixed small memory, at the price of solving a small dense eigenproblem at each step.
