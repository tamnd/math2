---
tag: XB91QS2AR0
kind: concept
name: Pseudo-spectral method
msc: [65M70, 65N35]
specializes: [MYV657YRDW]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-spectral_method
same_as:
  wikidata: Q7254447
  wikipedia: Pseudo-spectral method
---

## Summary

A pseudo-spectral method is a [[spectral method|MYV657YRDW]] that imposes the equation at grid points, by collocation.
It does not use integrals against the basis functions.
Derivatives are computed in coefficient space, for example with the [[fast Fourier transform|S966EZX3ZT]], while products and other nonlinear terms are computed pointwise on the grid.
This keeps the accuracy of spectral methods at a much lower cost for nonlinear problems.
The price is [[aliasing|FEC9RG38X9]] errors from the pointwise products, which are often removed by padding or truncation.
See the [[definition|T37Q055GDA]].

## Explanations

### L1 human

Store a function by its values at evenly spaced points around a circle.
To differentiate, turn the values into wave amplitudes, multiply each amplitude by its frequency times $i$, and turn the result back into values.
To multiply two functions, just multiply their values point by point.
Switching back and forth between values and amplitudes is fast, which makes the method efficient.
