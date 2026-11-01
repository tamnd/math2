---
tag: H4MQD841BR
kind: concept
name: Power iteration
msc: [65F15, 15A18]
sources:
  - url: https://en.wikipedia.org/wiki/Power_iteration
same_as:
  wikidata: Q1426504
  wikipedia: Power iteration
---

## Summary

Power iteration, or the power method, finds the [[eigenvalue|0BQAA2BK3Q]] of largest absolute value of a matrix and a corresponding [[eigenvector|0N6960W0BV]].
It multiplies a starting vector by the matrix again and again and rescales it.
It needs only matrix-vector products, so it works for very large sparse matrices, and it is the basis of the PageRank computation.
Its speed depends on the ratio between the two largest absolute values of the eigenvalues.

## Explanations

### L1 human

Applying a matrix stretches each eigenvector direction by its eigenvalue.
After many applications, the direction with the largest stretch wins over all others.
For $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $x_0 = (1, 0)$, the vectors $A x_0, A^2 x_0, A^3 x_0$ are $(2, 1)$, $(5, 4)$, $(14, 13)$.
They point closer and closer to $(1, 1)$, the eigenvector for the largest eigenvalue $3$.
