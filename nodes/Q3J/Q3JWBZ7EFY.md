---
tag: Q3JWBZ7EFY
kind: concept
name: Vandermonde matrix
msc: [15B99, 15A15, 41A05]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Vandermonde_matrix
same_as:
  wikidata: Q579544
  wikipedia: Vandermonde matrix
---

## Summary

A Vandermonde matrix has rows of the form $1, x, x^2, \dots, x^{n-1}$, one row for each of the numbers $x_1, \dots, x_m$.
Multiplying it by the coefficient vector of a polynomial gives the values of the polynomial at $x_1, \dots, x_m$.
Its determinant, the [[Vandermonde determinant|0P84B554AS]], is nonzero exactly when the $x_i$ are distinct.
This is why a polynomial of degree less than $n$ is fixed by its values at $n$ distinct points.

## Explanations

### L1 human

Take a few numbers, say $1, 2, 3$, and write each one's powers in a row: $1, x, x^2$.
This gives the square table $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 3 & 9 \end{pmatrix}$.
To find a parabola through three given points, one solves a linear system with this matrix.
Because the numbers are distinct, the matrix is invertible, so there is exactly one such parabola.
