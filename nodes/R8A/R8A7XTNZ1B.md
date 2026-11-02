---
tag: R8A7XTNZ1B
kind: concept
name: Self-similar measure
msc: [28A80]
specializes: [059TJN0NZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Self-similarity
---

## Summary

A self-similar measure is a [[probability measure|059TJN0NZ1]] on $\R^n$ that is a weighted average of its own images under finitely many contracting similarities.
For given similarities and weights there is exactly one such measure, by a theorem of Hutchinson.
Its support is the self-similar fractal, or attractor, of the similarities.
Self-similar measures are the basic examples of fractal measures, and their dimensions and Fourier decay are studied in detail.

## Explanations

### L1 human

Take a unit of sand on the line and copy it in two shrunken versions, each with half of the sand.
Put one copy in the left third and one in the right third, and repeat this forever.
The limit distribution of the sand is the Cantor measure, which lives on the middle-thirds Cantor set.
It is self-similar: its part on the left third and its part on the right third each look like the whole measure, shrunk by $3$ and holding half the mass.
