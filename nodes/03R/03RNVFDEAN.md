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

We define the square matrices whose transpose is their negative.
Let $R$ be a ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
The matrix $A$ is *skew-symmetric* when $A^{\mathsf{T}} = -A$, where $A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]] of $A$; equivalently, $a_{ji} = -a_{ij}$ for all $i, j \in \{1, \dots, n\}$.

## Notation

Other names are *antisymmetric* and *skew*.
The condition is also written $A^t = -A$, ${}^t\!A = -A$ or $A' = -A$, following the notation for the transpose.
In Mathlib the condition is written `Aᵀ = -A`.

## Remarks

For $i = j$ the condition reads $a_{ii} = -a_{ii}$, that is, $2 a_{ii} = 0$.
So if $2$ is not a zero divisor in $R$, for example over $\mathbb{R}$ or over any field of characteristic not $2$, every diagonal entry of a skew-symmetric matrix is $0$.
In characteristic $2$ this fails: there $-1 = 1$, skew-symmetric means symmetric, and the identity matrix is skew-symmetric.

For example, $\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ is skew-symmetric, while the real matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is not, because $a_{21} = 1$ but $-a_{12} = -1$; see [[this example|8YRP1P4XRX]].
When $2$ is invertible in a commutative ring $R$, every square matrix is the sum of a [[symmetric matrix|0VR671PHE5]] and a skew-symmetric matrix in exactly one way, by [[this theorem|K284W6D15Z]].
The concept page on [[skew-symmetric matrices|0PBY4E9GQF]] has more examples and properties.

## Explanations

### L1 human

In a skew-symmetric matrix, the number in row $i$, column $j$ is the negative of the number in row $j$, column $i$.
Over the real numbers this forces zeros on the diagonal, because the only number equal to its own negative is $0$.

### L2 human

To check that a real matrix is skew-symmetric, first check that the diagonal is $0$, then compare each entry above the diagonal with its mirror entry below it.
In $\begin{pmatrix} 0 & 1 & -4 \\ -1 & 0 & 2 \\ 4 & -2 & 0 \end{pmatrix}$ the three pairs are $(1, -1)$, $(-4, 4)$ and $(2, -2)$, so the matrix is skew-symmetric.
Over a field of characteristic not $2$ only the $n(n-1)/2$ entries above the diagonal are free, which is $3$ for $n = 3$.
