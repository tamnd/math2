---
tag: 067NKSBEWT
kind: concept
name: Scalar matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
specializes: [044JNC7ZAA]
uses: [044JNC7ZAA, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Scalar matrix
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Properties
inventory: [2HSM4TW6Y6]
---

## Summary

A scalar matrix is a [[diagonal matrix|044JNC7ZAA]] whose diagonal entries are all equal: $cI_n = \operatorname{diag}(c, \dots, c)$.
The [[formal definition|0FRM62SG7D]] states it with the [[identity matrix|06DW9BAWB1]].
Multiplying by $cI$ is the same as multiplying by the scalar $c$: $(cI)A = cA$.
Over a field, the scalar matrices are [[exactly the matrices that commute with every matrix|~c64c046f]].

## Motivation

The scalars act on matrices in two ways: as scalar multiples $cA$ and as products $(cI)A$.
The scalar matrices make the two ways one, so the field $F$ sits inside the ring $M_n(F)$ as $\{cI\}$.
This copy of $F$ is the centre of the ring, the part that commutes with everything.

## Notation

- Books write $cI$, $cI_n$, $c \cdot 1$ or just $c$ when the order is clear, as in $A - \lambda$ for $A - \lambda I$.
- In Mathlib, `Matrix.scalar n c` is the scalar matrix, and `(c : Matrix n n α)` coerces a scalar to it.

## Remarks

### Examples

- [[The matrix 3I commutes with every matrix|~fcc587ea]] and acts as multiplication by $3$.
- [[The scalar matrices form a copy of the field|~6cae0a02]] inside $M_2(\mathbb{R})$.
- The [[zero matrix|0ZTKJJDGR7]] $0 = 0I$ and the identity $I = 1I$ are scalar matrices.

### Non-examples

- [[The diagonal matrix diag(1, 2)|~80d5c38d]] is not scalar, and it does not commute with $E_{12}$.
- The all-ones matrix $J$ is not scalar: it has nonzero entries off the diagonal.

### Basic properties

- $cI + dI = (c + d)I$ and $(cI)(dI) = (cd)I$.
- $(cI)A = cA$ and $A(cI) = Ac$ for every $n \times n$ matrix $A$.
- If $c$ is central in $R$, then $cI$ commutes with every matrix; conversely, the [[centre theorem|~c64c046f]] shows that only such matrices do.
- A matrix that commutes with all [[matrix units|~709aa34e]] is scalar, by [[this lemma|~30ae7883]].
- Over a field, $cI$ is similar only to itself, since $P(cI)P^{-1} = cI$.
- The only eigenvalue of $cI$ is $c$, and every nonzero vector is an [[eigenvector|0N6960W0BV]].

### Common errors

- Writing $A + 2$ for $A + 2I$ and then adding $2$ to every entry.
- Thinking that every diagonal matrix commutes with every matrix; only the scalar ones do.

## Explanations

### L1 human

A scalar matrix has the same number on the whole diagonal and zeros elsewhere.
Multiplying by it is the same as multiplying by that number.
For example, $3 I_2 = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$ triples each vector.

### L2 human

As a linear map, $cI$ stretches every vector by the factor $c$ in every direction.
Since it treats all directions in the same way, it commutes with every other linear map.
The lemma shows the converse: commuting with all maps forces equal treatment of all directions.

### L3 human

The map $c \mapsto cI$ is the structure map $R \to M_n(R)$, and for commutative $R$ it makes $M_n(R)$ an $R$-algebra.
Its image is the centre $Z(M_n(R))$ exactly when $R$ is commutative.
Schur's lemma is a far-reaching relative: an endomorphism of an irreducible representation over an algebraically closed field is scalar.
