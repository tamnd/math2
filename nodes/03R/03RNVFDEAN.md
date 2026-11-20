---
tag: 03RNVFDEAN
kind: definition
name: Skew-symmetric matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: 0PBY4E9GQF
uses: [0W809K6AW0, 0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: lead section
inventory: [2FP1241FAJ]
---

## Definition

Let $R$ be a ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
The matrix $A$ is *skew-symmetric* when $A^{\mathsf{T}} = -A$, where $A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]] of $A$.
Equivalently, $a_{ji} = -a_{ij}$ for all $i$ and $j$.

## Notation

- Other names are *antisymmetric* and *skew*.
- Mathlib has no separate name for this property. The condition is written `Aᵀ = -A`.

## Remarks

- If $2$ is not a zero divisor in $R$, for example over $\mathbb{R}$, then each diagonal entry of a skew-symmetric matrix is $0$.
- When $2$ is invertible in $R$, each square matrix is the sum of a [[symmetric matrix|0VR671PHE5]] and a skew-symmetric matrix; see [[this theorem|~3a63c44b]].
- The matrix $\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ is skew-symmetric.

## Explanations

### L1 human

In a skew-symmetric matrix, the entry across the diagonal is the negative of the entry here.
Over the real numbers this forces zeros on the diagonal, because only $0$ equals its own negative.

### L2 human

Only the entries above the diagonal are free when $2$ is invertible.
The entries below are their negatives, and the diagonal is $0$.
