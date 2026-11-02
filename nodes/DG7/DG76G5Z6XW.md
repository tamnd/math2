---
tag: DG76G5Z6XW
kind: concept
name: Integral of a non-negative function
msc: [28A25]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_integral
---

## Summary

The integral of a non-negative measurable function on a measure space is the supremum of the integrals of the simple functions that lie below it.
It always exists, as a number in $[0, \infty]$.
It is the first step of the Lebesgue integral, and the monotone convergence theorem and Fatou's lemma are statements about it.

## Explanations

### L1 human

For a function that takes finitely many values, the integral is easy: add up each value times the measure of the set where it is taken.
A general non-negative function is approached from below by such staircase functions.
The integral is the best value that these staircases reach.
For example, the function $f(x) = x$ on $[0, 1]$ has staircases below it with integrals as close to $1/2$ as one wants, and its integral is $1/2$.
The value $\infty$ is allowed, as for the constant function $1$ on the whole real line.
