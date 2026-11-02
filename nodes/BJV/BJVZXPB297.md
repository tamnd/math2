---
tag: BJVZXPB297
kind: concept
name: Floquet theory
msc: [34C25, 34A30, 34D08]
sources:
  - url: https://en.wikipedia.org/wiki/Floquet_theory
same_as:
  wikidata: Q902618
  wikipedia: Floquet theory
---

## Summary

Floquet theory studies linear systems $x' = A(t)\, x$ whose coefficient matrix $A(t)$ is periodic in time.
Its main result is that every [[fundamental matrix|0H1GN6P9R5]] is a periodic matrix times a matrix exponential $e^{tB}$.
So a periodic change of variables turns the system into one with constant coefficients.
The behaviour of solutions, such as stability, is read off from the eigenvalues of the monodromy matrix, the [[Floquet multipliers|FPS7YFGX32]].
It applies to the [[Hill equation|YE7H8DGDPY]], to the stability of periodic orbits and to waves in periodic media.
See the [[definition|GW8SBF37K1]].

## Explanations

### L1 human

A child on a swing who pumps the legs periodically changes the equation of motion periodically in time.
Floquet theory answers whether such a periodically forced linear system has growing or bounded motion.
The key is to look at the system once per period, like taking a photo every period.
The map from one photo to the next is a fixed matrix, the monodromy matrix, and its eigenvalues decide everything.
