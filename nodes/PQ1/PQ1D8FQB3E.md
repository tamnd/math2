---
tag: PQ1D8FQB3E
kind: concept
name: Hankel matrix
msc: [15B05]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_matrix
same_as:
  wikidata: Q1575637
  wikipedia: Hankel matrix
---

## Summary

A Hankel matrix is a matrix that is constant along each anti-diagonal, the lines that go from lower left to upper right.
Its entry in row $i$ and column $j$ depends only on the sum $i + j$.
Hankel matrices appear for moment sequences, for the realisation of linear systems from their impulse responses, and in the theory of orthogonal polynomials.
Reversing the order of the rows turns a square Hankel matrix into a [[Toeplitz matrix|GKY2WSHE26]].

## Explanations

### L1 human

Take a sequence of numbers $h_2, h_3, h_4, \dots$ and write it into a square so that it runs along the anti-diagonals.
For example, $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{pmatrix}$ is Hankel, built from $1, 2, 3, 4, 5$.
Each row is the row above it shifted one step to the left, with a new number at the end.
A square Hankel matrix is always symmetric.
