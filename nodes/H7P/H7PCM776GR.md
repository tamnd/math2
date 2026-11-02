---
tag: H7PCM776GR
kind: concept
name: Bockstein homomorphism
msc: [55S05, 55N10]
sources:
  - url: https://en.wikipedia.org/wiki/Bockstein_homomorphism
same_as:
  wikidata: Q4936292
  wikipedia: Bockstein homomorphism
---

## Summary

The Bockstein homomorphism is the connecting map in the long exact sequence of (co)homology that comes from a short exact sequence of coefficient groups.
It raises cohomological degree by one.
For the sequence $0 \to \Z/p \to \Z/p^2 \to \Z/p \to 0$ it gives a natural operation on mod $p$ cohomology that detects $p$-torsion in integral cohomology.

## Explanations

### L1 human

Cohomology with coefficients in $\Z/p$ loses some information about integral cohomology.
The Bockstein homomorphism recovers part of it by asking whether a mod $p$ class lifts to a mod $p^2$ class.
When it does not lift, the Bockstein gives a nonzero class one degree higher.
For the real projective plane, the generator of $H^1(\R P^2; \Z/2)$ does not lift to $\Z/4$ coefficients, and its Bockstein is the generator of $H^2(\R P^2; \Z/2)$.
