---
tag: NCRPWS9W5R
kind: concept
name: Quasitriangular Hopf algebra
msc: [16T05, 16T25, 81R50]
specializes: [7XFYP0N84H]
sources:
  - url: https://en.wikipedia.org/wiki/Quasitriangular_Hopf_algebra
same_as:
  wikidata: Q7269541
  wikipedia: Quasitriangular Hopf algebra
---

## Summary

A quasitriangular Hopf algebra is a [[Hopf algebra|7XFYP0N84H]] $H$ together with an invertible element $R \in H \otimes H$.
This element, the universal R-matrix, conjugates the coproduct into the opposite coproduct.
The element $R$ satisfies the [[Yang–Baxter equation|663BP8ZHS5]].
For two modules $V, W$ over $H$, the map $v \otimes w \mapsto \tau(R \cdot (v \otimes w))$, with $\tau$ the flip, is an isomorphism $V \otimes W \to W \otimes V$.
These isomorphisms make the category of $H$-modules a [[braided monoidal category|VT8SFWT0XW]], which is why such algebras feed knot invariants and [[quantum groups|AP2ZDXANKC]].

## Explanations

### L1 human

For a group, the representations $V \otimes W$ and $W \otimes V$ are the same up to swapping the factors.
For a general Hopf algebra the plain swap is no longer a map of modules.
A quasitriangular structure supplies a corrected swap: first act by a fixed element $R$, then swap.
In the simplest case, the group algebra of a group with $R = 1 \otimes 1$, the corrected swap is the ordinary swap.
The interesting examples, such as the Drinfeld double of a finite-dimensional Hopf algebra, can have a corrected swap that applied twice is not the identity.
