---
tag: 0YQSGNYE3K
kind: concept
name: Matrix of a linear map
aliases: [transformation-matrix]
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
uses: [0NRYHJPQG2, 0KCQ9Y3QKA, 04CYQHN6MC, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 2.2
  - book: isbn:9783031410253
    locator: Chapter 3
same_as:
  wikidata: Q1482183
  wikipedia: Transformation matrix
---

## Summary

The matrix of a [[linear map|0NRYHJPQG2]] $T \colon V \to W$ in ordered [[bases|0KCQ9Y3QKA]] $B$ of $V$ and $C$ of $W$ is a [[matrix|0VD9ZSWWJG]] with one column for each vector of $B$.
Column $j$ is the [[coordinate vector|04CYQHN6MC]] in $C$ of the image of the $j$-th vector of $B$.
With this matrix, $[T(v)]_C = [T]_{C,B}[v]_B$ for each $v \in V$.

## Motivation

A linear map is determined by the images of the vectors of a basis.
Each image is determined by its coordinates in a basis of the target.
So a finite table of numbers holds all the information about $T$.
With this table, questions about $T$ become questions about matrices, which a computer can answer by row reduction.

## Notation

The matrix is written $[T]_{C,B}$, $[T]_B^C$, $M(T)$ or $\mathcal{M}(T, B, C)$.
If $V = W$ and $B = C$, it is written $[T]_B$.
The order of the subscripts differs between books; here the basis of the target comes first, so that $[S]_{C,B}[T]_{B,A} = [S \circ T]_{C,A}$.
Mathlib writes `LinearMap.toMatrix v₁ v₂ f`, where `v₁` is the basis of the domain and indexes the columns.

## Remarks

### Examples

- [[The derivative $P_2 \to P_1$|KWN1RM45D5]]: in the bases $(1, x, x^2)$ and $(1, x)$ the matrix is $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$.
- [[A symmetric map of the plane|7HRGTM3RKJ]]: the map $(x, y) \mapsto (2x + y, x + 2y)$ has a diagonal matrix in the basis $((1, 1), (1, -1))$.
- The rotation of $\R^2$ by the angle $\theta$ has the matrix $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ in the standard basis.
- The identity map of $V$ has the identity matrix $I_n$ in the bases $B$ and $B$. In two different bases, its matrix is a [[change-of-basis matrix|0MKRHZB3WS]].
- For an $m \times n$ matrix $A$, the map $x \mapsto Ax$ has the matrix $A$ in the standard bases.

### Non-examples

- [[Images written as rows|RSET6QRFJR]]: the array with the images of the basis vectors as rows is the transpose of the matrix, and it gives wrong products.
- A map that is not linear has no matrix. The map $x \mapsto x + 1$ on $\R$ is not $x \mapsto ax$ for any $a$.

### Basic properties

- $[T(v)]_C = [T]_{C,B}[v]_B$ for each $v$, and $[T]_{C,B}$ is the only matrix with this property, by the [[coordinate formula|8B63KHW6D5]].
- The map $T \mapsto [T]_{C,B}$ is a linear isomorphism $\Hom(V, W) \to M_{m \times n}(F)$, by the [[theorem on linear maps and matrices|Q3EDKTZ6TA]]. Its inverse sends a matrix to its [[linear map|06HMCTAQH3]].
- $[S \circ T]_{C,A} = [S]_{C,B}[T]_{B,A}$, by the theorem on the [[matrix of a composition|05Q1B7MH0M]].
- The rank of $T$ is the [[rank|0ZC9YTXZRY]] of $[T]_{C,B}$, for every choice of bases.
- If the bases change, the matrix changes by the [[change-of-basis formula|0MQXVZEBMT]].

### History

Matrices first served to record the coefficients of systems of linear equations.
Cayley defined the product of matrices in 1858 so that it matches the composition of linear substitutions.

### Common errors

- Writing the images of the basis vectors as rows instead of columns.
- Taking the coordinates of $T(b_j)$ in the standard basis when the basis $C$ of the target is not standard.
- Forgetting that the matrix depends on the order of the basis vectors. A different order permutes the rows or the columns.
- Mixing the conventions $[T]_{C,B}$ and $[T]_{B,C}$ of different books.

## Explanations

### L1 human

To write a linear map as a matrix, apply the map to each basis vector.
Write the coordinates of each image as a column.
These columns, side by side, are the matrix.
Then multiplying the matrix by the coordinates of a vector gives the coordinates of its image.

### L2 human

The matrix depends on three choices: the map, the basis of the domain and the basis of the target.
One map has many matrices, one for each pair of bases.
A good choice of bases can make the matrix simple, for example diagonal.
The key formula $[T(v)]_C = [T]_{C,B}[v]_B$ turns the evaluation of $T$ into a matrix-vector product.
The common trap is to put the images in rows; this gives the transpose.

### L3 human

The coordinate maps $\phi_B \colon V \to F^n$ and $\phi_C \colon W \to F^m$ are isomorphisms, and $[T]_{C,B}$ is the matrix of $\phi_C \circ T \circ \phi_B^{-1} \colon F^n \to F^m$.
So the choice of bases gives an equivalence between the category of finite-dimensional vector spaces with chosen bases and the category of matrices.
In Mathlib, `LinearMap.toMatrix v₁ v₂` is a linear equivalence from linear maps to matrices, and entry $(i, j)$ is coordinate $i$ of the image of `v₁ j` in the basis `v₂`.
So Mathlib also puts the images of the domain basis in the columns.
