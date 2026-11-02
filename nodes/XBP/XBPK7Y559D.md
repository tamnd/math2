---
tag: XBPK7Y559D
kind: concept
name: Incomplete LU factorization
msc: [65F08, 65F50, 65F10]
sources:
  - url: https://en.wikipedia.org/wiki/Incomplete_LU_factorization
same_as:
  wikidata: Q1654069
  wikipedia: Incomplete LU factorization
---

## Summary

An incomplete LU factorization of a sparse square matrix $A$ is a pair of sparse triangular matrices $L$ and $U$ with $L U \approx A$.
It is computed like the [[LU decomposition|0RKG5YW66Y]], but entries outside a prescribed sparsity pattern are dropped.
It is one of the most common [[preconditioners|KE98SW3SBD]] for Krylov methods on nonsymmetric systems.

## Explanations

### L1 human

Exact elimination on a sparse matrix creates many new nonzeros, called fill.
The incomplete factorization throws away the fill that falls outside allowed positions.
The factors stay as sparse as $A$, or nearly so, and $L U$ is close to $A$.
Solving with $L$ and then $U$ is cheap, so $L U$ acts as an easy approximate inverse inside an iterative solver.
