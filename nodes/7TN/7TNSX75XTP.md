---
tag: 7TNSX75XTP
kind: concept
name: Algebraic K-theory of spaces
msc: [19D10, 57Q10, 55P42]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

The algebraic K-theory of a space $X$, written $A(X)$, is a spectrum defined by Waldhausen from spaces built from $X$ by attaching finitely many cells.
It is a version of [[algebraic K-theory|5GVFZWMWC8]] in which rings are replaced by spaces.
It links K-theory to the geometry of manifolds: through it, the spaces of h-cobordisms and of diffeomorphisms of high-dimensional manifolds are related to homotopy theory.
For a point, $A(\ast)$ is the K-theory of the sphere spectrum.

## Explanations

### L1 human

Ordinary algebraic K-theory studies modules over a ring and how they can be built from each other.
Waldhausen's idea was to do the same with spaces over a fixed space $X$, built by gluing finitely many cells to $X$.
Cells play the role of free modules, and homotopy equivalences play the role of isomorphisms.
When $X$ is a point, this is K-theory of finite cell complexes, which is K-theory of the sphere spectrum.
Linearizing, that is replacing spaces by their cellular chain complexes, gives a map from $A(X)$ to the K-theory of the group ring $\Z[\pi_1 X]$.
