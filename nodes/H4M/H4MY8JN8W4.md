---
tag: H4MY8JN8W4
kind: concept
name: Preservation of limits
msc: [18A35]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_(category_theory)
---

## Summary

A [[functor|28NQ0KRHD3]] preserves limits when it sends every limit cone to a limit cone.
Such a functor is also called continuous.
Forgetful functors from algebraic categories to sets preserve limits, and right adjoint functors always do.
Preservation of limits is the main condition in the adjoint functor theorems.

## Explanations

### L1 human

A limit is built from a diagram, like a product or a set of solutions.
A functor preserves it when doing the construction first and then applying the functor gives the same as applying the functor first.
For example, the underlying set of a product of two groups is the product of the underlying sets.
So the forgetful functor from groups to sets preserves products.
It does not preserve coproducts, because the free product of two groups is much bigger than the disjoint union of the sets.
