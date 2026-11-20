---
tag: 0ZZQ2E1MTE
kind: statement
role: proposition
name: Determinant of the transpose
aliases: [determinant-of-a-transpose]
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 0W809K6AW0]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.det_transpose
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

Let $K$ be a commutative ring and let $A$ be an $n \times n$ matrix over $K$.
Then
$$\det A^{T} = \det A,$$
where $A^{T}$ is the [[transpose|0W809K6AW0]] of $A$ and $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### Why each hypothesis is needed

The ring must be commutative.
Over the quaternions, with $A = \begin{pmatrix} i & j \\ i & j \end{pmatrix}$, the naive formula $a_{11} a_{22} - a_{12} a_{21}$ gives $ij - ji = 2k$ for $A$ and $ij - ij = 0$ for $A^{T}$.

### Consequences

- $\det$ is multilinear and alternating in the columns, and the rules for [[row operations|09YB3WQG38]] hold for column operations.
- A matrix with two equal columns or a zero column has determinant $0$.
- The [[Laplace expansion|0C08BQ3M05]] along a column follows from the expansion along a row.
- For an orthogonal matrix $Q$, $Q^{T} Q = I$ gives $(\det Q)^2 = 1$ with [[multiplicativity|04CPJ6AF00]], so $\det Q = \pm 1$.

### Converse

The statement is an identity, so there is no converse in the usual sense.
It shows that the three properties of the definition, stated for columns, characterize the same function; this is part of the [[equivalence theorem|W3JN0WPZ10]].

### Generalizations

For a linear map $f \colon V \to V$ with dual map $f^{*} \colon V^{*} \to V^{*}$, $\det f^{*} = \det f$.
For non-square matrices the [[Cauchy-Binet formula|08WE2W7DYS]] plays the role of this identity: the $k \times k$ minors of $A^{T}$ are those of $A$.

## Explanations

### L1 human

Turning a square table on its diagonal, so that rows become columns, does not change the determinant.
So every rule for rows has a twin rule for columns.
For example, $\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = -2 = \det \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.

### L2 human

We check the rule on $A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 2 \end{pmatrix}$.

1. Expansion along row $1$ gives $\det A = 2 (6 - 2) - 0 + 1 (1 - 3) = 8 - 2 = 6$.
2. $A^{T} = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 3 & 1 \\ 1 & 2 & 2 \end{pmatrix}$.
3. Expansion of $A^{T}$ along row $1$ gives $2 (6 - 2) - 1 (0 - 1) + 1 (0 - 3) = 8 + 1 - 3 = 6$.

The typical use is to choose freely between rows and columns in a computation.
A trap: $\det A^{T} = \det A$ does not mean $A^{T} = A$; the matrices above differ.

### L3 human

In invariant terms, $A^{T}$ represents the dual map, and the top exterior power of the dual is the dual of the top exterior power.
Both maps act on a free module of rank $1$ by the same scalar.
