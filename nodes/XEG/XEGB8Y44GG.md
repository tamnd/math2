---
tag: XEGB8Y44GG
kind: concept
name: Asymptotic scale
msc: [41A60, "30E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_expansion
---

## Summary

An asymptotic scale, also called an asymptotic sequence, is a sequence of functions $\varphi_0, \varphi_1, \dots$ near a point $x_0$.
Each function in it is negligible compared with the one before it.
It is the system of reference functions in which [[asymptotic expansions|BJQTEPEZ9G]] are written.
The most common scale is the powers $x^{-n}$ as $x \to \infty$, but scales with logarithms, fractional powers or exponentials are also needed.
Fixing a scale makes the coefficients of an expansion unique.

## Explanations

### L1 human

An asymptotic scale is a ladder of functions, each one much smaller than the previous one when $x$ is close to the limit point.
It plays the role that the powers $1, x, x^2, \dots$ play in a Taylor series.
An approximation is then described by saying how many steps of the ladder it gets right.
For example, $1, \frac1x, \frac{1}{x^2}, \dots$ is a scale as $x \to \infty$, because $\frac{1/x^{n+1}}{1/x^n} = \frac1x \to 0$.
