---
tag: ~3de2cc1b
kind: concept
name: Gauss–Jordan elimination
msc: [15A06, 65F05]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: lead section
---

## Summary

Gauss–Jordan elimination is the variant of [[Gaussian elimination|~402766e6]] that continues until the matrix is in [[reduced row echelon form|~ca88f169]].
After the forward phase gives a row echelon form, it scales each pivot row to make the [[pivot|~a3760fc0]] equal to $1$.
Then it adds multiples of each pivot row to the rows above it, to make every other entry in each pivot column zero.
Applied to the [[augmented matrix|~77d11eff]] of a system, the result shows the solutions directly, with no [[back substitution|~a2f0b72a]].

## Remarks

The result of Gauss–Jordan elimination does not depend on the choices in the algorithm.
The reason is that the reduced row echelon form of a matrix is unique.
Applied to $[A \mid I]$ for an invertible matrix $A$, it gives $[I \mid A^{-1}]$, see [[computing the inverse by row reduction|~74e15f5d]].

## Explanations

### L1 human

Gauss–Jordan elimination cleans up the staircase matrix that Gaussian elimination produces.
It makes every pivot equal to $1$ and clears the entries above the pivots too.
Then each equation names one basic unknown in terms of the free unknowns.
