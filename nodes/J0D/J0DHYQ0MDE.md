---
tag: J0DHYQ0MDE
kind: concept
name: Lattice-ordered group
msc: ["06F15", "06F20"]
specializes: [KRDR04RQ7N]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_group
---

## Summary

A lattice-ordered group, or $\ell$-group, is an [[ordered group|KRDR04RQ7N]] whose order is a [[lattice|WH4SFAACAS]].
Any two elements have a least upper bound and a greatest lower bound, and multiplication preserves the order on both sides.
Every linearly ordered group is an $\ell$-group, and so are groups of real-valued functions with the pointwise order.
In an $\ell$-group each element splits into a positive part and a negative part, which gives an absolute value and a rich arithmetic of inequalities.

## Explanations

### L1 human

Think of real functions on a set, added pointwise and compared pointwise.
For two such functions $f$ and $g$ you can form the pointwise maximum and the pointwise minimum.
So the order is not total, but every pair of elements still has a best upper bound and a best lower bound.
A lattice-ordered group is a group with an order of this kind.
Each $f$ is the difference $f^+ - f^-$ of its positive part $\max(f, 0)$ and its negative part $\max(-f, 0)$.
