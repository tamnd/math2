---
tag: 5GN0RYRVBA
kind: concept
name: Totally positive matrix
msc: [15B48]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Totally_positive_matrix
same_as:
  wikidata: Q3893192
  wikipedia: Totally positive matrix
---

## Summary

A totally positive matrix is a real matrix all of whose [[minors|0BT9BYWVRY]] are positive.
When the minors are only required to be nonnegative, the matrix is called totally nonnegative.
Totally positive matrices have strong spectral properties: a square one has only positive, distinct eigenvalues.
They occur in approximation theory, in probability, in combinatorics and in the study of oscillating mechanical systems.

## Explanations

### L1 human

Every entry of a matrix is a $1 \times 1$ minor, and determinants of larger square pieces are larger minors.
A totally positive matrix is one where every such determinant, of every size and position, is positive.
For example, $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ has positive entries and determinant $1$, so it is totally positive.
The condition is much stronger than having positive entries: $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ has positive entries but determinant $-3$.
