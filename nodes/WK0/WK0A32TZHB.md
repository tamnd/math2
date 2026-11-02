---
tag: WK0A32TZHB
kind: concept
name: Simplicial object
msc: [18N50, 55U10]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_set
---

## Summary

A simplicial object in a [[category|A2DE66937D]] $\mathcal{C}$ is a contravariant [[functor|28NQ0KRHD3]] from the [[simplex category|FRFYHJGAN3]] to $\mathcal{C}$.
It is a sequence of objects $X_0, X_1, X_2, \dots$ of $\mathcal{C}$ with face and degeneracy maps between them that obey the simplicial identities.
In $\mathcal{C} = \mathbf{Set}$ these are the [[simplicial sets|WW81ARB8K9]], and in abelian groups they are the simplicial abelian groups of the [[Dold–Kan correspondence|PY4EWJ8BQA]].
They let one do homotopy theory with objects of $\mathcal{C}$.

## Explanations

### L1 human

Think of $X_n$ as the "$n$-dimensional pieces" of a shape built from points, edges, triangles and higher simplices.
The face maps send a piece to its faces, and the degeneracy maps view a piece as a flattened piece one dimension up.
In a simplicial object, each $X_n$ is not a mere set but an object of some category, such as a group or a space.
For example, the constant simplicial object on an object $A$ has $X_n = A$ for all $n$ and all face and degeneracy maps equal to the identity.
