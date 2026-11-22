---
tag: 0N28QN4CYA
kind: definition
name: Symmetric matrix
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: 0VR671PHE5
uses: [0W809K6AW0, 0CP7YY6NAG]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.IsSymm
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: lead section
inventory: [42HBTH0KFH]
---

## Definition

We define the square matrices that equal their own transpose.
Let $R$ be a ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
The matrix $A$ is *symmetric* when $A^{\mathsf{T}} = A$, where $A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]] of $A$; equivalently, $a_{ij} = a_{ji}$ for all $i, j \in \{1, \dots, n\}$.

## Notation

The condition is also written $A = A^t$, $A = {}^t\!A$ or $A = A'$, following the notation for the transpose.
Some books write $\operatorname{Sym}_n(F)$ or $S_n(F)$ for the set of symmetric $n \times n$ matrices over $F$.
In Mathlib, `Matrix.IsSymm A` means `Aᵀ = A`, for a matrix whose rows and columns are indexed by the same finite type.

## Remarks

The definition asks for a square matrix, since only then do $A$ and $A^{\mathsf{T}}$ have the same size.
The condition $a_{ij} = a_{ji}$ says nothing when $i = j$, so the diagonal entries are free, and the entries below the diagonal are copies of those above it.
For example, $\begin{pmatrix} 1 & 7 \\ 7 & 2 \end{pmatrix}$ is symmetric, while $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ is not, because $a_{12} = 2$ and $a_{21} = 0$.

For every $m \times n$ matrix $B$ over a commutative ring, the matrices $B^{\mathsf{T}} B$ and $B B^{\mathsf{T}}$ are symmetric; see [[this example|VR8VKQA9BN]].
A product of two symmetric matrices, however, is symmetric only when they commute, by [[this theorem|YX9Z3E9SGN]].
In a basis, symmetric matrices are the matrices of [[symmetric bilinear forms|0AXZNE5XNH]], and over $\mathbb{R}$ the [[spectral theorem|06J4PXRG22]] diagonalizes them in an orthonormal basis.
The concept page on [[symmetric matrices|0VR671PHE5]] has more examples and properties.

## Explanations

### L1 human

A symmetric matrix looks the same after you flip it over its main diagonal.
The number in row $i$, column $j$ equals the number in row $j$, column $i$.

### L2 human

To check that a matrix is symmetric, compare each entry above the diagonal with its mirror entry below the diagonal.
For a $3 \times 3$ matrix there are three pairs to compare: $(1, 2)$ with $(2, 1)$, $(1, 3)$ with $(3, 1)$, and $(2, 3)$ with $(3, 2)$.
Only the $n(n+1)/2$ entries on and above the diagonal are free, so over a field the symmetric $n \times n$ matrices form a space of dimension $n(n+1)/2$, which is $6$ for $n = 3$.
