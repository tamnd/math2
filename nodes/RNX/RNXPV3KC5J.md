---
tag: RNXPV3KC5J
kind: concept
name: Henselian ring
msc: [13J15]
specializes: [MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
same_as:
  wikidata: Q1607573
  wikipedia: Henselian ring
---

## Summary

A Henselian ring is a [[local ring|MZ02BKPHJA]] in which [[Hensel's lemma|010QVB71T2]] holds.
There, factorizations of polynomials over the [[residue field|NJ3APQ8BHH]] into coprime factors lift to the ring.
Every complete local ring, such as the $p$-adic integers or a formal power series ring, is Henselian.
Henselian rings behave like small neighbourhoods of a point in the étale topology.
Every local ring has a [[Henselization|917PGHVZPM]], a smallest Henselian ring over it.

## Explanations

### L1 human

Hensel's lemma says that a root of a polynomial modulo $p$ can be refined to a root modulo $p^2$, $p^3$, and so on, if the root is simple.
A Henselian ring is a local ring where this refinement always ends in an actual root inside the ring.
The $p$-adic integers have this property, but the fractions with denominators prime to $p$ do not.
For example, $x^2 + 1$ has a simple root modulo $5$, yet no square root of $-1$ is rational.
The [[definition|WSQ8GH8XWZ]] states the lifting condition.
