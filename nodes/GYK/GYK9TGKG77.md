---
tag: GYK9TGKG77
kind: concept
name: Relative K-groups
msc: [19B99, 19A49]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

Relative K-groups $K_n(R, I)$ attach K-groups to a ring $R$ together with a two-sided ideal $I$.
They measure the part of the K-theory of $R$ that is invisible in the quotient ring $R/I$.
They fit into a long exact sequence that links $K_n(R, I)$, $K_n(R)$ and $K_n(R/I)$.
This sequence is a basic tool for computing K-groups, for instance through Mayer–Vietoris sequences and excision.

## Explanations

### L1 human

Reducing a ring modulo an ideal forgets information, and the relative K-groups record what is forgotten.
In degree one, they are built from invertible matrices that become the identity modulo the ideal.
Picture integer matrices that are congruent to the identity modulo $p$: they are invisible in matrices over $\Z/p\Z$.
When the ideal is the whole ring, nothing survives in the quotient, and the relative groups are the ordinary K-groups of the ring.
