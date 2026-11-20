---
tag: 06HMCTAQH3
kind: concept
name: Linear map of a matrix
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
uses: [0VD9ZSWWJG, 0KCQ9Y3QKA, 0NRYHJPQG2, 0YQSGNYE3K]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Matrices
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Summary

The linear map of an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ in ordered [[bases|0KCQ9Y3QKA]] $B$ of $V$ and $C$ of $W$ is the [[linear map|0NRYHJPQG2]] $T_A \colon V \to W$ whose matrix in these bases is $A$.
It sends the $j$-th vector of $B$ to the vector of $W$ with coordinates given by column $j$ of $A$.
This construction inverts the [[matrix of a linear map|0YQSGNYE3K]].

## Motivation

Matrices are easy to store and to compute with, and linear maps carry the meaning.
The dictionary between the two must work in both directions.
The linear map of a matrix is the direction from matrices to maps.
For $V = F^n$ and $W = F^m$ with the standard bases, it is the familiar map $x \mapsto Ax$.

## Notation

The map is written $T_A$, $L_A$ or $x \mapsto Ax$ when the spaces are $F^n$ and $F^m$.
Mathlib writes `Matrix.toLin v₁ v₂ A`, where `v₁` is the basis of the domain and `v₂` the basis of the target.
For the standard bases of `n → R` and `m → R`, Mathlib also has `Matrix.toLin'` and `Matrix.mulVecLin`.

## Remarks

### Examples

- [[One matrix in two bases|V8J40J1DKG]]: the matrix $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ gives a shear in the standard basis and the map $(x, y) \mapsto (-x + 2y, -2x + 3y)$ in the basis $((1, 1), (0, 1))$.
- [[The maps of the matrix units|XQB25QZHAH]]: they form a basis of $\Hom(\R^3, \R^2)$.
- In the standard bases, the map of $\begin{pmatrix} 1 & 0 & -1 \end{pmatrix}$ is the linear form $(x, y, z) \mapsto x - z$ on $\R^3$.
- The map of the identity matrix $I_n$ in bases $B$ and $B$ is the identity of $V$.
- The map of the $m \times n$ zero matrix is the zero map, for every choice of bases.

### Non-examples

- [[A translation|PGCAMM8J4T]]: the map $x \mapsto x + (1, 0)$ of $\R^2$ is not linear, so it is not the map of any matrix.
- The map $x \mapsto Ax$ for a $2 \times 3$ matrix $A$ goes from $F^3$ to $F^2$, not from $F^2$ to $F^3$. So no $2 \times 3$ matrix gives a map $F^2 \to F^3$.

### Basic properties

- The matrix of $T_A$ in the bases $B$ and $C$ is $A$, and $T_{[T]_{C,B}} = T$. So the two constructions are inverse, by the [[theorem on linear maps and matrices|Q3EDKTZ6TA]].
- $A \mapsto T_A$ is a linear isomorphism $M_{m \times n}(F) \to \Hom_F(V, W)$.
- $T_{AB} = T_A \circ T_B$ when the bases fit, by the theorem on the [[matrix of a composition|05Q1B7MH0M]].
- For the standard bases of $F^n$ and $F^m$, every linear map $F^n \to F^m$ is $x \mapsto Ax$ for one matrix $A$, by the theorem on [[matrix transformations of $F^n$|W6KB0J3SZZ]].
- The image of $T_A$ corresponds to the [[column space|03AJKXH1AV]] of $A$, and the kernel to the [[null space|0PHDYNR24D]].

### Common errors

- Forgetting that the map depends on the bases, as in the first example.
- Reading the columns of $A$ as standard coordinates when the basis $C$ is not standard.
- Expecting an $m \times n$ matrix to act on $F^m$. It acts on vectors with $n$ entries, one for each column.

## Explanations

### L1 human

A matrix and two bases together define a linear map.
Column $j$ tells where the map sends basis vector $j$.
This undoes the step from a linear map to its matrix.

### L2 human

To evaluate $T_A$ at $v$, find the coordinates $[v]_B$, multiply by $A$, and read the result as coordinates in $C$.
So $T_A = \phi_C^{-1} \circ L_A \circ \phi_B$, where $L_A(x) = Ax$ and $\phi_B$, $\phi_C$ are the coordinate maps.
The space of linear maps $V \to W$ and the space of $m \times n$ matrices have the same structure, so results proved for one hold for the other.

### L3 human

The pair of constructions $T \mapsto [T]_{C,B}$ and $A \mapsto T_A$ is an isomorphism of vector spaces, and of algebras when $V = W$ and $B = C$.
In Mathlib, `Matrix.toLin v₁ v₂` is a linear equivalence whose inverse is `LinearMap.toMatrix v₁ v₂`.
