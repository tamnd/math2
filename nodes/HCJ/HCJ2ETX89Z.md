---
tag: HCJ2ETX89Z
kind: concept
name: Eigenvalue algorithm
msc: [65F15, 15A18]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalue_algorithm
same_as:
  wikidata: Q6766437
  wikipedia: Eigenvalue algorithm
---

## Summary

An eigenvalue algorithm is a numerical procedure that computes [[eigenvalues|0BQAA2BK3Q]], and often [[eigenvectors|0N6960W0BV]], of a square matrix.
By the [[Abel–Ruffini theorem|163A2WQQJX]], the eigenvalues of a general matrix of size at least $5$ cannot be written with radicals.
So such algorithms are iterative and produce approximations.
They are central in numerical linear algebra, with uses from vibration analysis to search engines and quantum chemistry.

## Explanations

### L1 human

An eigenvector of a matrix is a direction that the matrix only stretches, and the eigenvalue is the stretch factor.
For a $2 \times 2$ matrix one can find the eigenvalues by solving a quadratic equation, but for large matrices no formula exists.
Eigenvalue algorithms instead improve a guess step by step until it is accurate enough.
The simplest one, [[power iteration|H4MQD841BR]], multiplies a vector by the matrix again and again; the vector turns toward the direction of the largest stretch.
For example, repeatedly applying $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ to $(1, 1)$ gives $(2^k, 1)$, which points more and more along $(1, 0)$, the eigenvector for eigenvalue $2$.
