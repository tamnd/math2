---
tag: Y2HXSEA2EE
kind: concept
name: Newton series
msc: [39A70, 41A58]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Summary

The Newton series of a function $f$ at a point $a$ is the series $\sum_{k \ge 0} \binom{x-a}{k} \Delta^k f(a)$, built from the forward differences of $f$ at $a$.
It is the difference analogue of the Taylor series, with generalized binomial coefficients in place of powers.
For a polynomial it is a finite sum equal to the polynomial; for other functions it may or may not converge to $f$.

## Explanations

### L1 human

A Taylor series rebuilds a function from its derivatives at one point.
A Newton series tries to rebuild it from its differences at one point, that is, from its values at $a, a+1, a+2, \dots$.
At the integers $x = a + n$ the series stops after $n + 1$ terms and gives exactly $f(a + n)$.
Between the integers it is an interpolation, which can work well or fail: the function $\sin(\pi x)$ vanishes at every integer, so its Newton series at $0$ is the zero series.
