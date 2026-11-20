---
tag: 0DXKE10PHF
kind: concept
name: Conjugate transpose
aliases: [hermitian-transpose]
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
uses: [09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
same_as:
  wikidata: Q2051983
  wikipedia: Conjugate transpose
---

## Summary

The conjugate transpose of a complex $m \times n$ matrix $A$ is the $n \times m$ matrix $A^*$ with $(A^*)_{ij} = \overline{a_{ji}}$.
It is the [[transpose|09DXWYRD43]] of the matrix with each entry replaced by its complex conjugate; the [[formal definition|0EX045E2BP]] states the rule.
For complex matrices it takes the place of the transpose, because $x^* x$ is the squared length of $x \in \mathbb{C}^n$.
It gives the [[Hermitian matrices|0P17NGQQMQ]], with $A^* = A$.

## Motivation

The plain transpose is the wrong tool over $\mathbb{C}$.
For $x = (1, i)$ we have $x^{\mathsf{T}} x = 1 + i^2 = 0$, although $x \neq 0$.
The standard inner product on $\mathbb{C}^n$ is $\langle x, y \rangle = y^* x$, and with it $\langle Ax, y \rangle = \langle x, A^* y \rangle$.
So $A^*$ is the matrix of the adjoint map.

## Notation

- Books write $A^*$, $A^{\mathsf{H}}$, $A^H$, $A^\dagger$ or $\overline{A}^{\mathsf{T}}$.
- Physics uses $A^\dagger$ ("A dagger"), and numerical analysis often uses $A^{\mathsf{H}}$.
- Some books use $A^*$ for the plain complex conjugate $\overline{A}$, or for the adjugate. Check the convention of each book.
- In MATLAB, `A'` is the conjugate transpose, and `A.'` is the plain transpose.
- In Mathlib, `Matrix.conjTranspose A` is written `Aᴴ`. It is defined over any ring with a star operation.

## Remarks

### Examples

- [[The conjugate transpose of a 2 × 2 matrix and the product rule|~53ef5cb8]].
- [[For a complex vector x, x*x is its squared length|~185f7b23]].
- For a real matrix, $A^* = A^{\mathsf{T}}$.

### Non-examples

- [[The plain transpose of a complex vector|~21bf0015]] does not give its length.
- The entrywise conjugate $\overline{A}$ is not $A^*$ unless $A$ is symmetric.

### Basic properties

For complex matrices of suitable sizes and $c \in \mathbb{C}$:

- $(A^*)^* = A$ and $(A + B)^* = A^* + B^*$.
- $(cA)^* = \overline{c}\, A^*$, so the map $A \mapsto A^*$ is conjugate-linear, not linear.
- $(AB)^* = B^* A^*$. The proof is the proof of the [[transpose of a product|09GK5PS824]] with conjugates, using $\overline{zw} = \overline{z}\, \overline{w}$.
- $(A^{-1})^* = (A^*)^{-1}$ for an [[invertible|0EB9N0S33C]] $A$.
- $\operatorname{tr}(A^*) = \overline{\operatorname{tr} A}$ and $\det(A^*) = \overline{\det A}$.
- $\operatorname{tr}(A^* A) = \sum_{i,j} |a_{ij}|^2$, which is $0$ only for $A = 0$.

### Common errors

- Forgetting the conjugate in $(cA)^* = \overline{c}\, A^*$.
- Using $x^{\mathsf{T}} y$ as an inner product on $\mathbb{C}^n$.

## Explanations

### L1 human

To find the conjugate transpose, write the rows as columns and change the sign of each imaginary part.
For real matrices, nothing changes except the transpose.

### L2 human

The squared length of $z \in \mathbb{C}$ is $\overline{z} z$, not $z^2$.
So the length of a complex vector uses conjugates, and the matrix that moves across the inner product uses them too.
That matrix is $A^*$.

### L3 human

The map $A \mapsto A^*$ makes $M_n(\mathbb{C})$ a $*$-algebra, and with the operator norm a C*-algebra.
Mathlib defines `conjTranspose` for any ring with an involution `star`, so the same notation covers quaternion matrices.
