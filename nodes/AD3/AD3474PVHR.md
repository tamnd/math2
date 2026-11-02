---
tag: AD3474PVHR
kind: concept
name: Polynomially convex set
msc: ["32E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Summary

A compact set $K \subseteq \C^n$ is polynomially convex if every point outside $K$ can be separated from $K$ by a polynomial.
This means that some polynomial is larger in absolute value at the point than everywhere on $K$.
They are the natural sets for polynomial approximation.
By the [[Oka–Weil theorem|7AWZJNQGT2]], every function holomorphic near such a set is a uniform limit of polynomials on it.
In $\C$ they are the compact sets with connected complement.
For $n \ge 2$ the condition is much subtler, and it is not determined by the topology of $K$ alone.

## Explanations

### L1 human

The hull of a compact set $K$ collects the points where no polynomial beats its maximum over $K$.
The set is polynomially convex if the hull adds nothing.
A closed disc in $\C$ is polynomially convex, but a circle is not: by the maximum principle, its hull is the whole closed disc.
Every compact convex set in $\C^n$ is polynomially convex, and so is every compact subset of $\R^n \subseteq \C^n$.
