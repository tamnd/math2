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

A matrix together with a basis of each space defines a linear map, and this reverses the step from a map to its matrix.
Column $j$ of the matrix says where the map sends the $j$-th basis vector.
Let $A = (a_{ij})$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over a field $F$, and let $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$ be ordered [[bases|0KCQ9Y3QKA]] of vector spaces $V$ and $W$.
The linear map of $A$ in these bases is the [[linear map|0NRYHJPQG2]] $T_A \colon V \to W$ with
$$T_A(b_j) = a_{1j} c_1 + a_{2j} c_2 + \dots + a_{mj} c_m \qquad (1 \le j \le n).$$
It is the unique linear map whose [[matrix|0YQSGNYE3K]] in the bases $B$ and $C$ is $A$, and the [[formal definition|009892PZ30]] states it.
Together the two constructions identify $\Hom(V, W)$ with the space $M_{m \times n}(F)$ of matrices.

## Motivation

Matrices are easy to store and to compute with, while linear maps carry the meaning.
A dictionary between them is useful only if it works in both directions.
The matrix of a map goes from maps to matrices, and the linear map of a matrix goes back.
For $V = F^n$ and $W = F^m$ with the standard bases, the linear map of $A$ is the familiar map $x \mapsto Ax$.

The return direction is what lets us build maps to order.
To get a map of the plane that sends $(1, 1)$ to $(2, 0)$ and $(1, -1)$ to $(0, 5)$, put the two images in the columns of a matrix and read it in the basis $((1, 1), (1, -1))$ of the domain, as L2 below does.
Because the dictionary is a [[linear isomorphism|0B8T10CE7N]], facts about matrices, such as $\dim M_{m \times n}(F) = mn$, become facts about maps.

## Notation

Books write $T_A$, $L_A$ or $x \mapsto Ax$, and often they leave the bases out of the notation.
Mathlib writes `Matrix.toLin v₁ v₂ A`, where `v₁` is the basis of the domain and `v₂` the basis of the target.
For the standard bases of `n → R` and `m → R`, Mathlib also has `Matrix.toLin'` and `Matrix.mulVecLin`.
An $m \times n$ matrix acts on columns with $n$ entries, one for each column of $A$, and returns columns with $m$ entries.

## Remarks

### A first computation

Read the matrix $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ in the basis $(1, x)$ of the space $P_1$ of linear polynomials, on both sides.
The columns say
$$T_A(1) = 0 \cdot 1 + 0 \cdot x = 0, \qquad T_A(x) = 1 \cdot 1 + 0 \cdot x = 1.$$
So $T_A(a + bx) = b$, which is the derivative of $a + bx$.
For $p = 4 + 7x$ the coordinates $(4, 7)$ go to $A(4, 7)^{\mathsf{T}} = (7, 0)^{\mathsf{T}}$, the coordinates of $p' = 7$.
In the standard basis of $\mathbb{R}^2$ the same matrix gives the map $(x, y) \mapsto (y, 0)$.

### One matrix, many maps

The map depends on the bases.
The matrix $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ is a shear $(x, y) \mapsto (x + 2y, y)$ in the standard basis of $\mathbb{R}^2$.
In the basis $((1, 1), (0, 1))$ on both sides it is the map $(x, y) \mapsto (-x + 2y, -2x + 3y)$, as [[one matrix in two bases|V8J40J1DKG]] works out.
The two maps differ already at $(1, 0)$, which goes to $(1, 0)$ and to $(-1, -2)$.
A row is a matrix too: in the standard bases, $\begin{pmatrix} 1 & 0 & -1 \end{pmatrix}$ gives the linear form $(x, y, z) \mapsto x - z$ on $\mathbb{R}^3$.

### Matrix units give a basis of maps

The matrix unit $E_{ij}$ has entry $1$ in place $(i, j)$ and $0$ elsewhere.
Its linear map sends $b_j$ to $c_i$ and every other $b_k$ to $0$.
Every matrix is $A = \sum_{i,j} a_{ij} E_{ij}$ in exactly one way, and the map of $A$ is the same combination of the maps of the $E_{ij}$.
So these $mn$ maps form a basis of $\Hom(V, W)$, as the [[example on matrix units|XQB25QZHAH]] checks for $\Hom(\mathbb{R}^3, \mathbb{R}^2)$.

### What it is not

