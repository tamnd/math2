---
tag: S2GBXQ26QM
kind: concept
name: Karoubi envelope
msc: [18A05, "18E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Karoubi_envelope
same_as:
  wikidata: Q3055409
  wikipedia: Karoubi envelope
---

## Summary

The Karoubi envelope of a category $\mathcal{C}$ is the category obtained by formally adding an image for every [[idempotent|0N5NJZKKN3]] morphism.
Its objects are pairs of an object and an idempotent endomorphism of it.
It is the smallest category containing $\mathcal{C}$ in which every idempotent splits, and it is also called the idempotent completion.
For example, the Karoubi envelope of the category of finitely generated free modules over a ring is the category of finitely generated projective modules.

## Explanations

### L1 human

An idempotent map $e$ satisfies $e \circ e = e$, like a projection onto a subspace.
In vector spaces such a projection has an image, and $e$ factors through it.
In some categories the image is missing, and the Karoubi envelope adds it as the formal object $(A, e)$.
In this way projective modules appear as images of projections on free modules.
