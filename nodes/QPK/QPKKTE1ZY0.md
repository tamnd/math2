---
tag: QPKKTE1ZY0
kind: concept
name: Interval arithmetic
msc: [65G30, 65G40]
sources:
  - url: https://en.wikipedia.org/wiki/Interval_arithmetic
same_as:
  wikidata: Q1671453
  wikipedia: Interval arithmetic
---

## Summary

Interval arithmetic computes with closed bounded [[intervals|0Q1D85B8G6]] of real numbers instead of single numbers.
The result of an operation on two intervals is the smallest interval that contains every result of the operation on numbers taken from them.
When a computer rounds the lower end down and the upper end up, the computed interval is sure to contain the exact answer.
This gives rigorous error bounds and is the base of verified numerical computation and of some computer-assisted proofs.

## Explanations

### L1 human

If you know only that a length lies between $1$ and $2$ and another lies between $3$ and $5$, then their sum lies between $4$ and $7$.
Interval arithmetic makes this kind of reasoning into a set of rules for adding, subtracting, multiplying and dividing ranges.
Each number with an uncertainty becomes an interval, and the final interval shows how large the uncertainty of the answer can be.
A catch is that the same quantity used twice is treated as two independent quantities, so the bounds can be wider than needed: $[0, 1] - [0, 1]$ is $[-1, 1]$, not $\set{0}$.
