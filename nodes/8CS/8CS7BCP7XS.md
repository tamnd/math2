---
tag: 8CS7BCP7XS
kind: concept
name: Flexibility method
msc: [74K10, 74S99]
sources:
  - url: https://en.wikipedia.org/wiki/Flexibility_method
same_as:
  wikidata: Q492260
  wikipedia: Flexibility method
---

## Summary

The flexibility method, also called the force method, analyses a [[statically indeterminate structure|SKVPKD5VZN]] by taking some redundant forces as unknowns.
Removing the redundant supports or members leaves a statically determinate structure; the redundant forces are then fixed by requiring that the removed constraints are respected.
These compatibility conditions form a linear system whose matrix is the flexibility matrix.
It is the counterpart of the [[direct stiffness method|7511XGF6MJ]], which takes displacements as unknowns.

## Explanations

### L1 human

Some structures have more supports than are needed to stand, so the equations of balance alone do not fix the forces.
The flexibility method removes the extra supports and asks how far the structure would then move at those points.
Each removed support must in fact not move, so the unknown support forces must push the points back.
Take a beam of length $L$, clamped at one end, resting on a prop at the other, and carrying a uniform load $w$ per length.
For it the method gives the prop force $3wL/8$.