A translation of the plane is not the linear map of any matrix.
The map $f(x, y) = (x + 1, y)$ sends the origin to $(1, 0)$, while every linear map fixes the origin, as the [[translation non-example|PGCAMM8J4T]] shows.
Size is the other condition that can fail.
A $2 \times 3$ matrix gives maps from a space of dimension $3$ to a space of dimension $2$, so no $2 \times 3$ matrix gives a map $F^2 \to F^3$.

### The rules you can use

The matrix of $T_A$ in the bases $B$ and $C$ is $A$, and the map of $[T]_{C,B}$ is $T$, so the two constructions are inverse to each other.
The assignment $A \mapsto T_A$ is linear, so $T_{A + A'} = T_A + T_{A'}$ and $T_{cA} = c\,T_A$, and it is an isomorphism $M_{m \times n}(F) \cong \Hom(V, W)$ by the [[theorem on linear maps and matrices|Q3EDKTZ6TA]].
Products become composites, $T_{AA'} = T_A \circ T_{A'}$ when the bases fit, by the theorem on the [[matrix of a composition|05Q1B7MH0M]].
The image of $T_A$ corresponds to the [[column space|03AJKXH1AV]] of $A$, and its kernel to the [[null space|0PHDYNR24D]].

### Watch out

The columns of $A$ are coordinates in $C$, not standard coordinates.
With $C = ((1, 1), (0, 1))$, the column $(2, 1)$ stands for the vector $2(1, 1) + 1(0, 1) = (2, 3)$, not for $(2, 1)$.
Also, an $m \times n$ matrix acts on vectors with $n$ entries, not $m$: the $2 \times 3$ matrix $\begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 0 \end{pmatrix}$ sends $(1, 1, 1)$ to $(5, 1)$ and cannot act on $(1, 1)$.

### Try it

First, find the map of $\begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$ in the standard basis of $\mathbb{R}^2$.
It sends $e_1$ to $(2, 1)$ and $e_2$ to $(0, 3)$, so it is $(x, y) \mapsto (2x, x + 3y)$.

Second, find a matrix whose map in the standard bases is $(x, y, z) \mapsto (y, z)$ from $\mathbb{R}^3$ to $\mathbb{R}^2$.
The images of $e_1, e_2, e_3$ are $(0, 0)$, $(1, 0)$ and $(0, 1)$, so the matrix is $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.

## Explanations

### L1 human

A matrix and two bases together define a linear map.
Column $j$ tells you where the map sends basis vector number $j$.
For the matrix with columns $(2, 1)$ and $(0, 3)$ in the standard basis, the first arrow $(1, 0)$ goes to $(2, 1)$ and the second arrow $(0, 1)$ goes to $(0, 3)$.
Every other vector then goes where linearity sends it, so this undoes the step from a map to its matrix.

### L2 human

Here is a typical use: build the map $T$ of $\mathbb{R}^2$ with $T(1, 1) = (2, 0)$ and $T(1, -1) = (0, 5)$.
Take the basis $B = ((1, 1), (1, -1))$ of the domain and the standard basis $E$ of the target.
The matrix with the images as columns is $A = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$, and $T$ is its linear map in the bases $B$ and $E$.
To evaluate $T(3, 1)$, first find $[(3, 1)]_B$ from $a + b = 3$ and $a - b = 1$, so $a = 2$ and $b = 1$.
Then
$$A \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 5 \end{pmatrix},$$
so $T(3, 1) = (4, 5)$.
Check: $T(3, 1) = 2\,T(1, 1) + T(1, -1) = (4, 0) + (0, 5) = (4, 5)$.
In general $T_A = \phi_C^{-1} \circ L_A \circ \phi_B$, where $L_A(x) = Ax$ and $\phi_B$, $\phi_C$ are the coordinate maps.

### L3 human

The pair of constructions $T \mapsto [T]_{C,B}$ and $A \mapsto T_A$ is an isomorphism of vector spaces, and of algebras $\End(V) \cong M_n(F)$ when $V = W$ and $B = C$.
In Mathlib, `Matrix.toLin v₁ v₂` is a linear equivalence whose inverse is `LinearMap.toMatrix v₁ v₂`.
The isomorphism depends on the bases, and the [[change of basis formula|0MQXVZEBMT]] says how: in new bases, the map $T_A$ has the matrix $Q^{-1} A P$ for suitable invertible matrices $P$ and $Q$.
Over a commutative ring the same construction identifies the maps between free modules of finite rank with matrices.
