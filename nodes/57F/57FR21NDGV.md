---
tag: 57FR21NDGV
kind: concept
name: Continuous wavelet transform
msc: [42C40, 42A38, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_wavelet_transform
same_as:
  wikidata: Q2622756
  wikipedia: Continuous wavelet transform
---

## Summary

The continuous wavelet transform compares a function $f$ with all rescaled and shifted copies $\abs{a}^{-1/2} \psi((t - b)/a)$ of one analyzing function $\psi$.
It gives a function of scale $a$ and position $b$, which shows where $f$ has features of each size.
When $\psi$ satisfies the [[admissibility condition|2BBB8NY5ZA]], the transform preserves energy up to a constant, and $f$ can be rebuilt from it.
Unlike the [[short-time Fourier transform|3DHNP5NEWH]], its time resolution adapts to the scale.

## Explanations

### L1 human

Pick a small wave shape, like the Mexican hat curve.
Stretch it to many widths and slide it to every position.
At each width and position, measure how well the signal matches the shape.
Wide shapes pick out slow trends and narrow shapes pick out sharp details, such as a jump in the signal.
The resulting map of matches, scale against position, is the continuous wavelet transform.
