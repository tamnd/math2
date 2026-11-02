---
tag: P3H4MMC4ZH
kind: concept
name: Discrete wavelet transform
msc: [42C40, 65T60, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_wavelet_transform
same_as:
  wikidata: Q2414958
  wikipedia: Discrete wavelet transform
---

## Summary

The discrete wavelet transform splits a sequence into a coarse part and a detail part.
It uses two filters followed by downsampling by $2$, and then repeats the split on the coarse part.
For filters from an orthonormal [[multiresolution analysis|1GHQMBR7DE]], each step is an orthogonal change of coordinates.
So the transform preserves energy and is easy to invert.
The outputs are the coefficients of a function in a [[wavelet|4PZ35C0GV3]] basis.
The [[fast wavelet transform|PDVYQAW887]] computes them in a number of steps proportional to the length of the signal.
It is the basis of wavelet compression, for example in the JPEG 2000 image standard.

## Explanations

### L1 human

Take a list of numbers and group them in pairs.
For each pair, keep a scaled sum, which records the average, and a scaled difference, which records the detail.
Then do the same with the list of sums, and again, until one number is left.
For a smooth signal most details are tiny, so one can drop them and still rebuild a good approximation.
This is the Haar case; other wavelets use longer filters in the same pattern.
