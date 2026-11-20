---
tag: 09DXWYRD43
kind: concept
name: Transpose
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.1
same_as:
  wikidata: Q223683
  wikipedia: Transpose
---

## Summary

The transpose of an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ is the $n \times m$ matrix $A^{\mathsf{T}}$ with $(A^{\mathsf{T}})_{ij} = a_{ji}$.
The [[formal definition|0W809K6AW0]] states the rule.
The rows of $A^{\mathsf{T}}$ are the columns of $A$, so the transpose reflects the array in its main diagonal.
It turns column vectors into row vectors, and it writes the [[dot product|0S52TNNTH9]] as $u^{\mathsf{T}} v$.
The key rule is the [[reversal of products|09GK5PS824]], $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$.

## Motivation

Many formulas need both rows and columns of the same matrix.
The transpose lets us speak of the rows of $A$ as the columns of $A^{\mathsf{T}}$.
It moves a matrix to the other side of a dot product: $(Ax) \cdot y = x \cdot (A^{\mathsf{T}} y)$.
This rule is the coordinate form of the dual map, and it is the source of [[symmetric matrices|0VR671PHE5]] and of least squares.

## Notation

- Books write $A^{\mathsf{T}}$, $A^T$, $A^t$, ${}^t\!A$, ${}^{\mathsf{T}}\!A$, $A'$ or $A^{\top}$.
- The notation $A'$ is common in statistics and in MATLAB, where `A'` is the conjugate transpose and `A.'` is the plain transpose.
- Some books write $A^t$ for the transpose and $A^*$ for the [[conjugate transpose|0DXKE10PHF]]; in other books $A^*$ is the adjugate or the adjoint map.
- Do not confuse $A^t$ with a power of $A$, or ${}^t\!A$ with a superscript on the previous symbol.
- In Mathlib, `Aᵀ` is notation for `Matrix.transpose A`, written with the Unicode character `ᵀ`.

## Remarks

### Examples

- [[The transpose of a 2 × 3 matrix and its rules|~7c0c40f2]].
- [[For an invertible 2 × 2 matrix, the inverse of the transpose is the transpose of the inverse|~543933c8]].
- For a column $x \in \mathbb{R}^n$, $x^{\mathsf{T}}$ is a row and $x^{\mathsf{T}} x = \|x\|^2$.

### Non-examples

- [[Turning the array by a quarter turn|~84079e58]] is not the transpose.
- Reversing the order of the rows is not the transpose.

### Basic properties

For matrices over a commutative ring:

- $(A^{\mathsf{T}})^{\mathsf{T}} = A$, $(A + B)^{\mathsf{T}} = A^{\mathsf{T}} + B^{\mathsf{T}}$ and $(cA)^{\mathsf{T}} = c A^{\mathsf{T}}$.
- $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$, by the [[transpose of a product|09GK5PS824]].
- $(A^{-1})^{\mathsf{T}} = (A^{\mathsf{T}})^{-1}$ for an [[invertible matrix|0EB9N0S33C]] $A$.
- $\operatorname{tr}(A^{\mathsf{T}}) = \operatorname{tr} A$, by [[this statement|09E1RCZ7YT]], and $\det A^{\mathsf{T}} = \det A$, by the [[determinant of the transpose|0ZZQ2E1MTE]].
- $(Ax) \cdot y = x \cdot (A^{\mathsf{T}} y)$ for column vectors $x$ and $y$.
- The [[rank|0ZC9YTXZRY]] of $A^{\mathsf{T}}$ equals the rank of $A$, by the later theorem that [[row rank equals column rank|0TZAG60ZYT]].
- In any bases, the [[matrix of the dual map is the transpose|0ZPB3180AY]] of the matrix of the map.

### History

- Cayley used the transposed matrix in his memoir of 1858.

### Common errors

- Writing $(AB)^{\mathsf{T}} = A^{\mathsf{T}} B^{\mathsf{T}}$; for non-square matrices this is often not even defined.
- Using the plain transpose for complex matrices where the [[conjugate transpose|0DXKE10PHF]] is needed.
- Reading $A'$ as a derivative or as another matrix.

## Explanations

### L1 human

To transpose a matrix, write its rows as columns.
The first row becomes the first column, the second row becomes the second column, and so on.
A $2 \times 3$ matrix becomes a $3 \times 2$ matrix.

### L2 human

The transpose reflects the array in the main diagonal, so diagonal entries stay where they are.
The rule $(Ax) \cdot y = x \cdot (A^{\mathsf{T}} y)$ is the useful property: $A^{\mathsf{T}}$ is the matrix that moves across the dot product.
This explains the reversal $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$, because $A$ must move across first.

### L3 human

For a linear map $f : V \to W$, the dual map $f^* : W^* \to V^*$ sends $\varphi$ to $\varphi \circ f$.
In dual bases, its matrix is the transpose of the matrix of $f$.
The transpose is an anti-automorphism of $M_n(R)$ for commutative $R$; over a noncommutative ring $R$ it is an anti-isomorphism $M_n(R) \to M_n(R^{\mathrm{op}})$.
