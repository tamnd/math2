---
tag: DZW58R6T2Q
kind: concept
name: Picard group of a ring
msc: [13C20, 13C10, 14C22]
sources:
  - url: https://en.wikipedia.org/wiki/Picard_group
---

## Summary

The Picard group $\operatorname{Pic}(R)$ of a [[commutative ring|0310REJJY8]] $R$ collects the isomorphism classes of rank one [[projective modules|BFFA03GE3V]] over $R$.
Its group law is the [[tensor product|F0HQXQ0HCD]].
It measures how far such modules are from being free.
For an [[integral domain|0QVD7WBFGN]] it is the group of [[invertible ideals|E190TAV2S6]] modulo principal ones, and for a [[Dedekind domain|7NPY2CN5KB]] it is the [[ideal class group|WQ46BD3ARY]].
It is the Picard group of the affine scheme $\operatorname{Spec} R$.

## Explanations

### L1 human

A rank one projective module looks like a copy of the ring near every point, but it may be twisted globally.
The Picard group collects all these twisted copies, and tensoring two of them gives a third one.
The ring itself is the untwisted copy and plays the role of the identity.
Over $\Z[\sqrt{-5}]$, the ideal $(2, 1 + \sqrt{-5})$ is such a twisted copy, and the Picard group has two elements.
