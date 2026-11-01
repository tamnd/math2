---
tag: AB3S6MHJ8X
kind: concept
name: Condition number
msc: [15A12, 65F35]
sources:
  - url: https://en.wikipedia.org/wiki/Condition_number
same_as:
  wikidata: Q1147936
  wikipedia: Condition number
---

## Summary

A condition number measures how much the output of a problem can change, relative to the size of a small relative change in its input.
For an [[invertible matrix|0EB9N0S33C]] $A$ and a [[matrix norm|54T6Y6DSY4]], it is $\kappa(A) = \norm{A} \norm{A^{-1}}$.
It bounds the relative error in the solution of $Ax = b$ caused by a relative error in $b$.
A problem with a large condition number is ill-conditioned: rounding errors in the data can be strongly amplified, whatever algorithm is used.

## Explanations

### L1 human

Some problems are sensitive: a tiny change in the data gives a big change in the answer.
The condition number puts a number on this sensitivity.
For a linear system $Ax = b$, a condition number of $1000$ means that a $0.1\%$ error in $b$ can cause up to a $100\%$ error in $x$.
For example, the diagonal matrix with entries $1$ and $0.001$ has condition number $1000$ in the Euclidean norm.
