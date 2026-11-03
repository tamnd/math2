---
tag: NJQY3GHY7H
kind: concept
name: K-theory of a symmetric monoidal category
msc: [19D23, 18M05]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_monoidal_category
---

## Summary

The K-theory of a [[symmetric monoidal category|5S7ER95XAC]] $S$, in Quillen's form, is the classifying space of a category $S^{-1}S$.
In $S^{-1}S$ the objects of $S$ become invertible up to homotopy.
When $S$ is a groupoid whose translations are faithful, this space is the group completion of the classifying space of $S$.
For the groupoid of finitely generated projective modules over a ring it recovers $K_0(R) \times BGL(R)^+$.
For finite sets it gives the infinite loop space $QS^0$ of stable homotopy theory.
This construction is the bridge between algebraic K-theory and infinite loop spaces.

## Explanations

### L1 human

The integers come from the natural numbers by allowing differences $m - n$ of two natural numbers.
Quillen's $S^{-1}S$ does the same for a symmetric monoidal category: its objects are pairs $(m, n)$, thought of as formal differences.
The classifying space of $S^{-1}S$ has as components the formal differences of isomorphism classes, which is the Grothendieck group.
The higher homotopy groups remember the automorphisms of the objects, and they give the higher K-groups.
For finite sets with disjoint union, the result is the stable homotopy groups of spheres, by the Barratt–Priddy–Quillen theorem.
