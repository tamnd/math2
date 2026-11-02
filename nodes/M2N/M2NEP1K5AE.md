---
tag: M2NEP1K5AE
kind: concept
name: Compact operator
msc: [47B07]
specializes: [03TM135G0N]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_operator
same_as:
  wikidata: Q1780743
  wikipedia: Compact operator
---

## Summary

A compact operator is a linear map between Banach spaces that sends bounded sets to relatively compact sets.
Compact operators are the operators closest to finite-dimensional linear algebra: their nonzero spectrum consists of eigenvalues of finite multiplicity, which can accumulate only at $0$.
They include the [[finite-rank operators|Z8FABSYQTS]] and their norm limits, and integral operators with continuous kernels.
They are the setting of the Fredholm alternative and of the spectral theorem for compact self-adjoint operators.

## Explanations

### L1 human

A compact operator squeezes the unit ball, which in infinite dimensions is very large, into a set that is almost finite-dimensional.
Take the operator on sequences that multiplies the $n$-th entry by $1/n$.
It flattens the directions far out in the sequence more and more.
So, up to any given accuracy, the image of the unit ball is small in all but finitely many directions.
The identity on an infinite-dimensional space is not compact: it leaves the unit ball as large as it was.
