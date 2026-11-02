---
tag: 2RPE77ACER
kind: concept
name: Iterative method
msc: [65F10, 65H10]
sources:
  - url: https://en.wikipedia.org/wiki/Iterative_method
same_as:
  wikidata: Q2321565
  wikipedia: Iterative method
---

## Summary

An iterative method solves a problem by producing a sequence of approximate solutions, each computed from the previous ones, that converges to a solution.
It contrasts with a direct method, which gives the answer after a fixed finite number of steps.
Iterative methods are the standard tool for nonlinear equations and for very large sparse linear systems, where direct elimination costs too much.

## Explanations

### L1 human

Start with a guess, improve it by a fixed rule, and repeat until the guess is good enough.
[[Newton's method|07EXVNF9VP]] for $\sqrt{2}$ is an example: from $x_0 = 1$ the rule $x_{k+1} = (x_k + 2 / x_k) / 2$ gives $1.5$, then $1.41\overline{6}$, then $1.41421\ldots$.
Each step is cheap, and one stops when the error is below a tolerance.
The questions are whether the sequence converges and how fast.
