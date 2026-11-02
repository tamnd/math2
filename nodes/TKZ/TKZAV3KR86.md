---
tag: TKZAV3KR86
kind: concept
name: Function of exponential order
msc: [44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Summary

A function $f$ on $[0, \infty)$ is of exponential order when it grows no faster than some exponential $M e^{at}$ for large $t$.
This is the usual sufficient condition for the [[Laplace transform|0V49JEZW06]] of $f$ to exist.
For a piecewise continuous $f$ of exponential order $a$, the integral $\int_0^\infty f(t) e^{-st}\, dt$ converges absolutely for $\operatorname{Re} s > a$.
Most functions met in linear differential equations, such as polynomials, exponentials, sines and cosines, are of exponential order.

## Explanations

### L1 human

The factor $e^{-st}$ in the Laplace transform decays exponentially.
It can tame $f$ only if $f$ itself grows at most exponentially.
For example, $t^3$ is of exponential order, because $t^3 \le 6 e^t$ for all $t \ge 0$.
The function $e^{t^2}$ is not: it eventually beats every $e^{at}$, and indeed it has no Laplace transform.
