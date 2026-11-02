---
tag: TDKKST5AWA
kind: concept
name: Direct and inverse theorems of approximation
msc: [41A25, 41A27, 42A10]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson%27s_inequality
---

## Summary

Direct and inverse theorems are the two halves of the link between the smoothness of a function and how fast it can be approximated.
A direct theorem, of Jackson type, says that smooth functions have small errors of best approximation.
An inverse theorem, of Bernstein type, says that small errors of best approximation force smoothness.
Together they often characterise a smoothness class exactly by the rate of approximation.

## Explanations

### L1 human

A smooth function is easy to imitate with polynomials of low degree, and a rough one is hard.
Direct theorems turn "smooth" into "the error goes down fast as the degree grows".
Inverse theorems go back the other way.
For periodic functions and $0 < \alpha < 1$, the error of the best trigonometric polynomial of degree $n$ is of order $n^{-\alpha}$ exactly when the function is Hölder continuous with exponent $\alpha$.
