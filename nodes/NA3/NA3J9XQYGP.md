---
tag: NA3J9XQYGP
kind: concept
name: Lacunary series
msc: [42A55, 30B10]
specializes: [FZK2M8KGXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Lacunary_function
---

## Summary

A lacunary series is a [[trigonometric series|FZK2M8KGXQ]] or a [[power series|0D6KXBHKC0]] whose nonzero terms have frequencies that grow at least geometrically, such as $1, 2, 4, 8, \ldots$.
The large gaps make the terms behave almost like independent random variables.
As a result, lacunary series have rigid properties.
By the [[Hadamard gap theorem|DA8M8VZZHC]], a power series with such gaps cannot be continued past its circle of convergence.
A lacunary Fourier series of a bounded function converges absolutely.

## Explanations

### L1 human

Most of the terms of a lacunary series are zero, and the remaining ones are spaced further and further apart.
For example, $\sum_{k \ge 0} 2^{-k} \cos(2^k x)$ uses only the frequencies $1, 2, 4, 8, \ldots$.
Waves with such widely spaced frequencies hardly interfere with each other.
This makes lacunary series a source of both clean theorems and striking examples, such as the nowhere differentiable Weierstrass function.
