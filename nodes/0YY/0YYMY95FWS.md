---
tag: 0YYMY95FWS
kind: definition
name: Matrix of a linear map
msc: [15A04]
defines: 0YQSGNYE3K
uses: [0RJF668P1T, 0VTQTPQGAV, 0BMVBHTWV2]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: lead section
---

## Definition

Let $F$ be a field, and let $V$ and $W$ be vector spaces over $F$ with [[bases|0KCQ9Y3QKA]] $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$.
Let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *matrix of $T$* in the bases $B$ and $C$ is the $m \times n$ matrix $[T]_{C,B} = (a_{ij})$ defined by
$$T(b_j) = \sum_{i=1}^{m} a_{ij} c_i \qquad (1 \le j \le n).$$
Equivalently, column $j$ of $[T]_{C,B}$ is the [[coordinate vector|04CYQHN6MC]] $[T(b_j)]_C$.

## Remarks

For each $v \in V$, $[T(v)]_C = [T]_{C,B} [v]_B$.
The map $T \mapsto [T]_{C,B}$ is a linear isomorphism $\Hom_F(V, W) \to M_{m \times n}(F)$.
For the rotation of $\R^2$ by an angle $\theta$, in the standard basis, the matrix is $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.
Mathlib writes this map as `LinearMap.toMatrix`.

## Explanations

### L1 human

To write a linear map as a matrix, apply the map to each basis vector.
Write the coordinates of each image as a column.
These columns, side by side, are the matrix.
