---
tag: DXX7GNY3HE
kind: concept
name: von Neumann regular ring
msc: ["16E50", 13C11]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_regular_ring
same_as:
  wikidata: Q2895315
  wikipedia: Von Neumann regular ring
---

## Summary

A von Neumann regular ring is a ring in which every element $a$ has a weak inverse $x$, with $a x a = a$.
Fields, division rings, matrix rings over division rings, products of fields and Boolean rings are examples.
John von Neumann introduced these rings in his work on continuous geometry.
In the commutative case they are exactly the reduced rings of Krull dimension $0$, and also the rings over which every module is flat.
The name is unrelated to regular local rings.

## Explanations

### L1 human

In a field every nonzero element has an inverse.
A von Neumann regular ring asks for less: each element $a$ has a partner $x$ that undoes $a$ "on its image", in the sense that $a x a = a$.
In the product $\Q \times \Q$ of two fields, the element $(2, 0)$ has no inverse, but $x = (\frac12, 0)$ satisfies $a x a = a$.
In the integers, $2 x 2 = 2$ would need $4x = 1$, which has no solution, so $\Z$ is not von Neumann regular.
