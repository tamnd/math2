---
tag: Y553MSYDAH
kind: statement
role: theorem
name: Schur–Horn theorem
msc: [15A42, 15B57]
uses: [5K7VT2VKZT, 0P17NGQQMQ, 0BQAA2BK3Q, JJA90EB2PS, 0AR68JTMDT]
about: [5K7VT2VKZT, 0P17NGQQMQ]
sources:
  - url: https://en.wikipedia.org/wiki/Schur%E2%80%93Horn_theorem
same_as:
  wikidata: Q7433042
  wikipedia: Schur–Horn theorem
---

## Statement

Let $n \ge 1$ and let $\lambda = (\lambda_1, \ldots, \lambda_n)$ and $d = (d_1, \ldots, d_n)$ be vectors in $\R^n$.
Then the following are equivalent.

1. There is an $n \times n$ [[Hermitian matrix|0P17NGQQMQ]] with [[eigenvalues|0BQAA2BK3Q]] $\lambda_1, \ldots, \lambda_n$, counted with multiplicity, and diagonal entries $d_1, \ldots, d_n$.
2. The vector $d$ is [[majorized|5K7VT2VKZT]] by $\lambda$, that is, $d \prec \lambda$.

## Remarks

Schur proved that the condition is necessary, and Horn proved that it is sufficient.
For necessity, write $A = U \Lambda U^*$ with $U$ [[unitary|0AR68JTMDT]] and $\Lambda$ diagonal; then $d_i = \sum_j \abs{u_{ij}}^2 \lambda_j$.
The matrix $(\abs{u_{ij}}^2)$ is [[doubly stochastic|JJA90EB2PS]], so $d \prec \lambda$ by the Hardy–Littlewood–Pólya characterisation of majorization.
The converse is proved by constructing the matrix, for example by induction on $n$.
Example: $\lambda = (2, 0)$ and $d = (1, 1)$ satisfy $d \prec \lambda$, and $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has eigenvalues $2, 0$ and diagonal $1, 1$.
The diagonal $(3, -1)$ is impossible for the eigenvalues $(2, 0)$, since $3 > 2$.
The same statement holds with real symmetric matrices in place of Hermitian matrices.

## Explanations

### L1 human

The diagonal entries of a Hermitian matrix are averages of its eigenvalues.
So they are less spread out than the eigenvalues, in the precise sense of majorization.
The theorem says that this is the only restriction: every diagonal that is less spread out than the eigenvalues actually occurs.

### L2 human

The case $k = 1$ of the majorization gives $\max_i d_i \le \max_j \lambda_j$, a special case of the Rayleigh quotient bound.
The theorem identifies the set of diagonals of the matrices $U \Lambda U^*$, $U$ unitary, with the permutohedron, the convex hull of the permutations of $\lambda$.
In this form it is a special case of Kostant's convexity theorem and of the convexity theorem of Atiyah and of Guillemin and Sternberg for moment maps.
In frame theory it is used to build frames with prescribed norms and frame operator.
