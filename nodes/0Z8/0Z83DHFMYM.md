---
tag: 0Z83DHFMYM
kind: concept
name: Computing the inverse by row reduction
msc: [15A09, 65F05]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: Finding the inverse of a matrix
---

## Summary

Row reduction computes the inverse of a square matrix, or shows that no inverse exists.
Let $A$ be an $n \times n$ matrix over a field $F$, and form the $n \times 2n$ [[augmented matrix|0T6MWGZSXA]] $[A \mid I_n]$.
Apply [[Gauss–Jordan elimination|098D6FQN3N]] to it.
If the left block becomes $I_n$, then the result is $[I_n \mid A^{-1}]$, and the right block is the inverse.
If the left block gets a zero row, then $A$ is not [[invertible|0EB9N0S33C]].

## Remarks

The method works because each row operation is left multiplication by an [[elementary matrix|01REXW3WWE]].
If $E_k \cdots E_1 A = I_n$, then $E_k \cdots E_1 = A^{-1}$, and the same product changes $I_n$ into $A^{-1}$.
For $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, the method gives $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.

## Explanations

### L1 human

We write the identity matrix next to $A$ and row reduce the whole wide matrix.
When the left half becomes the identity, the right half has become $A^{-1}$.
The same row operations that turn $A$ into $I$ turn $I$ into $A^{-1}$.
