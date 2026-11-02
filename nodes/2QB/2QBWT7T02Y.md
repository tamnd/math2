---
tag: 2QBWT7T02Y
kind: concept
name: Abel function
msc: [39B12, 26A18]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_equation
---

## Summary

An Abel function of a map $f$ is a solution $\alpha$ of the [[Abel equation|68SHB7Z721]] $\alpha(f(x)) = \alpha(x) + 1$.
It is a coordinate in which one step of $f$ becomes a shift by $1$.
When $\alpha$ is injective, it defines a whole family of iterates $f^t = \alpha^{-1} \circ (\alpha + t)$, one for each real $t$ in a suitable range.
Abel functions are the standard tool for fractional iteration, for example in the construction of iterates of the exponential function.

## Explanations

### L1 human

An Abel function is a clock that ticks once each time the map $f$ is applied.
For the map $f(x) = x + 3$ on the real line, the function $\alpha(x) = x/3$ is such a clock.
Reading the clock, one can run the map for any amount of time: running for time $t$ moves $x$ to $x + 3t$.
For more complicated maps the clock is harder to find, but the idea is the same.
