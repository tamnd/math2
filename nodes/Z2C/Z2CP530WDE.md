---
tag: Z2CP530WDE
kind: concept
name: Trace class operator
msc: [47B10]
specializes: [153N5DW55Z]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_class
same_as:
  wikidata: Q977297
  wikipedia: Trace class
---

## Summary

A trace class operator is a bounded operator on a Hilbert space whose singular values have a finite sum.
For such operators the trace $\sum_i \ip{T e_i}{e_i}$ converges absolutely and does not depend on the orthonormal basis, so the trace of matrices extends to them.
Trace class operators are central in the theory of Fredholm determinants.
In quantum mechanics, density matrices are positive trace class operators of trace $1$.

## Explanations

### L1 human

For a matrix, the trace is the sum of the diagonal entries.
For an operator on an infinite-dimensional space, this sum may diverge or depend on the chosen basis.
Trace class operators are those small enough that the sum always converges and gives the same answer in every basis.
For example, the operator on square-summable sequences that multiplies the $n$-th coordinate by $1/n^2$ is trace class, with trace $\sum 1/n^2 = \pi^2 / 6$.
