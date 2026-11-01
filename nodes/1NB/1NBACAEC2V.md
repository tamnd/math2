---
tag: 1NBACAEC2V
kind: concept
name: Finite morphism of rings
msc: [13B10, 13B21]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_morphism
---

## Summary

A ring homomorphism $f \colon A \to B$ is finite if $B$, viewed as an $A$-module through $f$, is [[finitely generated|05QY1VEBYD]].
Finite homomorphisms are exactly the [[integral|B7X0KFY1S1]] homomorphisms that are also of [[finite type|AC5TFFQT9M]].
They are closed under composition and base change.
In algebraic geometry they correspond to finite morphisms of affine schemes, such as the projection of a curve onto a line in general position.

## Explanations

### L1 human

A finite ring map makes the big ring a finite-dimensional object over the small ring, in the sense of modules.
The Gaussian integers $\Z[i]$ are finite over $\Z$: every element is $a \cdot 1 + b \cdot i$ with $a, b \in \Z$.
The polynomial ring $k[x]$ is not finite over the field $k$: the powers $1, x, x^2, \ldots$ are linearly independent, so no finite set spans it.
Finiteness is the ring version of a finite field extension.
