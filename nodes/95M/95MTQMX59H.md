---
tag: 95MTQMX59H
kind: concept
name: Cauchy matrix
msc: [15B05, 15A15]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_matrix
same_as:
  wikidata: Q2915997
  wikipedia: Cauchy matrix
---

## Summary

A Cauchy matrix has entries $1/(x_i - y_j)$ for two lists of numbers $x_1, \dots, x_m$ and $y_1, \dots, y_n$ with $x_i \ne y_j$.
Its determinant has an explicit product formula, the Cauchy determinant.
As a result, a square Cauchy matrix is invertible when the $x_i$ are distinct and the $y_j$ are distinct.
The [[Hilbert matrix|2DTWB6F5TA]] is the best known Cauchy matrix.

## Explanations

### L1 human

Pick two lists of numbers that share no value.
Fill a table with one over the difference of a number from the first list and a number from the second.
For example, with $x = (1, 2)$ and $y = (0, -1)$ one gets $\begin{pmatrix} 1 & \tfrac12 \\ \tfrac12 & \tfrac13 \end{pmatrix}$.
Such tables appear in rational interpolation and in coding theory.
Their determinants factor completely, much like the Vandermonde determinant.
