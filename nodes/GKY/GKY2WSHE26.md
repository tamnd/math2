---
tag: GKY2WSHE26
kind: concept
name: Toeplitz matrix
msc: [15B05]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Toeplitz_matrix
same_as:
  wikidata: Q849428
  wikipedia: Toeplitz matrix
---

## Summary

A Toeplitz matrix is a matrix that is constant along each diagonal parallel to the main diagonal.
Its entry in row $i$ and column $j$ depends only on the difference $i - j$.
Toeplitz matrices describe discrete convolutions and stationary time series, and linear systems with them can be solved faster than general systems.
They are closely related to [[Hankel matrices|PQ1D8FQB3E]], which are constant along the anti-diagonals.

## Explanations

### L1 human

A Toeplitz matrix is fixed by its first row and its first column; every other entry copies the entry up and to the left of it.
For example, $\begin{pmatrix} a & b & c \\ d & a & b \\ e & d & a \end{pmatrix}$ is Toeplitz.
Such matrices come up whenever a rule acts the same way at every position, like a moving average over a list of numbers.
So an $n \times n$ Toeplitz matrix is described by only $2n - 1$ numbers instead of $n^2$.
