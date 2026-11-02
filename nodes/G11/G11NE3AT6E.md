---
tag: G11NE3AT6E
kind: statement
role: theorem
name: Min-max theorem
msc: [49R05, 47A75, 35P15]
uses: [0NEGN5CRSC, HM2HHE3J51, 06WHP8SE98, 0BQAA2BK3Q, 00YC1D652K, 4VD8XXQ4P3]
about: [0BQAA2BK3Q, 0NEGN5CRSC]
sources:
  - url: https://en.wikipedia.org/wiki/Min-max_theorem
    locator: Self-adjoint operators
---

## Statement

Let $H$ be an infinite-dimensional real or complex [[Hilbert space|HM2HHE3J51]].
Let $A$ be a [[self-adjoint operator|0NEGN5CRSC]] in $H$ that is bounded below and has compact resolvent.
Let $\lambda_1 \le \lambda_2 \le \lambda_3 \le \cdots$ be its [[eigenvalues|0BQAA2BK3Q]], listed with multiplicity.
Let $Q$ be the closed quadratic form of $A$, with form domain $D(Q)$, so that $Q(u) = \ip{Au}{u}$ for $u$ in the domain of $A$.
For $u \in D(Q)$ with $u \ne 0$, let $R(u) = Q(u) / \norm{u}^2$ be the [[Rayleigh quotient|06WHP8SE98]].
Then, for every $k \ge 1$,
$$\lambda_k = \min_{\substack{V \subseteq D(Q) \\ \dim V = k}} \; \max_{u \in V \setminus \set{0}} R(u) = \max_{\substack{W \subseteq H \\ \dim W \le k - 1}} \; \inf_{\substack{u \in D(Q) \setminus \set{0} \\ u \perp W}} R(u),$$
where $V$ and $W$ run over [[linear subspaces|00YC1D652K]] of the given dimensions.

## Remarks

Proof idea: let $(e_j)$ be an orthonormal basis of eigenvectors with $A e_j = \lambda_j e_j$.
On the span of $e_1, \dots, e_k$ the quotient $R$ is at most $\lambda_k$.
Every $k$-dimensional subspace $V$ contains a nonzero vector orthogonal to $e_1, \dots, e_{k-1}$, and there $R \ge \lambda_k$ by expanding in the basis.
The max-min form is proved in the same way, with the orthogonal complement of $W$.

Example: for a bounded open set $\Omega \subseteq \R^n$ and $A = -\Delta$ with Dirichlet condition, $D(Q) = H^1_0(\Omega)$ and $R(u) = \int_\Omega \abs{\nabla u}^2 / \int_\Omega u^2$.
So the [[Dirichlet eigenvalues|4VD8XXQ4P3]] are $\lambda_k(\Omega) = \min_{\dim V = k} \max_{u \in V \setminus \set{0}} R(u)$.
Since $H^1_0(\Omega_1) \subseteq H^1_0(\Omega_2)$ when $\Omega_1 \subseteq \Omega_2$, this gives domain monotonicity: $\lambda_k(\Omega_2) \le \lambda_k(\Omega_1)$.

The compact resolvent is used to have a basis of eigenvectors.
Without it the formulas still hold for the eigenvalues below the bottom of the essential spectrum, and otherwise the min-max values equal the bottom of the essential spectrum.
In finite dimension the result is the [[Courant–Fischer min-max theorem|CJK2HS2508]] for Hermitian matrices.

## Explanations

### L1 human

The eigenvalues of a symmetric operator can be found by optimisation alone.
The lowest one is the smallest value of the energy ratio $R$.
The $k$-th one is the smallest value one can reach for the worst vector of a $k$-dimensional family of trial functions.

### L2 human

The theorem turns questions on eigenvalues into questions on trial functions.
Any $k$-dimensional subspace of trial functions gives the upper bound $\lambda_k \le \max_V R$, which is the basis of the Rayleigh–Ritz and finite element approximations of eigenvalues.
It gives domain monotonicity of Dirichlet eigenvalues, the comparison of Dirichlet and Neumann eigenvalues, and, with Weyl's counting argument, the asymptotic law of eigenvalues.
For the Laplacian, the first eigenvalue is the minimum of the Rayleigh quotient, which is the starting point of the [[Faber–Krahn inequality|E7TY2TPXX7]].
