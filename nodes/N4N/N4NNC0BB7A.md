---
tag: N4NNC0BB7A
kind: concept
name: Galois symbol
msc: [19D45, 12G05, 19F15]
sources:
  - url: https://en.wikipedia.org/wiki/Norm_residue_isomorphism_theorem
---

## Summary

The Galois symbol is also called the norm residue homomorphism.
It maps Milnor K-theory modulo $m$ of a field $F$ to the Galois cohomology of $F$.
The coefficients are the twisted roots of unity $\mu_m^{\otimes n}$.
It sends a symbol $\set{a_1, \ldots, a_n}$ to the cup product of the Kummer classes of the $a_i$.
The norm residue isomorphism theorem says that it is always an isomorphism; the cases $n = 2$ and $m = 2$ are the Merkurjev–Suslin theorem and the Milnor conjecture.

## Explanations

### L1 human

Kummer theory turns a nonzero element $a$ of a field into a cohomology class, which records how the field symmetries move the $m$-th roots of $a$.
Cohomology classes can be multiplied by the cup product.
The Galois symbol multiplies the classes of $a_1, \ldots, a_n$.
It turns explicit symbols, built from field elements, into cohomology classes, which are defined abstractly.
