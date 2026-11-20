---
tag: 0KWXYZPJKN
kind: definition
name: Change of basis matrix
msc: ["15A03", "15A04"]
topics: [S6559D61BP]
audience: ug1
defines: 0MKRHZB3WS
uses: [0VTQTPQGAV, 0BMVBHTWV2]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Change-of-basis formula
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$ with two [[bases|0KCQ9Y3QKA]] $B = (b_1, \dots, b_n)$ and $B' = (b'_1, \dots, b'_n)$.
The *change of basis matrix* from $B$ to $B'$ is the $n \times n$ matrix $P = (p_{ij})$ defined by
$$b'_j = \sum_{i=1}^{n} p_{ij} b_i \qquad (1 \le j \le n).$$
Its column $j$ is the [[coordinate vector|04CYQHN6MC]] $[b'_j]_B$.

## Notation

The matrix is written $P$, $P_{B \to B'}$ or $[\id_V]_{B, B'}$.
In Mathlib, `Basis.toMatrix e v` has as column $j$ the coordinates of $v_j$ in the basis $e$, so it is $P$ for $B = e$ and $B' = v$.

## Remarks

For each $v \in V$, $[v]_B = P [v]_{B'}$.
The matrix $P$ is invertible, and $P^{-1}$ is the change of basis matrix from $B'$ to $B$.
$P$ is the matrix of the identity map of $V$ in the bases $B'$ (domain) and $B$ (codomain).
Conventions differ between authors, and some call $P^{-1}$ the change of basis matrix from $B$ to $B'$.
Lay writes $P_{C \leftarrow B}$ for the matrix with columns $[b_j]_C$, which changes $B$-coordinates into $C$-coordinates.

## Explanations

### L1 human

The change of basis matrix lists the new basis vectors in the old coordinates.
It translates coordinates in the new basis into coordinates in the old basis.
Its inverse translates in the other direction.

### L2 human

For $V = \R^2$, $B$ the standard basis and $B' = ((1, 1), (1, -1))$, the matrix is $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
The new coordinates $(3, 2)$ give the old coordinates $P(3, 2) = (5, 1)$.
