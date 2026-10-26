---
tag: ~0b0fbdd8
kind: definition
name: Lower triangular matrix
msc: [15A99]
defines: ~fa891bf6
uses: [~c4555ee3]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: lead section
---

## Definition

Let $R$ be a ring and let $n \ge 0$ be an integer.
A [[square matrix|~92565f6b]] $L = (l_{ij})$ of order $n$ over $R$ is *lower triangular* when $l_{ij} = 0$ for all $i < j$.
It is *strictly lower triangular* when $l_{ij} = 0$ for all $i \le j$.

## Remarks

A matrix is lower triangular if and only if its [[transpose|~5d7b1e24]] is [[upper triangular|~b3effb11]].
Sums and products of lower triangular matrices of the same order are lower triangular.
A system $Lx = b$ with $L$ lower triangular and invertible is solved by forward substitution.
In an [[LU decomposition|~5ee706d0]], the factor $L$ is lower triangular.

## Explanations

### L1 human

A lower triangular matrix has zeros everywhere above its diagonal.
Its nonzero entries fill a triangle at the bottom left.
For example, $\begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix}$ is lower triangular.
