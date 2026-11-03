---
tag: PAPN0JNEKN
kind: concept
name: Conic optimization
msc: [90C25, 90C22, 90C46]
specializes: [1W1BXJN9ER]
sources:
  - url: https://en.wikipedia.org/wiki/Conic_optimization
same_as:
  wikidata: Q2654791
  wikipedia: Conic optimization
---

## Summary

Conic optimization is the minimisation of a linear function over the intersection of an affine subspace with a closed [[convex cone|6VE4KA12VD]].
It is a special case of [[convex optimization|1W1BXJN9ER]] that still contains most convex problems met in practice.
The nonnegative orthant gives [[linear programming|VNMXB0J2KA]], and products of Lorentz cones give [[second-order cone programming|H80KQPNN9B]].
The cone of positive semidefinite matrices gives [[semidefinite programming|2RTN2X4R2N]].
Its duality theory uses the [[dual cone|QFY1JR1TK4]], and [[interior-point methods|M7HYT44ZJA]] solve these problems efficiently.

## Explanations

### L1 human

A linear program asks that each variable be nonnegative.
Conic optimization replaces "nonnegative" by "lies in a given cone", a set closed under adding vectors and scaling by nonnegative numbers.
The objective and the equations stay linear, so all the nonlinearity sits in the cone.
For example, the cone $\set{(x, y, z) : z \ge \sqrt{x^2 + y^2}}$, an ice-cream cone, lets one write bounds on Euclidean lengths.
