---
tag: Z58FRZCF8P
kind: concept
name: Band matrix
msc: [15B99, 65F05]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Band_matrix
same_as:
  wikidata: Q806350
  wikipedia: Band matrix
---

## Summary

A band matrix is a matrix whose nonzero entries all lie in a band around the main diagonal.
The widths of the band below and above the diagonal are the lower and upper bandwidths.
[[Diagonal|044JNC7ZAA]], [[tridiagonal|DARX1KZRHZ]] and [[triangular|GTG8MJGDKC]] matrices are special band matrices.
Algorithms such as Gaussian elimination without pivoting keep the band, so systems with narrow band matrices are cheap to store and to solve.

## Explanations

### L1 human

Many problems link each unknown only to a few nearby unknowns, such as points on a line or a grid.
The matrix of such a problem has zeros everywhere except in a strip along the diagonal.
For example, a $5 \times 5$ matrix with nonzero entries only where the row and column numbers differ by at most $2$ is a band matrix of bandwidth $2$.
One only needs to store the strip, which saves memory and time when the matrix is large.
