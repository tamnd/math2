---
tag: 0YYMY95FWS
kind: definition
name: Matrix of a linear map
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
defines: 0YQSGNYE3K
uses: [0RJF668P1T, 0VTQTPQGAV, 0BMVBHTWV2]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.toMatrix
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: lead section
---

## Definition

The matrix of a linear map records, column by column, the coordinates of the images of the basis vectors of the domain.
Let $F$ be a field, and let $V$ and $W$ be finite-dimensional vector spaces over $F$ with ordered [[bases|0VTQTPQGAV]] $B = (b_1, \dots, b_n)$ of $V$ and $C = (c_1, \dots, c_m)$ of $W$.
Let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
The *matrix of $T$ in the bases $B$ and $C$* is the $m \times n$ matrix $[T]_{C,B} = (a_{ij})$ over $F$ defined by
$$T(b_j) = \sum_{i=1}^{m} a_{ij} c_i \qquad (1 \le j \le n).$$
Equivalently, column $j$ of $[T]_{C,B}$ is the [[coordinate vector|0BMVBHTWV2]] $[T(b_j)]_C$.
When $V = W$ and $B = C$, we write $[T]_B$ for $[T]_{B,B}$.

## Remarks

Each condition in the definition has a job.
The bases must be finite, so that the matrix has finitely many rows and columns.
They must be ordered, because the order of $B$ fixes the order of the columns and the order of $C$ fixes the order of the rows.
The entries $a_{ij}$ exist and are unique because $C$ is a basis, so each $T(b_j)$ has exactly one expansion in $C$.
The map $T$ must be linear, since only then do the values $T(b_j)$ determine $T$ on all of $V$.

For a small example, take the rotation of $\mathbb{R}^2$ by the angle $\theta$, with the standard basis on both sides.
It sends $e_1$ to $(\cos\theta, \sin\theta)$ and $e_2$ to $(-\sin\theta, \cos\theta)$, so
$$[R_\theta] = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
The definition fails for the map $x \mapsto x + 1$ on $\mathbb{R}$, because it is not linear: with $B = C = (1)$ the recipe gives the $1 \times 1$ array $(2)$, but the map sends $2$ to $3$, not to $4$.

The matrix computes the map, $[T(v)]_C = [T]_{C,B}[v]_B$ for each $v \in V$, by the [[coordinate theorem|8B63KHW6D5]].
The assignment $T \mapsto [T]_{C,B}$ is a linear isomorphism $\Hom_F(V, W) \to M_{m \times n}(F)$, by the [[theorem on linear maps and matrices|Q3EDKTZ6TA]].
Mathlib writes this map as `LinearMap.toMatrix`, and the basis of the domain indexes the columns, as here.
The [[concept page|0YQSGNYE3K]] has worked examples and the traps.

## Explanations

### L1 human

To write a linear map as a matrix, apply the map to each basis vector.
Write the coordinates of each image as a column.
These columns, side by side and in the order of the basis, are the matrix.
For the map $(x, y) \mapsto (x + 2y, 3y)$ the images of $(1, 0)$ and $(0, 1)$ are $(1, 0)$ and $(2, 3)$, so the matrix has the columns $(1, 0)$ and $(2, 3)$.
