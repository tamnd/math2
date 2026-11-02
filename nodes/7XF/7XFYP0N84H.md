---
tag: 7XFYP0N84H
kind: concept
name: Hopf algebra
msc: [16T05]
specializes: [Q9HHVN606G]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
same_as:
  wikidata: Q1627597
  wikipedia: Hopf algebra
---

## Summary

A Hopf algebra is a [[bialgebra|Q9HHVN606G]] with an [[antipode|PG3ECG5D0G]], a linear map that plays the role of taking inverses in a group.
Group algebras, coordinate rings of affine algebraic groups and universal enveloping algebras of Lie algebras are the main classical examples.
Quantum groups are Hopf algebras that deform these examples.
Hopf algebras also appear in algebraic topology, as the cohomology of Lie groups and H-spaces, and in combinatorics and renormalization.

## Explanations

### L1 human

A group has a product, an identity and inverses.
A Hopf algebra copies all three in linear form: a multiplication, a comultiplication that splits elements, and an antipode that imitates $g \mapsto g^{-1}$.
In the group algebra $KG$, the antipode sends each group element $g$ to $g^{-1}$, and the axiom $S(g)g = 1$ is just $g^{-1}g = 1$.
The extra structure lets one tensor representations together and take duals of representations, as one does for groups.
