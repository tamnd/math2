---
tag: PB0DSH9XCG
kind: concept
name: Motzkin number
msc: [05A15, 11B83]
sources:
  - url: https://en.wikipedia.org/wiki/Motzkin_number
same_as:
  wikidata: Q2915234
  wikipedia: Motzkin number
---

## Summary

The Motzkin number $M_n$ counts certain [[lattice paths|040WY0TT2G]] from $(0, 0)$ to $(n, 0)$, see the [[definition|PHA1S6GQGV]].
The paths use up, down and flat steps and never go below the horizontal axis.
It also counts the ways to draw non-crossing chords between $n$ points on a circle.
The sequence starts $1, 1, 2, 4, 9, 21, 51, 127$.
The Motzkin numbers are a close relative of the [[Catalan numbers|0YWZJEABB2]], which count the same paths without flat steps.

## Explanations

### L1 human

Imagine a walker who takes $n$ steps to the right, and each step goes up, down or stays level.
The walker starts and ends at height $0$ and never goes underground.
For $n = 3$ the possible walks are level-level-level, up-down-level, level-up-down and up-level-down.
So $M_3 = 4$.
