---
tag: PS28BSAJKJ
kind: concept
name: Vector measure
msc: [28B05, 46G10]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_measure
same_as:
  wikidata: Q219308
  wikipedia: Vector measure
---

## Summary

A vector measure is an additive set function whose values lie in a [[Banach space|06GZ956657]] instead of the real or complex numbers.
The basic notion is finite additivity; countable additivity is an extra property, with convergence of series in norm.
Vector measures arise from spectral theory, where a self-adjoint operator gives a projection-valued measure, and from integration of vector-valued functions.
Their theory, including the Bartle–Dunford–Schwartz integral and Lyapunov's convexity theorem, studies how far scalar measure theory extends to infinite dimensions.

## Explanations

### L1 human

An ordinary measure gives each set a number.
A vector measure gives each set a vector, for example a function in some function space, and it adds up over disjoint sets.
A simple example sends a set $E \subseteq [0, 1]$ to its indicator function $\mathbf{1}_E$, viewed as an element of $L^1([0, 1])$.
New phenomena appear in infinite dimensions: the same rule with values in $L^\infty([0, 1])$ adds up over finitely many sets but not over countably many.
