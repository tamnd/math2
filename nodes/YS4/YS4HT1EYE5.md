---
tag: YS4HT1EYE5
kind: statement
role: theorem
name: Extreme values of a quadratic form on unit vectors
aliases: [constrained-optimization-of-quadratic-forms]
msc: [15A18, 15A63]
topics: [6TSCEW8QMK]
audience: ug1
about: [0RBQS1JJCR, 0VR671PHE5]
uses: [0RBQS1JJCR, 0VR671PHE5, 0BQAA2BK3Q, T7MFPSY009]
proofs: [~c12802a2]
sources:
  - locator: src/section7-2.xml:839
    url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-2.xml#L839
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
  - book: isbn:9780321982384
---

## Statement

Let $A$ be a real [[symmetric matrix|0VR671PHE5]] of size $m \times m$.
Let $q_A(\mathbf u) = \mathbf u^T A \mathbf u$ be its [[quadratic form|0RBQS1JJCR]].
List the [[eigenvalues|0BQAA2BK3Q]] of $A$ in decreasing order, $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_m$.
Choose a basis $\mathbf u_1, \dots, \mathbf u_m$ of $\R^m$ with $A \mathbf u_i = \lambda_i \mathbf u_i$.

1. Over all unit vectors $\mathbf u$, the largest value of $q_A(\mathbf u)$ is $\lambda_1$. It is reached at the unit vector in the direction of $\mathbf u_1$.
2. Over all unit vectors $\mathbf u$, the smallest value of $q_A(\mathbf u)$ is $\lambda_m$. It is reached at the unit vector in the direction of $\mathbf u_m$.
3. A unit vector $\mathbf u$ has $q_A(\mathbf u) = \lambda_1$ if and only if $A \mathbf u = \lambda_1 \mathbf u$, and $q_A(\mathbf u) = \lambda_m$ if and only if $A \mathbf u = \lambda_m \mathbf u$.

This is the case of real symmetric matrices of [[the extreme values of the Rayleigh quotient|T7MFPSY009]].

## Remarks

### Why each hypothesis is needed

- $A$ symmetric: if $A$ is not symmetric, replace it by $\frac12 (A + A^T)$, which has the same form. The eigenvalues of $A$ itself do not give the extremes: $\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$ has only the eigenvalue $1$, but its form takes the value $3$ at $(1, 1)/\sqrt 2$.
- Unit vectors: without a bound on the length, $q_A(t \mathbf u) = t^2 q_A(\mathbf u)$ has no maximum when $\lambda_1 > 0$.
- Real entries: for complex vectors, use $\bar{\mathbf u}^T A \mathbf u$ with $A$ Hermitian, as in [[the Rayleigh quotient statement|T7MFPSY009]].

### Consequences

- For every $\mathbf x \in \R^m$, $\lambda_m \norm{\mathbf x}^2 \le \mathbf x^T A \mathbf x \le \lambda_1 \norm{\mathbf x}^2$.
- $q_A$ is [[positive definite|0RP20HFYM3]] if and only if $\lambda_m > 0$.
- For $q = 5x^2 + 4xy + 2y^2$, the extremes on the unit circle are $6$ at $\pm(2, 1)/\sqrt 5$ and $1$ at $\pm(-1, 2)/\sqrt 5$. The [[ellipse example|~aeb4d8e6]] and [[the Rayleigh quotient example|3FXAQ6P15S]] use the same matrix.

### Converse

Part 3 is an equivalence.
Every number in $[\lambda_m, \lambda_1]$ is a value of $q_A$ on unit vectors when $m \ge 2$, since the unit sphere is connected and $q_A$ is continuous.

### Generalizations

- The other eigenvalues are also extremes: $\lambda_2$ is the maximum of $q_A$ on unit vectors orthogonal to $\mathbf u_1$. [[The Courant-Fischer theorem|CJK2HS2508]] gives each $\lambda_k$ as a max-min over subspaces.
- With a positive definite matrix $M$ in place of the identity, the extremes of $\mathbf x^T A \mathbf x$ on $\mathbf x^T M \mathbf x = 1$ are the extreme roots of $\det(A - \lambda M) = 0$.
- With the method of [[Lagrange multipliers|0VKKP8X6Q6]], the critical points of $q_A$ on the sphere are exactly the unit eigenvectors.

## History

No source in our list gives a date or a name for this form of the result.

## Explanations

### L1 human

On the unit circle or the unit sphere, a quadratic form has a largest and a smallest value.
These values are the largest and the smallest eigenvalues of its matrix.
They are reached in the directions of the matching eigenvectors, which are the principal axes.

### L2 human

To find the maximum of $q_A$ on unit vectors, do not use calculus: find the eigenvalues of $A$ and take the largest.
A trap: the matrix must be symmetric, so the coefficient of $x_i x_j$ is split in half between the places $(i, j)$ and $(j, i)$.
Another trap: the maximum is reached at a unit eigenvector, so normalize the eigenvector before you give the point.

### L3 human

In the coordinates of [[the principal axis theorem|0PR5P9Z4KM]], $q_A = \sum_i \lambda_i y_i^2$ with $\sum_i y_i^2 = 1$.
So $q_A$ is a weighted average of the eigenvalues, with weights $y_i^2$.
This view gives the result at once, and it is the base of principal component analysis, where $A$ is a covariance matrix.
