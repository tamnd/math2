---
tag: VSD67A49XC
kind: concept
name: Totally unimodular matrix
msc: [15B36, 90C10, 90C27]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Unimodular_matrix
    locator: Total unimodularity
---

## Summary

A totally unimodular matrix is an integer matrix in which every square submatrix has determinant $0$, $1$ or $-1$.
In particular every entry is $0$, $1$ or $-1$.
A linear program whose constraint matrix is totally unimodular and whose right-hand side is integral has integral vertices.
This explains why many problems on graphs, such as bipartite matching and network flows, can be solved exactly by linear programming.

## Explanations

### L1 human

Linear programs are easy to solve, but problems that ask for whole-number answers are usually hard.
For some special constraint matrices, the two coincide: whenever the right-hand side is whole-number and the linear program has a best solution, it has a best solution in whole numbers.
Totally unimodular matrices are exactly such special matrices: every square piece of them has determinant $0$, $1$ or $-1$.
The incidence matrix of a bipartite graph, with a row for each vertex and a column for each edge, is a standard example.
