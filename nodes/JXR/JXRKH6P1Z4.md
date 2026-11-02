---
tag: JXRKH6P1Z4
kind: concept
name: Morphism of schemes
msc: [14A15]
sources:
  - url: https://en.wikipedia.org/wiki/Morphism_of_schemes
same_as:
  wikidata: Q25303616
  wikipedia: Morphism of schemes
---

## Summary

A morphism of schemes is a morphism of [[locally ringed spaces|B7FPT8JTXR]] between [[schemes|5A35TYZD02]].
It is a continuous map together with a compatible way to pull back functions.
Between [[affine schemes|B3V3XJ2W8G]], morphisms are the same as ring homomorphisms in the opposite direction.
Schemes with these morphisms form a category, the setting for almost all constructions of algebraic geometry.

## Explanations

### L1 human

A map between two geometric objects should send points to points and also let functions be pulled back.
For schemes, the second part is part of the data: a function $g$ on an open set of the target becomes a function on its preimage.
The local condition says that if $g$ vanishes at $f(x)$, then its pullback vanishes at $x$.
For example, the ring inclusion $\Z \to \Z[i]$ gives a morphism $\operatorname{Spec} \Z[i] \to \operatorname{Spec} \Z$, which sends a prime ideal of $\Z[i]$ to its intersection with $\Z$.
