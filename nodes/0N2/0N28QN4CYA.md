---
tag: 0N28QN4CYA
kind: definition
name: Symmetric matrix
msc: [15A99, 15B57]
defines: 0VR671PHE5
uses: [0W809K6AW0, 0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: lead section
---

## Definition

Let $R$ be a ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The matrix $A$ is *symmetric* when $A^T = A$, where $A^T$ is the [[transpose|09DXWYRD43]] of $A$.
Equivalently, $a_{ij} = a_{ji}$ for all $i$ and $j$.

## Remarks

The matrix $\begin{pmatrix} 1 & 7 \\ 7 & 2 \end{pmatrix}$ is symmetric.
For each $m \times n$ matrix $B$ over a commutative ring, $B^T B$ and $B B^T$ are symmetric.
A real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors, by the [[spectral theorem|06J4PXRG22]].
Symmetric matrices represent [[symmetric bilinear forms|0AXZNE5XNH]] in a basis.

## Explanations

### L1 human

A symmetric matrix looks the same after we flip it over its main diagonal.
The entry in row $i$, column $j$ equals the entry in row $j$, column $i$.
Distance tables between cities are symmetric, because the distance from $A$ to $B$ equals the distance from $B$ to $A$.
