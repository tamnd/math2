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

Let $R$ be a ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
The matrix $A$ is *symmetric* when $A^{\mathsf{T}} = A$, where $A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]] of $A$.
Equivalently, $a_{ij} = a_{ji}$ for all $i$ and $j$.

## Notation

- In Mathlib, `Matrix.IsSymm A` means `Aᵀ = A`.
- Some books write $\operatorname{Sym}_n(F)$ or $S_n(F)$ for the set of symmetric $n \times n$ matrices over $F$.

## Remarks

- The matrix $\begin{pmatrix} 1 & 7 \\ 7 & 2 \end{pmatrix}$ is symmetric.
- For each $m \times n$ matrix $B$ over a commutative ring, $B^{\mathsf{T}} B$ and $B B^{\mathsf{T}}$ are symmetric; see [[this example|~fca1333e]].
- A real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors, by the [[spectral theorem|06J4PXRG22]].
- Symmetric matrices represent [[symmetric bilinear forms|0AXZNE5XNH]] in a basis.

## Explanations

### L1 human

A symmetric matrix looks the same after we flip it over its main diagonal.
The entry in row $i$, column $j$ equals the entry in row $j$, column $i$.

### L2 human

Only the entries on and above the diagonal are free; the others are copies.
So the symmetric $n \times n$ matrices over a field form a space of dimension $n(n+1)/2$.
