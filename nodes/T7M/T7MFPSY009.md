---
tag: T7MFPSY009
kind: statement
role: theorem
name: Extreme values of the Rayleigh quotient
aliases: [rayleigh-ritz-principle, rayleigh-quotient-bounds]
msc: ["15A18", "15A42"]
topics: [3YM9EK6VMB]
audience: ug1
about: [06WHP8SE98]
uses: [06WHP8SE98, 0MB8HQW495, 0ZND7NQ970, 0B5H4208Z9, 0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
  - url: https://understandinglinearalgebra.org/sec-quadratic-forms.html
    locator: Proposition 7.2.8
---

## Statement

Let $V$ be an inner product space of finite dimension $n \geq 1$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
Let $T \colon V \to V$ be [[self-adjoint|0MB8HQW495]], with [[eigenvalues|0ZND7NQ970]] $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$, repeated by multiplicity.
For $v \neq 0$, let $R(v) = \ip{Tv}{v} / \ip{v}{v}$ be the [[Rayleigh quotient|06WHP8SE98]].

1. $\lambda_n \leq R(v) \leq \lambda_1$ for every $v \neq 0$.
2. $R(v) = \lambda_1$ if and only if $v$ is an [[eigenvector|0B5H4208Z9]] for $\lambda_1$. Also $R(v) = \lambda_n$ if and only if $v$ is an eigenvector for $\lambda_n$.
3. So the maximum of $R$ is the largest eigenvalue, and the minimum of $R$ is the smallest eigenvalue.

For a [[Hermitian|0EKZCX4K3P]] $n \times n$ matrix $A$, the same holds for $R_A(x) = x^* A x / x^* x$ on $\mathbb{C}^n$.

## Remarks

### Why each hypothesis is needed

- Self-adjointness is needed. [[The matrix $\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$|39XSQ9MTZ3]] has the only eigenvalue $1$, but its Rayleigh quotient takes the values $3$ and $-1$.
- The vector must be nonzero, because $R(0)$ is $0 / 0$.

### Consequences

- The quadratic form $\ip{Tv}{v}$ on the unit sphere has the maximum $\lambda_1$ and the minimum $\lambda_n$. For real symmetric matrices, this is [[the extreme values of a quadratic form on unit vectors|YS4HT1EYE5]].
- $T$ is positive definite if and only if $\lambda_n > 0$.
- The operator norm of a self-adjoint $T$ is $\max(\abs{\lambda_1}, \abs{\lambda_n})$.
- The other eigenvalues are values of $R$ on subspaces. [[The Courant–Fischer min-max theorem|CJK2HS2508]] gives $\lambda_k$ as a max-min of $R$ over subspaces of dimension $k$.

### Converse

Part 2 is an equivalence.
Part 1 has a partial converse: every number in $[\lambda_n, \lambda_1]$ is a value of $R$, because $R$ is continuous on the connected set of nonzero vectors when $\dim V \geq 2$.
For $n = 1$, the only value is $\lambda_1$.

## Explanations

### L1 human

The Rayleigh quotient measures how much $T$ stretches a vector in its own direction.
For a self-adjoint operator, the largest stretch is the largest eigenvalue, and the smallest stretch is the smallest eigenvalue.
These extreme stretches happen exactly along the eigenvectors.

### L2 human

Worked example: [[the matrix $\begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$|3FXAQ6P15S]] with the eigenvalues $6$ and $1$.

1. $R(1, 0) = 5$, $R(0, 1) = 2$ and $R(1, 1) = \tfrac{11}{2}$. All lie between $1$ and $6$.
2. $R(2, 1) = 6$, and $(2, 1)$ is an eigenvector for $6$.
3. $R(1, -2) = 1$, and $(1, -2)$ is an eigenvector for $1$.

The typical use: a test vector $v$ gives the lower bound $R(v) \leq \lambda_1$ for the largest eigenvalue without any eigenvector computation.
A trap: the bounds need a self-adjoint operator, as the example with the value $-1$ shows.

### L3 human

The theorem is the first case of the min-max principle.
It holds for bounded self-adjoint operators on a Hilbert space, with the supremum and the infimum of the spectrum in place of $\lambda_1$ and $\lambda_n$.
The set of all values of $R$, for any operator, is the numerical range.
For normal operators it is the convex hull of the eigenvalues.
