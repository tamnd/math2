---
tag: PMJT3FZE0Y
kind: concept
name: q-derivative
msc: [05A30, 39A13]
sources:
  - url: https://en.wikipedia.org/wiki/Q-derivative
same_as:
  wikidata: Q7265300
  wikipedia: Q-derivative
---

## Summary

The $q$-derivative of a function $f$ is the quotient $\frac{f(qx) - f(x)}{qx - x}$, where $q \ne 1$ is a fixed number.
It replaces the limit in the ordinary [[derivative|0V1EJCT8G6]] by a comparison of $f$ at $x$ and at the scaled point $qx$.
It is the basic operator of $q$-calculus and of the theory of [[q-analogs|GFSDMJHHVA]], and it tends to the ordinary derivative as $q \to 1$.
It is also called the Jackson derivative.

## Explanations

### L1 human

The ordinary derivative compares $f(x)$ with $f(x + h)$ for tiny $h$ and takes a limit.
The $q$-derivative compares $f(x)$ with $f(qx)$, a point that is a fixed factor away, and takes no limit at all.
For $f(x) = x^2$ it gives $\frac{q^2 x^2 - x^2}{qx - x} = (1 + q) x$, which tends to the usual $2x$ as $q \to 1$.
The number $1 + q$ in place of $2$ is a first example of a $q$-number.
