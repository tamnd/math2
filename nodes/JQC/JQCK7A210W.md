---
tag: JQCK7A210W
kind: concept
name: Stiefel–Whitney class
msc: [57R20, 55R40]
specializes: [7HACJC0JE2]
sources:
  - url: https://en.wikipedia.org/wiki/Stiefel%E2%80%93Whitney_class
same_as:
  wikidata: Q1293273
  wikipedia: Stiefel–Whitney class
---

## Summary

The Stiefel–Whitney classes $w_i(E) \in H^i(B; \Z/2\Z)$ are mod $2$ [[characteristic classes|7HACJC0JE2]] of real vector bundles $E \to B$.
Four axioms determine them: naturality, the [[Whitney sum|BE9NJRVDR3]] formula, a normalization, and vanishing above the rank.
The first class detects orientability and the second detects the existence of a spin structure.
Stiefel–Whitney numbers of manifolds decide when two closed manifolds are cobordant.

## Explanations

### L1 human

A real vector bundle can be twisted in ways that ordinary integer invariants do not see.
Stiefel–Whitney classes count such twists modulo $2$, as cohomology classes with values $0$ or $1$.
The first one answers a yes-or-no question: can the fibers be oriented consistently along every loop?
For the Möbius band over the circle the answer is no, and $w_1$ is nonzero; for the cylinder it is yes, and $w_1 = 0$.
