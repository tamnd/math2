---
tag: 5GVFZWMWC8
kind: concept
name: Algebraic K-theory
msc: ["16E20", 19D06]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
same_as:
  wikidata: Q2553675
  wikipedia: Algebraic K-theory
---

## Summary

Algebraic K-theory attaches to a [[ring|0B1261B5ED]] $R$ a sequence of abelian groups $K_n(R)$.
The group $K_0(R)$ is the [[Grothendieck group|5FDMY7PDYY]] of finitely generated [[projective modules|BFFA03GE3V]], and $K_1(R)$ is the abelianization of the infinite general linear group.
Daniel Quillen defined the higher groups by homotopy theory, for instance through the [[plus construction|XFGZFM8PC6]].
The groups encode deep arithmetic information, such as class groups, units and special values of zeta functions.

## Explanations

### L1 human

Algebraic K-theory measures a ring through its modules and its invertible matrices.
The group $K_0$ counts projective modules, with the rule that a direct sum becomes a sum.
For a field, projective modules are vector spaces, and $K_0$ just records the dimension, so it is $\Z$.
The group $K_1$ remembers invertible matrices up to elementary row operations; for a field this is the determinant, so $K_1$ is the group of nonzero elements.
The higher groups are harder to compute, and they connect algebra with topology and number theory.
