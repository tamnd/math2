---
tag: VTJV7JVJEA
kind: concept
name: Schröder's equation
msc: [39B12, 30D05, 39B32]
specializes: [BCGBQ3HK26]
sources:
  - url: https://en.wikipedia.org/wiki/Schr%C3%B6der%27s_equation
same_as:
  wikidata: Q7432911
  wikipedia: Schröder's equation
---

## Summary

Schröder's equation asks for a function $\Psi$ with $\Psi(f(x)) = \lambda \Psi(x)$, where the map $f$ and the constant $\lambda$ are given.
A solution is a change of coordinates in which $f$ becomes multiplication by $\lambda$.
It is one of the basic [[iterative functional equations|BCGBQ3HK26]]: once it is solved, every [[iterate|AYVTR2ES5B]] of $f$ has the closed form $f^n = \Psi^{-1} \circ (\lambda^n \Psi)$.
Near a [[fixed point|R6QVS6P21N]] of a holomorphic map, the natural choice of $\lambda$ is the derivative of $f$ at that point.

## Explanations

### L1 human

Iterating a map is often hard, but iterating multiplication by a number is easy: $n$ steps multiply by $\lambda^n$.
Schröder's equation looks for a new coordinate in which the given map is just such a multiplication.
For example, take $f(x) = x^2 + 2x$ on $x > -1$ and $\Psi(x) = \log(1 + x)$.
Then $\Psi(f(x)) = \log\big((1 + x)^2\big) = 2 \Psi(x)$, so in the coordinate $\Psi$ the map $f$ doubles.
This gives at once $f^n(x) = (1 + x)^{2^n} - 1$.
