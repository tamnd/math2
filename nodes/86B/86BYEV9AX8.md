---
tag: 86BYEV9AX8
kind: concept
name: F-space
msc: [46A16]
sources:
  - url: https://en.wikipedia.org/wiki/F-space
same_as:
  wikidata: Q2664426
  wikipedia: F-space
---

## Summary

An F-space is a [[topological vector space|T32W553W95]] whose topology comes from a complete translation-invariant metric.
F-spaces are the natural setting of the Baire category arguments of functional analysis: the open mapping theorem and the closed graph theorem hold for F-spaces.
Every Banach space and every [[Fréchet space|3GAA614673]] is an F-space, but F-spaces need not be locally convex.

## Explanations

### L1 human

An F-space is a vector space with a notion of distance that behaves well under shifting and has no missing limit points.
Shifting two vectors by the same amount does not change their distance.
Every Cauchy sequence converges.
The space $L^p([0, 1])$ with $0 < p < 1$ and distance $d(f, g) = \int_0^1 \abs{f - g}^p$ is an F-space.
Its only open convex set containing $0$ is the whole space, so it is not locally convex, and in particular it is not a Banach space.
