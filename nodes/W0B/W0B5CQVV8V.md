---
tag: W0B5CQVV8V
kind: concept
name: Whittle likelihood
msc: [62M15, 62M10]
sources:
  - url: https://en.wikipedia.org/wiki/Whittle_likelihood
same_as:
  wikidata: Q25304822
  wikipedia: Whittle likelihood
---

## Summary

The Whittle likelihood approximates the Gaussian likelihood of a stationary time series using the [[periodogram|3ZYM0HXA3E]] and the model spectral density.
It replaces a large covariance matrix by a sum over frequencies, which makes estimation fast.
Peter Whittle introduced it in the 1950s, and maximizing it gives estimators with the same first-order asymptotic behaviour as Gaussian maximum likelihood.

## Explanations

### L1 human

Neighbouring values of a time series are dependent, which makes the exact likelihood awkward to compute.
After a Fourier transform, the values at different frequencies are nearly independent.
The Whittle likelihood treats them as independent, each with a spread given by the model's spectrum at that frequency.
Fitting a model then means matching the model spectrum to the observed periodogram, frequency by frequency.
