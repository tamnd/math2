---
tag: 7EB64ZBXAT
kind: concept
name: Jacobson ring
msc: [13A15]
specializes: [0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobson_ring
same_as:
  wikidata: Q2620920
  wikipedia: Jacobson ring
---

## Summary

A Jacobson ring, also called a Hilbert ring, is a [[commutative ring|0310REJJY8]] in which every [[prime ideal|00MHHZ9SNE]] is an intersection of [[maximal ideals|0PV74TR5FP]].
In such a ring, the maximal ideals alone determine all radical ideals, as in [[Hilbert's Nullstellensatz|D85VZWS9QK]].
Fields, $\Z$, and every finitely generated algebra over a Jacobson ring are Jacobson rings; this last fact is a general form of the Nullstellensatz.
In geometry, the closed points of the spectrum of a Jacobson ring are dense in every closed subset.

## Explanations

### L1 human

In the ring of polynomials over $\C$, a curve is determined by its points, and each point is a maximal ideal.
A Jacobson ring is a ring where every prime ideal is determined in this way by the maximal ideals above it.
The integers are an example: the prime ideal $0$ is the intersection of all ideals $p\Z$, since no nonzero integer is divisible by every prime.
A local domain that is not a field, such as $\Z_{(p)}$, is not Jacobson.
Its only maximal ideal is $p\Z_{(p)}$, and this ideal cannot recover the prime $0$.
