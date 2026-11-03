---
tag: AFXMKRC41H
kind: concept
name: Revised simplex method
msc: [90C05, 65K05, 90C49]
specializes: [MH272QHWPM]
sources:
  - url: https://en.wikipedia.org/wiki/Revised_simplex_method
same_as:
  wikidata: Q17085895
  wikipedia: Revised simplex method
---

## Summary

The revised simplex method is an implementation of the [[simplex algorithm|MH272QHWPM]] that does not update the whole tableau.
It keeps only the inverse, or a factorization, of the current basis matrix $A_B$.
From it, it computes the few quantities that each step needs.
For large sparse programs with many more columns than rows, this saves much work and memory, and it is the form used in practical solvers.

## Explanations

### L1 human

The textbook simplex method rewrites a whole table of numbers at every step.
Most of those numbers are never looked at.
The revised method keeps only the small square matrix of the current basis and computes the needed numbers on demand by solving linear systems.
For a program with $1000$ constraints and $100000$ variables, this means working with a $1000 \times 1000$ matrix instead of a $1000 \times 100000$ table.
