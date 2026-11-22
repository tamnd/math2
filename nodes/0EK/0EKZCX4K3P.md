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

A Hermitian matrix is a complex square matrix equal to its conjugate transpose, and a skew-Hermitian matrix is one equal to minus its conjugate transpose.
Let $A = (a_{ij})$ be an $n \times n$ complex [[square matrix|0CP7YY6NAG]], and let $A^*$ be its [[conjugate transpose|0EX045E2BP]].
The matrix $A$ is *Hermitian* when $A^* = A$, that is, $a_{ij} = \overline{a_{ji}}$ for all $i, j \in \{1, \dots, n\}$.
The matrix $A$ is *skew-Hermitian* when $A^* = -A$, that is, $a_{ij} = -\overline{a_{ji}}$ for all $i, j \in \{1, \dots, n\}$.

## Notation

In Mathlib, `Matrix.IsHermitian A` means `Aᴴ = A`, for matrices over any ring with a `star` operation.
Skew-Hermitian matrices are also called *anti-Hermitian*.

## Remarks

The matrix must be square, because $A^*$ has size $n \times m$ when $A$ has size $m \times n$, and the equation $A^* = A$ compares two matrices of the same size.
The condition with $i = j$ reads $a_{ii} = \overline{a_{ii}}$, so a Hermitian matrix has a real diagonal.
In the same way a skew-Hermitian matrix has a purely imaginary diagonal.

For example, $\begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$ is Hermitian: the diagonal is real and $1 - i = \overline{1 + i}$.
The matrix $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ fails the condition at the pair $(1, 2)$, since $\overline{a_{21}} = -i \neq i = a_{12}$, although the matrix is symmetric.

For a real matrix the conjugates change nothing.
So a real matrix is Hermitian exactly when it is [[symmetric|0N28QN4CYA]], and skew-Hermitian exactly when it is [[skew-symmetric|03RNVFDEAN]].
The concept page on [[Hermitian matrices|0P17NGQQMQ]] gives the properties, and the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]] shows that the eigenvalues are real.

## Explanations

### L1 human

A Hermitian matrix is the complex version of a symmetric matrix.
Each entry across the diagonal is the complex conjugate of the entry on this side, so $3 + 2i$ faces $3 - 2i$.

### L2 human

The two conditions differ by a factor $i$.
Since $(iA)^* = -i A^*$, the matrix $A$ is Hermitian exactly when $iA$ is skew-Hermitian.
For example, $iI$ is skew-Hermitian, because $(iI)^* = -iI$.
