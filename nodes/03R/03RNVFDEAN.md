---
tag: 03RNVFDEAN
kind: definition
name: Skew-symmetric matrix
msc: [15A99]
defines: 0PBY4E9GQF
uses: [0W809K6AW0, 0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: lead section
---

## Definition

Let $R$ be a ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The matrix $A$ is *skew-symmetric* when $A^T = -A$, where $A^T$ is the [[transpose|09DXWYRD43]] of $A$.
Equivalently, $a_{ji} = -a_{ij}$ for all $i$ and $j$.

## Remarks

If $2$ is invertible in $R$, for example over $\R$, then each diagonal entry of a skew-symmetric matrix is $0$.
Over a field of characteristic not $2$, each square matrix is the sum of a [[symmetric matrix|0VR671PHE5]] and a skew-symmetric matrix: $A = \tfrac12 (A + A^T) + \tfrac12 (A - A^T)$.
A real skew-symmetric matrix of odd order has determinant $0$.
The matrix $\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ is skew-symmetric.

## Explanations

### L1 human

In a skew-symmetric matrix, the entry across the diagonal is the negative of the entry here.
Over the real numbers this forces zeros on the diagonal, because only $0$ equals its own negative.
These matrices describe infinitesimal rotations.
