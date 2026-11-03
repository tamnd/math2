---
tag: AYVZQWZ08Y
kind: concept
name: Wiener series
msc: [93C10, "93E12"]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_series
same_as:
  wikidata: Q4402522
  wikipedia: Wiener series
---

## Summary

The Wiener series of a nonlinear time-invariant system expands its output into functionals of the input.
These functionals are orthogonal when the input is Gaussian white noise.
It is a reordering of the [[Volterra series|RQ3JKGWD03]].
Each term is corrected by lower-degree terms, so that terms of different degrees are uncorrelated.
This orthogonality makes the kernels measurable one at a time by correlating the output with products of delayed inputs.
Wiener series are a tool for identifying nonlinear systems, for example in physiology and in signal processing.

## Explanations

### L1 human

A Volterra series writes the output of a nonlinear system as a linear part, plus a quadratic part, plus a cubic part, and so on.
These parts overlap: a quadratic term already has a nonzero average, which also looks like a constant term.
The Wiener series subtracts such overlaps, so that each part carries new information when the input is random noise.
For example, the square $z^2$ of a filtered noise signal $z$ has the Wiener form "its mean" plus "$z^2$ minus its mean", and the two parts are uncorrelated.
