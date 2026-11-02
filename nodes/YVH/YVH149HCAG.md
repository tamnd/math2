---
tag: YVH149HCAG
kind: concept
name: Continuous and residual spectrum
msc: [47A10]
sources:
  - url: https://en.wikipedia.org/wiki/Decomposition_of_spectrum_(functional_analysis)
---

## Summary

The continuous and residual spectra are the parts of the spectrum of an operator that consist of numbers which are not eigenvalues.
At such a $\lambda$, the operator $T - \lambda I$ is injective but not invertible.
The spectrum is continuous at $\lambda$ when the range is dense and residual when it is not.
Together with the [[point spectrum|7FNVA0Q6YQ]], they split the spectrum into three disjoint pieces.

## Explanations

### L1 human

Outside the eigenvalues, $T - \lambda I$ loses no information, yet it still cannot be inverted with a bounded inverse.
Either its range comes close to every vector but misses some, which is the continuous case, or its range stays away from a whole direction, which is the residual case.
For multiplication by $x$ on square-integrable functions on $[0, 1]$, every number in $[0, 1]$ is in the continuous spectrum.
For the right shift on sequences, every number of absolute value less than $1$ is in the residual spectrum.
