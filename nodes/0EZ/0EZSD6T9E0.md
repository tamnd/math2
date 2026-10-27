---
tag: 0EZSD6T9E0
kind: definition
name: Lower triangular matrix
msc: [15A99]
defines: 00J3KZP8Y0
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: lead section
inventory: [3J3JZWN86P]
---

## Definition

Let $R$ be a ring and let $n \ge 0$ be an integer.
A [[square matrix|0JXZKX526R]] $L = (l_{ij})$ of order $n$ over $R$ is *lower triangular* when $l_{ij} = 0$ for all $i < j$.
It is *strictly lower triangular* when $l_{ij} = 0$ for all $i \le j$.

## Remarks

A matrix is lower triangular if and only if its [[transpose|09DXWYRD43]] is [[upper triangular|0N4XY7Z3NN]].
Sums and products of lower triangular matrices of the same order are lower triangular.
A system $Lx = b$ with $L$ lower triangular and invertible is solved by forward substitution.
In an [[LU decomposition|0RKG5YW66Y]], the factor $L$ is lower triangular.

## Explanations

### L1 human

A lower triangular matrix has zeros everywhere above its diagonal.
Its nonzero entries fill a triangle at the bottom left.
For example, $\begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix}$ is lower triangular.
