---
tag: 0KWXYZPJKN
kind: definition
name: Change of basis matrix
msc: [15A03, 15A04]
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

## Remarks

For each $v \in V$, $[v]_B = P [v]_{B'}$.
The matrix $P$ is invertible, and $P^{-1}$ is the change of basis matrix from $B'$ to $B$.
$P$ is the matrix of the identity map of $V$ in the bases $B'$ (domain) and $B$ (codomain).
Conventions differ between authors; some call $P^{-1}$ the change of basis matrix.

## Explanations

### L1 human

The change of basis matrix lists the new basis vectors in the old coordinates.
It translates coordinates in the new basis into coordinates in the old basis.
Its inverse translates in the other direction.
