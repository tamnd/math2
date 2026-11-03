---
tag: ECFW7KP0SX
kind: concept
name: Thomason–Trobaugh K-theory of schemes
msc: ["19E08", 18F25]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

Thomason–Trobaugh K-theory assigns to a quasi-compact quasi-separated [[scheme|5A35TYZD02]] $X$ the K-theory spectrum of its perfect complexes, with quasi-isomorphisms as weak equivalences.
It is built with Waldhausen's S-construction instead of from vector bundles.
When $X$ has an ample family of line bundles it agrees with Quillen's [[K-theory of vector bundles|Y2467453Q5]], but it behaves well on every such scheme.
Thomason and Trobaugh proved that it satisfies a localization theorem and Mayer–Vietoris sequences for open covers.

## Explanations

### L1 human

On a general scheme there may be too few vector bundles to describe the geometry, and Quillen's K-theory of vector bundles can then misbehave.
Thomason and Trobaugh replaced vector bundles by perfect complexes, which are chain complexes that look locally like bounded complexes of vector bundles.
Two complexes count as the same when they have the same cohomology through a quasi-isomorphism.
With this change, K-theory can be glued from open pieces, like a cohomology theory.
