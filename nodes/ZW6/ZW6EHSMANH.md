---
tag: ZW6EHSMANH
kind: concept
name: Statistical convergence
msc: [40A35, "11B05"]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_density
---

## Summary

A sequence converges statistically to $L$ when, for every $\varepsilon > 0$, the indices $n$ with $\abs{x_n - L} \ge \varepsilon$ form a set of [[natural density|RVG9Z8NYA6]] zero.
So the sequence may stray from $L$ infinitely often, but only on a sparse set of indices.
Every convergent sequence converges statistically to its limit, but not conversely.
For bounded sequences, statistical convergence to $L$ is equivalent to [[strong Cesàro summability|750MCA763X]] to $L$ with exponent $1$.

## Explanations

### L1 human

Ordinary convergence allows only finitely many terms to be far from the limit.
Statistical convergence allows infinitely many, as long as they become rarer and rarer, so that their proportion among the first $n$ terms tends to $0$.
For example, the sequence that is $1$ at perfect squares and $0$ elsewhere converges statistically to $0$, since there are only about $\sqrt{n}$ squares up to $n$.
It does not converge in the usual sense, because the ones never stop.
