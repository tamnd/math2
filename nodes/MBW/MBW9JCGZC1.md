---
tag: MBW9JCGZC1
kind: concept
name: Weak convergence of measures
msc: [60B10, 28A33]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_measures
---

## Summary

A sequence of [[probability measures|059TJN0NZ1]] on a [[metric space|0VKD1TP7F3]] converges weakly when the integrals of every bounded continuous function converge.
It is the mode of convergence behind [[convergence in distribution|0SRYJGXKR4]] of random variables and the central limit theorem.
Mass may move a little in the limit, so the measure of a fixed set need not converge.

## Explanations

### L1 human

Two measures are close in this sense if they look alike to every smooth test, even if they put mass on slightly different points.
Picture a point mass at $1/n$ sliding towards $0$.
For every continuous bounded $f$, the value $f(1/n)$ tends to $f(0)$, so these point masses converge weakly to the point mass at $0$.
Yet the set $\set{0}$ has mass $0$ for every $n$ and mass $1$ in the limit.
Weak convergence only sees the overall shape, not exact sets.
