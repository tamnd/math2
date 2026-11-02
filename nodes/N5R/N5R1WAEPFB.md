---
tag: N5R1WAEPFB
kind: concept
name: Geometric morphism
msc: [18F10, 18B25]
sources:
  - url: https://en.wikipedia.org/wiki/Topos
---

## Summary

A geometric morphism $f \colon \mathcal{E} \to \mathcal{F}$ between [[toposes|6837RS7N82]] is a pair of [[adjoint functors|TZHF6ZM92S]] $f^* \dashv f_*$, with $f_* \colon \mathcal{E} \to \mathcal{F}$, whose left adjoint $f^* \colon \mathcal{F} \to \mathcal{E}$ preserves finite limits.
It is the notion of map between toposes that matches continuous maps between spaces.
A continuous map $g \colon X \to Y$ gives a geometric morphism $\mathrm{Sh}(X) \to \mathrm{Sh}(Y)$, with $g_*$ the direct image and $g^*$ the inverse image of sheaves.
Points of a topos, and the classifying toposes of geometric theories, are described through geometric morphisms.

## Explanations

### L1 human

A continuous map of spaces lets one push sheaves forward and pull sheaves back, and these two operations are adjoint.
Pulling back keeps finite limits, such as products and equalities of sections.
A geometric morphism is any such adjoint pair between toposes, so it acts as a continuous map between generalized spaces.
For example, a point $x$ of a space $X$ gives a geometric morphism $\mathbf{Set} \to \mathrm{Sh}(X)$ whose inverse image sends a sheaf to its stalk at $x$.
