---
tag: 4QMDFYEK3T
kind: concept
name: Whitehead torsion
msc: [19J10, "57Q10"]
sources:
  - url: https://en.wikipedia.org/wiki/Whitehead_torsion
same_as:
  wikidata: Q7996043
  wikipedia: Whitehead torsion
---

## Summary

The Whitehead torsion $\tau(f)$ of a homotopy equivalence $f \colon K \to L$ of finite connected CW complexes is an element of the [[Whitehead group|8SY3AC4KW3]] of $\pi_1(L)$.
It vanishes exactly when $f$ is a simple homotopy equivalence.
This means that $f$ is homotopic to a composite of finitely many elementary expansions and collapses of cells and their homotopy inverses.
It is the invariant behind the [[s-cobordism theorem|E1E5ABP89W]] and it distinguishes homotopy equivalent spaces that are not simple homotopy equivalent, such as some lens spaces.

## Explanations

### L1 human

A homotopy equivalence says two spaces have the same shape up to continuous deformation.
A finer question is whether one can pass from one complex to the other by adding and removing cells in matched pairs.
Whitehead torsion answers this question algebraically.
It is computed from the cellular chains of the mapping cylinder, an exact complex whose bases give an invertible matrix over the group ring of the fundamental group.
The class of this matrix, up to trivial changes, is the torsion.
