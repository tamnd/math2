---
tag: SAT7ST5WP7
kind: concept
name: Quaternionic analysis
msc: [30G35]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternionic_analysis
same_as:
  wikidata: Q7269567
  wikipedia: Quaternionic analysis
---

## Summary

Quaternionic analysis studies functions of a quaternion variable with quaternion values, by analogy with complex analysis.
The naive analogue of the complex derivative is too restrictive.
So the central class is that of Fueter regular functions, the solutions of a quaternionic Cauchy–Riemann equation.
These functions have an integral formula like Cauchy's and are harmonic in $\R^4$.
A wider theory, [[Clifford analysis|DKVSAZQWF7]], extends these ideas to all dimensions.

## Explanations

### L1 human

The quaternions extend the complex numbers with three imaginary units $i, j, k$, but their multiplication is not commutative.
In complex analysis, a function is holomorphic when it has a derivative $\lim_{h \to 0} (f(z + h) - f(z))/h$.
For quaternions this limit exists only for affine functions, so this road leads nowhere.
Instead one copies the Cauchy–Riemann equations: one adds the four partial derivatives, each multiplied by $1, i, j$ or $k$, and asks the sum to be $0$.
Surprisingly, even $f(q) = q$ fails this test, while some functions of the real coordinates pass it.
