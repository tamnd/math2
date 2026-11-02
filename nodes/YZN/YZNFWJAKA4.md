---
tag: YZNFWJAKA4
kind: concept
name: Periodicity equation
msc: [39B22]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_function
---

## Summary

The periodicity equation is the [[functional equation|SRAN4EKWS0]] $f(x + p) = f(x)$ for a fixed nonzero number $p$ and an unknown function $f$ on $\R$.
Its solutions are exactly the [[periodic functions|0ATF6Q0633]] with period $p$.
It is the simplest linear difference equation with constant coefficients, and many other equations reduce to it.
For example, the general solution of $g(x + 1) = g(x) + 1$ is $g(x) = x + f(x)$, with $f$ a solution of the periodicity equation for $p = 1$.

## Explanations

### L1 human

The equation says that the function repeats itself after a shift by $p$.
A solution is fixed by its values on one interval of length $p$, and these values can be chosen freely.
For example, $\sin x$ solves it for $p = 2\pi$.
The fractional part $x - \floor{x}$ solves it for $p = 1$.
