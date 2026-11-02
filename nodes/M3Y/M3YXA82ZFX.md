---
tag: M3YXA82ZFX
kind: concept
name: Morita duality
msc: [16D90, 16D50]
sources:
  - url: https://en.wikipedia.org/wiki/Morita_equivalence
---

## Summary

A Morita duality between two [[rings|0B1261B5ED]] $R$ and $S$ is a contravariant equivalence between suitable categories of left $R$-modules and right $S$-modules.
It is given by a bimodule $U$ through the functors $\Hom(-, U)$.
It generalizes the duality $V \mapsto V^*$ between finite-dimensional vector spaces.
Matlis duality over complete Noetherian local rings and the duality $\Hom(-, R)$ over quasi-Frobenius rings are the main examples.
Morita characterized such dualities by the bimodule $U$, which must be an [[injective|85H7PRHDPZ]] cogenerator on both sides.

## Explanations

### L1 human

For finite-dimensional vector spaces, taking the dual space reverses all arrows and taking it twice gives back the space.
A Morita duality is the same phenomenon for modules over a ring.
One fixes a module $U$ that plays the role of the field and sends a module $M$ to the module of maps from $M$ to $U$.
For finitely generated modules, doing this twice gives back $M$.
Not every ring admits such a duality; it forces strong finiteness conditions on the ring.
