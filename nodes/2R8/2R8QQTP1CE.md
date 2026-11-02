---
tag: 2R8QQTP1CE
kind: concept
name: Lattice of equational theories
msc: [08B15, 08B05, 03C05]
sources:
  - url: https://en.wikipedia.org/wiki/Equational_logic
---

## Summary

The lattice of equational theories of a signature is the set of all equational theories of that signature, ordered by inclusion.
An equational theory is a set of identities closed under logical consequence.
This lattice is complete, and it is dually isomorphic to the lattice of all varieties of the signature, because larger theories have fewer models.
It can be described as the lattice of fully invariant congruences of a term algebra on countably many variables.

## Explanations

### L1 human

Collect all the identities that follow from some axioms; this is an equational theory.
Adding axioms gives a bigger theory and a smaller class of algebras that satisfy it.
The theories, ordered by inclusion, form a lattice that is the upside-down picture of the lattice of varieties.
For example, the theory of abelian groups contains the theory of groups, since it has the extra identity $xy \approx yx$.
