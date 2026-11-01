---
tag: JGACZYEEY7
kind: concept
name: Sparse matrix
msc: [65F50, 15B99]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Sparse_matrix
same_as:
  wikidata: Q1050404
  wikipedia: Sparse matrix
---

## Summary

A sparse matrix is a matrix in which most entries are zero.
Such matrices are stored by listing only the nonzero entries with their positions, which saves memory.
Algorithms that skip the zeros can be much faster than algorithms for general, dense matrices.
Large sparse matrices arise from networks, from discretised differential equations and from many problems in data science.

## Explanations

### L1 human

Think of a matrix that records which of a million people know each other.
Each person knows only a few hundred others, so almost all of the trillion entries are zero.
Storing all entries would be wasteful; it is enough to store, for each nonzero entry, its row, its column and its value.
The [[tridiagonal|DARX1KZRHZ]] and [[band|Z58FRZCF8P]] matrices are simple examples of sparse matrices.
