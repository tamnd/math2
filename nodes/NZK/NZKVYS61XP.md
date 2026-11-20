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

Let $A = [T]_{C,B} = (a_{ij})$.

1. Let $v \in V$ and let $[v]_B = (x_1, \dots, x_n)$. Then $v = \sum_{j=1}^n x_j b_j$, by the definition of the [[coordinate vector|0BMVBHTWV2]].
2. By the [[linearity|0RJF668P1T]] of $T$, $T(v) = \sum_{j=1}^n x_j T(b_j)$.
3. By the definition of the [[matrix of $T$|0YYMY95FWS]], $T(b_j) = \sum_{i=1}^m a_{ij} c_i$ for each $j$.
4. Put step 3 into step 2 and change the order of the finite sums: $T(v) = \sum_{i=1}^m \bigl(\sum_{j=1}^n a_{ij} x_j\bigr) c_i$.
5. By the [[uniqueness of coordinates|E2ZRZGXSNX]], coordinate $i$ of $T(v)$ in the basis $C$ is $\sum_{j=1}^n a_{ij} x_j$.
6. By the definition of the [[matrix-vector product|0PDVQEP0ZC]], $\sum_{j=1}^n a_{ij} x_j$ is entry $i$ of $A [v]_B$. So $[T(v)]_C = A [v]_B$.
7. For the uniqueness, let $M$ be an $m \times n$ matrix with $[T(v)]_C = M [v]_B$ for each $v$. Take $v = b_j$. Then $[b_j]_B = e_j$, the standard unit vector, since $b_j = 1 \cdot b_j$.
8. The product $M e_j$ is column $j$ of $M$. So column $j$ of $M$ is $[T(b_j)]_C$, which is column $j$ of $A$ by the definition.
9. All the columns of $M$ and $A$ agree. So $M = A$.

## Idea

Expand $v$ in the basis $B$ and apply $T$ term by term.
Each basis vector $b_j$ contributes $x_j$ times column $j$ of the matrix, and this weighted sum of columns is the matrix-vector product.
Testing on the basis vectors gives the uniqueness.

## Variants

- Some books define the matrix of $T$ by the formula $[T(v)]_C = M[v]_B$ for each $v$. Steps 7 to 9 show that this definition gives the same matrix.
- With the coordinate isomorphisms $\phi_B$ and $\phi_C$, the statement says that $\phi_C \circ T \circ \phi_B^{-1}$ is the map $x \mapsto Ax$. This form follows from [[matrix transformations of $F^n$|W6KB0J3SZZ]].
