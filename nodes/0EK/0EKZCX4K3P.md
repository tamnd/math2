---
tag: 0EKZCX4K3P
kind: definition
name: Hermitian matrix
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: 0P17NGQQMQ
uses: [0EX045E2BP, 0CP7YY6NAG]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.IsHermitian
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: lead section
inventory: [C1N93YZJGX]
---

## Definition

Let $A = (a_{ij})$ be an $n \times n$ complex [[square matrix|0CP7YY6NAG]], and let $A^*$ be its [[conjugate transpose|0EX045E2BP]].
The matrix $A$ is *Hermitian* when $A^* = A$, that is, $a_{ij} = \overline{a_{ji}}$ for all $i$ and $j$.
The matrix $A$ is *skew-Hermitian* when $A^* = -A$, that is, $a_{ij} = -\overline{a_{ji}}$ for all $i$ and $j$.

## Notation

- In Mathlib, `Matrix.IsHermitian A` means `Aᴴ = A`, for matrices over a ring with a `star` operation.
- Skew-Hermitian matrices are also called *anti-Hermitian*.

## Remarks

- The diagonal entries of a Hermitian matrix are real, and those of a skew-Hermitian matrix are purely imaginary.
- A real matrix is Hermitian if and only if it is [[symmetric|0N28QN4CYA]], and skew-Hermitian if and only if it is [[skew-symmetric|03RNVFDEAN]].
- The eigenvalues of a Hermitian matrix are real, and $\mathbb{C}^n$ has an orthonormal basis of eigenvectors, by the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]].
- The matrix $\begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$ is Hermitian.

## Explanations

### L1 human

A Hermitian matrix is the complex version of a symmetric matrix.
The entry across the diagonal is the complex conjugate of the entry here.

### L2 human

The two conditions differ by a factor $i$: $A$ is Hermitian exactly when $iA$ is skew-Hermitian.
