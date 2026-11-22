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

Once you choose a basis of each space, a linear map turns into a table of numbers, and every question about the map becomes a question about that table.
The table is built from the images of the basis vectors, one column for each of them.
Let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]] between finite-dimensional spaces over a field $F$, and let $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$ be ordered [[bases|0KCQ9Y3QKA]] of $V$ and $W$.
The matrix of $T$ in these bases is the $m \times n$ [[matrix|0VD9ZSWWJG]] $[T]_{C,B}$ whose column $j$ is the [[coordinate vector|04CYQHN6MC]] $[T(b_j)]_C$.
In entries, $[T]_{C,B} = (a_{ij})$ with
$$T(b_j) = a_{1j} c_1 + a_{2j} c_2 + \dots + a_{mj} c_m \qquad (1 \le j \le n).$$
The [[formal definition|0YYMY95FWS]] states this, and the matrix then computes the map: $[T(v)]_C = [T]_{C,B}\,[v]_B$ for each $v \in V$.

## Motivation

A linear map is fixed by its values on a basis, and each value is fixed by its coordinates in a basis of the target.
So $mn$ numbers hold all the information about $T$, however abstract the spaces are.
Differentiation of polynomials, a rotation of the plane and a map that evaluates a polynomial at two points all become small arrays of numbers.
Then row reduction, which a computer does well, can answer questions about kernels, images and inverses.

The dictionary also works in the other direction.
The [[linear map of a matrix|06HMCTAQH3]] reads a matrix as a map, and the [[matrix of a composition|05Q1B7MH0M]] shows that composing maps is multiplying matrices.
Later the same map is written in several bases at once, and the [[change of basis formula|0MQXVZEBMT]] says how its matrix changes.

## Notation

We write $[T]_{C,B}$ with the basis of the target first, so that the inner letters match in $[S]_{D,C}[T]_{C,B} = [S \circ T]_{D,B}$.
Other books write $[T]_B^C$, $M(T)$ or $\mathcal{M}(T, B, C)$, and some put the domain basis first.
When $V = W$ and $B = C$, we write $[T]_B$.
Mathlib writes `LinearMap.toMatrix v₁ v₂ f`, where `v₁` is the basis of the domain and indexes the columns, so Mathlib also puts the images of the domain basis in the columns.
Watch out for books that write vectors as rows: there the images go in the rows, and the matrix is the transpose of ours.

## Remarks

### A first computation

Take the derivative $D \colon P_2 \to P_1$ on polynomials of degree at most $2$, with the bases $B = (1, x, x^2)$ and $C = (1, x)$.
Differentiate each vector of $B$ and read off its coordinates in $C$:
$$D(1) = 0, \qquad D(x) = 1, \qquad D(x^2) = 2x.$$
These give the columns $(0, 0)$, $(1, 0)$ and $(0, 2)$, so
$$[D]_{C,B} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$$
For $p = 3 + 5x - 4x^2$ the product $[D]_{C,B}(3, 5, -4)^{\mathsf{T}}$ is $(5, -8)^{\mathsf{T}}$, and indeed $p' = 5 - 8x$.
The [[derivative example|KWN1RM45D5]] works this out step by step.
The matrix has $2$ rows because $\dim P_1 = 2$, and $3$ columns because $\dim P_2 = 3$.

### One map, many matrices

The matrix depends on the map and on both bases.
The map $T(x, y) = (2x + y, x + 2y)$ of $\mathbb{R}^2$ has the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ in the standard basis.
In the basis $b_1 = (1, 1)$, $b_2 = (1, -1)$ we find
$$T(b_1) = (3, 3) = 3 b_1, \qquad T(b_2) = (1, -1) = b_2,$$
so the matrix becomes $\begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$.
The diagonal matrix shows at once what $T$ does: it stretches the line through $(1, 1)$ by $3$ and fixes the line through $(1, -1)$.
The [[symmetric map example|7HRGTM3RKJ]] checks the formula $[T(v)]_B = [T]_B [v]_B$ on a vector.

### A rotation

The rotation $R_\theta$ of $\mathbb{R}^2$ by the angle $\theta$ sends $e_1$ to $(\cos\theta, \sin\theta)$ and $e_2$ to $(-\sin\theta, \cos\theta)$.
These two images are the columns of its matrix in the standard basis:
$$[R_\theta] = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
For $\theta = \pi/2$ this is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, which sends $(1, 0)$ to $(0, 1)$ and $(0, 1)$ to $(-1, 0)$.
In the same way, the identity map has the identity matrix $I_n$ when both bases are equal, and in two different bases its matrix is a [[change of basis matrix|0MKRHZB3WS]].

### What it is not

