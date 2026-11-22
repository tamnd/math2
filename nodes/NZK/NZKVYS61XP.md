---
tag: NZKVYS61XP
kind: proof
name: Proof that the coordinates of an image are the matrix times the coordinates
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
proves: 8B63KHW6D5
uses: [0YYMY95FWS, 0BMVBHTWV2, 0PDVQEP0ZC, E2ZRZGXSNX, 0RJF668P1T]
methods: [41JZ39GE3F, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: Finding the matrix of a transformation
---

## Proof

We expand $v$ in the basis $B$, apply $T$ term by term, and read off the coordinates in $C$; then we test on the basis vectors for uniqueness.
Let $A = [T]_{C,B} = (a_{ij})$.

1. Let $v \in V$ and let $[v]_B = (x_1, \dots, x_n)$, so that $v = \sum_{j=1}^n x_j b_j$ by the definition of the [[coordinate vector|0BMVBHTWV2]].
2. The map $T$ is [[linear|0RJF668P1T]], so
$$T(v) = \sum_{j=1}^n x_j\, T(b_j).$$
3. By the definition of the [[matrix of T|0YYMY95FWS]], $T(b_j) = \sum_{i=1}^m a_{ij} c_i$ for each $j$.
4. We put step 3 into step 2 and exchange the two finite sums:
$$T(v) = \sum_{j=1}^n x_j \sum_{i=1}^m a_{ij} c_i = \sum_{i=1}^m \Bigl(\sum_{j=1}^n a_{ij} x_j\Bigr) c_i.$$
5. Coordinates in a basis are unique, by the [[uniqueness of coordinates|E2ZRZGXSNX]], so coordinate $i$ of $T(v)$ in $C$ is $\sum_{j=1}^n a_{ij} x_j$.
6. By the definition of the [[matrix-vector product|0PDVQEP0ZC]], $\sum_{j=1}^n a_{ij} x_j$ is entry $i$ of $A [v]_B$, so $[T(v)]_C = A [v]_B$.
7. For uniqueness, let $M$ be an $m \times n$ matrix with $[T(v)]_C = M [v]_B$ for each $v \in V$, and take $v = b_j$.
8. Since $b_j = 1 \cdot b_j$, its coordinate vector $[b_j]_B$ is the unit vector $e_j$, so the hypothesis gives $[T(b_j)]_C = M e_j$.
9. The product $M e_j$ is column $j$ of $M$, so column $j$ of $M$ is $[T(b_j)]_C$, which is column $j$ of $A$ by definition.
10. All columns of $M$ and $A$ agree, so $M = A$.

This proves both parts of the statement.

## Idea

Write $v$ as a combination of the basis vectors and push $T$ through the combination.
Each basis vector $b_j$ then contributes $x_j$ times column $j$ of the matrix, and a weighted sum of columns is exactly what a matrix-vector product computes.
For uniqueness, feed in the basis vectors one at a time: each one picks out a single column, so the columns are forced.

## Variants

Some books define the matrix of $T$ as the matrix $M$ with $[T(v)]_C = M[v]_B$ for every $v$.
Steps 7 to 10 show that this definition gives the same matrix as the definition by columns.

A shorter proof uses the coordinate isomorphisms $\phi_B \colon V \to F^n$ and $\phi_C \colon W \to F^m$.
The composite $\phi_C \circ T \circ \phi_B^{-1}$ is a linear map $F^n \to F^m$, so it is $x \mapsto Ax$ for the matrix $A$ whose columns are the images of the unit vectors, by the theorem on [[matrix transformations of Fⁿ|W6KB0J3SZZ]].
Those images are $\phi_C(T(b_j)) = [T(b_j)]_C$, so $A = [T]_{C,B}$, and applying the composite to $\phi_B(v)$ gives the formula.
