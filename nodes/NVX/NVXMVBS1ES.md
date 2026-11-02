---
tag: NVXMVBS1ES
kind: definition
name: Weak equivalence
msc: [18N40, 55U35]
defines: E2870TEDG7
uses: [A2DE66937D, 4Q3WY1RX91, C9JEC2WQKV]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_equivalence_(homotopy_theory)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
A *class of weak equivalences* in $\mathcal{C}$ is a class $W$ of morphisms of $\mathcal{C}$ such that:

1. every isomorphism of $\mathcal{C}$ is in $W$;
2. (two out of three) if $f \colon X \to Y$ and $g \colon Y \to Z$ are morphisms and two of $f$, $g$, $g \circ f$ are in $W$, then so is the third.

A pair $(\mathcal{C}, W)$ is a *category with weak equivalences*, and the members of $W$ are its *weak equivalences*.
The weak equivalences of a model category are the members of the class $W$ of its model structure, which satisfies these two clauses.

## Remarks

Example: in the category of topological spaces, the [[weak homotopy equivalences|4Q3WY1RX91]] form a class of weak equivalences.
Homeomorphisms induce isomorphisms on all homotopy groups, and two out of three follows from functoriality of $\pi_0$ and of $\pi_n(-, x)$ at all base points.
Example: in the category of chain complexes of modules over a ring, the [[quasi-isomorphisms|C9JEC2WQKV]] form a class of weak equivalences, by functoriality of homology.

Non-example: in the category of sets, the class of injective maps is closed under composition and contains the isomorphisms, but it fails two out of three.
With $f \colon \set{0} \to \set{0, 1}$ the inclusion and $g \colon \set{0, 1} \to \set{0}$, both $f$ and $g \circ f = \id$ are injective, but $g$ is not.

Some authors, for homotopical categories, ask the stronger two out of six property.
