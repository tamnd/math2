---
tag: JPQCCFCY8X
kind: concept
name: Nonnegative matrix
msc: [15B48]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Nonnegative_matrix
same_as:
  wikidata: Q6961560
  wikipedia: Nonnegative matrix
---

## Summary

A nonnegative matrix is a real matrix whose entries are all greater than or equal to zero.
Transition matrices of [[Markov chains|0G48PYM96Q]], adjacency matrices of graphs and input-output tables in economics are nonnegative.
The [[Perron–Frobenius theorem|62NS7PV1M9]] describes the largest eigenvalue of such a matrix and its eigenvector.

## Explanations

### L1 human

A nonnegative matrix is a table of numbers with no negative entry.
Such tables often count things or give probabilities, and these are never negative.
For example, $\begin{pmatrix} 0 & 2 \\ 1 & 3 \end{pmatrix}$ is nonnegative, while $\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ is not.
Do not confuse this with a positive semidefinite matrix: the condition is on the entries, not on the eigenvalues.
