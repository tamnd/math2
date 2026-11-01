---
tag: DARX1KZRHZ
kind: concept
name: Tridiagonal matrix
msc: [15B99, 65F05]
specializes: [Z58FRZCF8P]
sources:
  - url: https://en.wikipedia.org/wiki/Tridiagonal_matrix
same_as:
  wikidata: Q1755277
  wikipedia: Tridiagonal matrix
---

## Summary

A tridiagonal matrix is a square matrix whose nonzero entries lie only on the main diagonal and on the two diagonals next to it.
It is a [[band matrix|Z58FRZCF8P]] of bandwidth one on each side, and it is both upper and lower [[Hessenberg|YCEEWJTX56]].
Linear systems with a tridiagonal matrix can be solved with a number of operations proportional to the size, not to its cube.
Such matrices arise from finite difference schemes, from three-term recurrences and from the reduction of symmetric matrices for eigenvalue computations.

## Explanations

### L1 human

Picture a square matrix where only a narrow strip of three diagonals is filled and everything else is zero.
For example, $\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$ is tridiagonal.
This one comes from approximating a second derivative at evenly spaced points: each point only talks to its two neighbours.
Because each unknown meets only its neighbours, elimination proceeds row by row without creating new nonzero entries.
