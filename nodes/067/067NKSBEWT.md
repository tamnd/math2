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

A scalar matrix is a number dressed up as a matrix: multiplying by it does exactly what multiplying by the number does.
For example,
$$3I_2 = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}, \qquad 3I_2 \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 3x \\ 3y \end{pmatrix}.$$
In general, a scalar matrix is a [[diagonal matrix|044JNC7ZAA]] whose diagonal entries are all equal, $cI_n = \operatorname{diag}(c, \dots, c)$, where $I_n$ is the [[identity matrix|06DW9BAWB1]].
The [[formal definition|0FRM62SG7D]] states this for a ring $R$ of entries.
For every $n \times n$ matrix $A$, the product $(cI)A$ is the scalar multiple $cA$.
Over a field, the scalar matrices are [[exactly the matrices that commute with every matrix|DVZ1V4A884]].

## Motivation

A number $c$ can act on a matrix in two ways: as the scalar multiple $cA$, or through a matrix product.
The scalar matrix $cI$ makes these two ways agree, since $(cI)A = cA$.
So a field $F$ sits inside the ring $M_n(F)$ as the set $\{ cI : c \in F \}$, and we can treat numbers as matrices without changing any answer.
This is what lets us plug a matrix into a polynomial: in $A^2 - 3A + 2$, the constant $2$ means $2I$.
This copy of $F$ is also the center of the ring, the part that commutes with everything.

## Notation

Books write $cI$, $cI_n$, $c \cdot 1$, or just $c$ when the size is clear, as in $A - \lambda$ for $A - \lambda I$.
In Mathlib, `Matrix.scalar n c` is the scalar matrix, and it equals `Matrix.diagonal (fun _ => c)`.

## Remarks

### Examples and a non-example

The [[matrix 3I commutes with every matrix|B8AH9ZEYTX]] and acts as multiplication by $3$.
Inside $M_2(\mathbb{R})$, the [[scalar matrices form a copy of the real numbers|SJM276KGDB]].
The [[zero matrix|0ZTKJJDGR7]] $0 = 0I$ and the identity $I = 1I$ are scalar matrices.
The [[diagonal matrix diag(1, 2)|RGEJG5KD95]] is not scalar, and it does not commute with $E_{12}$.
The all-ones matrix $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ is not scalar either, since it has nonzero entries off the diagonal.

### Arithmetic with scalar matrices

Scalar matrices add and multiply like their values:
$$cI + dI = (c + d)I, \qquad (cI)(dI) = (cd)I.$$
For every $n \times n$ matrix $A$, the products are $(cI)A = cA$ and $A(cI) = Ac$, where $Ac$ multiplies each entry of $A$ on the right by $c$.
Over a field, $cI$ is invertible exactly when $c \ne 0$, with inverse $c^{-1} I$.

### Commuting with everything

If $c$ is central in $R$, then $cI$ commutes with every matrix, because $cA = Ac$.
The [[center theorem|DVZ1V4A884]] shows that only such matrices do.
The [[lemma on matrix units|TX4J5JR205]] gives a sharper test: a matrix that commutes with all [[matrix units|A4HTT7JFD1]] is already scalar.
Over a field, $cI$ is similar only to itself, since $P(cI)P^{-1} = cPP^{-1} = cI$.
Its only eigenvalue is $c$, and every nonzero vector is an [[eigenvector|0N6960W0BV]].

### Watch out

Writing $A + 2$ for $A + 2I$ is common, but it means adding $2$ to the diagonal only, not to every entry.
For example,
$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} + 2I = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}.$$
Also, not every diagonal matrix commutes with every matrix; among the diagonal matrices, only the scalar ones do.

### Try it

Which values of $c$ make $cI_2$ equal to its own square?
Answer: $(cI)^2 = c^2 I$, so we need $c^2 = c$, and over $\mathbb{R}$ this gives $c = 0$ or $c = 1$.

## Explanations

### L1 human

A scalar matrix has the same number all along the diagonal and zeros everywhere else.
Multiplying by it is the same as multiplying by that number.
For example, $3 I_2$ triples each vector, and $3I_2$ times any matrix is that matrix with every entry tripled.

### L2 human

As a linear map, $cI$ stretches every vector by the factor $c$, in every direction at once.
Since it treats all directions in the same way, it commutes with every other linear map.
The [[lemma on matrix units|TX4J5JR205]] shows the converse: commuting with all maps forces equal treatment of all directions.
The typical use is in polynomials of a matrix and in $A - \lambda I$, where numbers must become matrices before they can be added to $A$.

### L3 human

For every ring $R$, the map $c \mapsto cI$ is an injective ring homomorphism $R \to M_n(R)$, and for a commutative $R$ it is the structure map that makes $M_n(R)$ an $R$-algebra.
Its image is the center $Z(M_n(R))$ exactly when $R$ is commutative, since the center is $\{ cI : c \in Z(R) \}$.
Schur's lemma is a far-reaching relative: an endomorphism of a finite-dimensional irreducible representation over an algebraically closed field is scalar.
