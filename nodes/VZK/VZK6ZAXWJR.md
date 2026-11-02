---
tag: VZK6ZAXWJR
kind: concept
name: Cascade algorithm
msc: [65T60, 42C40]
sources:
  - url: https://en.wikipedia.org/wiki/Cascade_algorithm
same_as:
  wikidata: Q5048176
  wikipedia: Cascade algorithm
---

## Summary

The cascade algorithm computes the [[scaling function|YH4BERB952]] of a wavelet from its filter coefficients by iterating the refinement equation.
It starts from a simple function, such as the indicator of $[0,1)$.
Each step builds a new function from shrunken and shifted copies of the old one.
For good filters, such as the filters of the Daubechies wavelets, the iterates converge to the scaling function.
Most compactly supported wavelets have no closed formula, so this is the usual way to draw them.

## Explanations

### L1 human

A scaling function is defined by a self-similarity rule: it is a weighted sum of half-size copies of itself.
The cascade algorithm uses this rule as a recipe.
Start with a box, apply the rule to get a new shape, then apply it again to the new shape, and so on.
For the Haar filter the box is already a fixed point: two half-width boxes side by side make the box again.
For Daubechies filters the shapes become finer and more jagged at each step and settle down to a fractal-looking curve.
