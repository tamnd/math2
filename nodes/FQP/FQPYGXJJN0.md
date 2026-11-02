---
tag: FQPYGXJJN0
kind: concept
name: q-difference equation
msc: [39A13, 05A30]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_calculus
---

## Summary

A $q$-difference equation relates the values of an unknown function at the points $x, qx, q^2 x, \dots$, where $q \ne 0, 1$ is a fixed number.
It is a difference equation in which the shift $x \mapsto x + 1$ is replaced by the dilation $x \mapsto qx$.
Equivalently, it can be written with the [[q-derivative|PMJT3FZE0Y]] in place of the ordinary derivative.
Such equations govern $q$-analogs of special functions, such as basic hypergeometric series, and they tend formally to differential equations as $q \to 1$.

## Explanations

### L1 human

An ordinary difference equation looks at a function at $x$ and at $x + 1$.
A $q$-difference equation looks at $x$ and at $qx$, a point a fixed factor away.
The simplest one is $y(qx) = y(x)$.
For $q = 2$, any function of $\log_2 x$ that has period $1$ solves it, for example $\cos(2\pi \log_2 x)$ for $x > 0$.
