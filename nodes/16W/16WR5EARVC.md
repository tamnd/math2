---
tag: 16WR5EARVC
kind: concept
name: Bessel–Clifford function
msc: [33C10]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel%E2%80%93Clifford_function
same_as:
  wikidata: Q4896413
  wikipedia: Bessel–Clifford function
---

## Summary

The Bessel–Clifford function $\mathcal{C}_n$ is an entire function of one variable.
It is the [[Bessel function of the first kind|CZCMRDWDYW]] without its power factor and its square root.
It satisfies $J_n(x) = \left( \frac{x}{2} \right)^n \mathcal{C}_n\left( -\frac{x^2}{4} \right)$.
Its power series has the simple coefficients $\frac{1}{k!\, \Gamma(n + k + 1)}$, which makes it convenient in computation and in algebraic arguments.

## Explanations

### L1 human

Bessel functions mix a power $x^n$ with a series in $x^2$.
The Bessel–Clifford function removes the power and replaces $x^2$ by a new variable, leaving a clean power series.
For $n = 0$ it is $\mathcal{C}_0(z) = \sum_{k \ge 0} \frac{z^k}{(k!)^2} = 1 + z + \frac{z^2}{4} + \cdots$.
From it one recovers $J_0(x) = \mathcal{C}_0\left( -\frac{x^2}{4} \right)$.
