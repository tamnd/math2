---
tag: 0P17NGQQMQ
kind: concept
name: Hermitian matrix
aliases: [self-adjoint-matrix]
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0MR0BYF0K2]
uses: [0DXKE10PHF, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Skew-Hermitian_matrix
    locator: lead section
same_as:
  wikidata: Q652941
  wikipedia: Hermitian matrix
inventory: [C1N93YZJGX]
---

## Summary

A Hermitian matrix is a complex square matrix equal to its [[conjugate transpose|0DXKE10PHF]]: $A^* = A$.
A skew-Hermitian matrix satisfies $A^* = -A$.
The [[formal definition|0EKZCX4K3P]] says $a_{ij} = \overline{a_{ji}}$, so the diagonal of a Hermitian matrix is real.
Hermitian matrices are the complex analogue of [[symmetric matrices|0VR671PHE5]], and they play the role of real numbers among matrices.
Each complex square matrix is $H + iK$ with $H$ and $K$ Hermitian, by the [[Cartesian decomposition|E2MNC3W2DM]].

## Motivation

A complex number $z$ is real exactly when $\overline{z} = z$, and imaginary exactly when $\overline{z} = -z$.
The equations $A^* = A$ and $A^* = -A$ are the matrix versions.
The [[spectral theorem for Hermitian matrices|0DGZBQWZWN]] supports this view: a Hermitian matrix has real eigenvalues.
In quantum mechanics, observable quantities are Hermitian operators.

## Notation

- Another name is *self-adjoint matrix*.
- In Mathlib, `Matrix.IsHermitian A` means `Aᴴ = A`.
- Mathlib has no separate name for skew-Hermitian; the condition is written `Aᴴ = -A`.

## Remarks

### Examples

- [[A Hermitian 2 × 2 matrix with real eigenvalues|GGFA8S4NZ2]].
- [[The Cartesian decomposition of a 2 × 2 matrix|NQBXQ87CXZ]].
- A real symmetric matrix is Hermitian.
- $iI$ and $\begin{pmatrix} i & 1 \\ -1 & 0 \end{pmatrix}$ are skew-Hermitian.

### Non-examples

- [[A complex symmetric matrix that is not Hermitian|DAZBNZXZK7]].
- $iI$ is not Hermitian, because $(iI)^* = -iI$.

### Basic properties

Let $A$ and $B$ be Hermitian $n \times n$ matrices.

- The diagonal entries are real, because $a_{ii} = \overline{a_{ii}}$.
- $A + B$ and $cA$ for real $c$ are Hermitian. So the Hermitian matrices form a real vector space of dimension $n^2$, not a complex one.
- $A$ is Hermitian if and only if $iA$ is skew-Hermitian.
- $AB$ is Hermitian if and only if $AB = BA$, by the same proof as for [[symmetric matrices|YX9Z3E9SGN]].
- $x^* A x$ is real for each $x \in \mathbb{C}^n$, because $\overline{x^* A x} = (x^* A x)^* = x^* A^* x = x^* A x$.
- $C^* C$ and $C C^*$ are Hermitian for every complex matrix $C$.
- Hermitian and skew-Hermitian matrices are [[normal|0MR0BYF0K2]], so they are unitarily diagonalizable; this is later theory.

### Common errors

- Calling a complex symmetric matrix Hermitian.
- Treating the Hermitian matrices as a complex subspace. The product of $i$ and a nonzero Hermitian matrix is not Hermitian.

## Explanations

### L1 human

A Hermitian matrix is the complex version of a symmetric matrix.
The entry across the diagonal is the complex conjugate of the entry here, and the diagonal entries are real.

### L2 human

The equation $A^* = A$ says $\langle Ax, y \rangle = \langle x, Ay \rangle$ for the standard inner product.
Then $\langle Ax, x \rangle$ is always real, and for an eigenvector $x$ with eigenvalue $\lambda$ this gives $\lambda \in \mathbb{R}$.

### L3 human

The map $A \mapsto (H, K)$ of the Cartesian decomposition identifies $M_n(\mathbb{C})$ with the complexification of the real space of Hermitian matrices.
The skew-Hermitian matrices are the Lie algebra $\mathfrak{u}(n)$ of the unitary group.