The array with the images of the basis vectors as rows is the transpose of the matrix, and it computes the wrong map.
For $T(x, y) = (x + 2y, 3y)$ the images are $(1, 0)$ and $(2, 3)$, and the array with these rows sends $(0, 1)$ to $(0, 3)$ instead of $(2, 3)$, as the [[non-example with rows|RSET6QRFJR]] shows.
A map that is not linear has no matrix at all.
The map $x \mapsto x + 1$ on $\mathbb{R}$ is not $x \mapsto ax$ for any $a$, since it sends $0$ to $1$.

### The rules you can use

The coordinate formula $[T(v)]_C = [T]_{C,B}[v]_B$ holds for each $v$, and $[T]_{C,B}$ is the only matrix with this property, by the [[coordinate theorem|8B63KHW6D5]].
The map $T \mapsto [T]_{C,B}$ is a linear isomorphism $\Hom(V, W) \to M_{m \times n}(F)$, by the [[theorem on linear maps and matrices|Q3EDKTZ6TA]].
Composition becomes the product, $[S \circ T]_{D,B} = [S]_{D,C}[T]_{C,B}$, by the [[composition theorem|05Q1B7MH0M]].
The [[rank of T|0ZZXSBTR4J]] equals the [[rank|0ZC9YTXZRY]] of $[T]_{C,B}$ for every choice of bases, because the coordinate map of $C$ carries the image of $T$ onto the column space of the matrix.

### Watch out

The coordinates of $T(b_j)$ must be taken in the basis $C$, not in the standard basis.
For the map $T(x, y) = (2x + y, x + 2y)$ and $b_1 = (1, 1)$, the image $(3, 3)$ has standard coordinates $(3, 3)$ but $B$-coordinates $(3, 0)$, and only $(3, 0)$ belongs in $[T]_B$.
The order of each basis also matters.
With $C = (x, 1)$ in place of $(1, x)$, the two rows of $[D]_{C,B}$ above change places.

### History

Matrices were first used to record the coefficients of systems of linear equations.
Cayley's memoir on matrices of 1858 defined the product of two matrices so that it matches the composition of the linear substitutions that they represent.

### Try it

First, find the matrix of $T(x, y) = (x - y, 3x)$ in the standard basis of $\mathbb{R}^2$.
The images are $T(e_1) = (1, 3)$ and $T(e_2) = (-1, 0)$, so the matrix is $\begin{pmatrix} 1 & -1 \\ 3 & 0 \end{pmatrix}$.

Second, find the matrix of the derivative $P_2 \to P_2$ in the basis $(1, x, x^2)$.
The columns are $(0, 0, 0)$, $(1, 0, 0)$ and $(0, 2, 0)$, so the matrix is $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$.

## Explanations

### L1 human

To write a linear map as a table, first apply the map to each basis vector.
Write the coordinates of each answer as a column.
Put these columns side by side, and you have the matrix.
For the map that sends $(x, y)$ to $(x - y, 3x)$, the two answers are $(1, 3)$ and $(-1, 0)$, so these are the two columns.
From then on, multiplying the matrix by the coordinates of any vector gives the coordinates of its image.

### L2 human

Here is a typical use: the map $T \colon P_1 \to \mathbb{R}^2$ with $T(p) = (p(0), p(1))$, which evaluates a linear polynomial at two points.
Use the basis $(1, x)$ of $P_1$ and the standard basis of $\mathbb{R}^2$.
The basis vectors go to
$$T(1) = (1, 1), \qquad T(x) = (0, 1),$$
so the matrix is $A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
For $p = 2 + 3x$ the coordinates are $(2, 3)$, and
$$A \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 + 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 5 \end{pmatrix}.$$
Check: $p(0) = 2$ and $p(1) = 5$.
The matrix $A$ has determinant $1$, so it is invertible, and hence $T$ is an isomorphism: a line is fixed by its values at $0$ and $1$.
The problem shows the typical use, a question about an abstract map answered by a computation with a small matrix.

### L3 human

The coordinate maps $\phi_B \colon V \to F^n$ and $\phi_C \colon W \to F^m$ are isomorphisms, and $[T]_{C,B}$ is the standard matrix of $\phi_C \circ T \circ \phi_B^{-1} \colon F^n \to F^m$.
So choosing bases makes the category of finite-dimensional vector spaces over $F$ equivalent to the category whose objects are the integers $n \ge 0$ and whose arrows $n \to m$ are the $m \times n$ matrices.
In Mathlib, `LinearMap.toMatrix v₁ v₂` is a linear equivalence from linear maps to matrices, whose entry $(i, j)$ is coordinate $i$ of the image of `v₁ j` in the basis `v₂`, and `Matrix.toLin v₁ v₂` is its inverse.
The same construction works for free modules of finite rank over a commutative ring.
The [[change of basis formula|0MQXVZEBMT]] and [[similar matrices|0E89HQATM8]] study how much of the matrix depends on the bases and how much belongs to the map itself.
