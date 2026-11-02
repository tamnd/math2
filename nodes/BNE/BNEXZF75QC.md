---
tag: BNEXZF75QC
kind: concept
name: Smoothing spline
msc: [65D10, 41A15, 62G08]
specializes: [V42H0R3EKX]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothing_spline
same_as:
  wikidata: Q7546460
  wikipedia: Smoothing spline
---

## Summary

A smoothing spline is the function that best balances closeness to noisy data against roughness, measured by the integral of the squared second derivative.
The balance is set by a smoothing parameter $\lambda > 0$.
The minimizer turns out to be a natural [[cubic spline|V42H0R3EKX]] with knots at the data points.
Smoothing splines are a basic tool of nonparametric regression and data smoothing.

## Explanations

### L1 human

Imagine noisy measurements scattered around an unknown smooth curve.
Passing a curve through every point copies the noise, while a straight line may miss the shape.
A smoothing spline pays a price for missing the points and a price for bending, and takes the curve with the smallest total price.
A small $\lambda$ gives a wiggly curve close to the data, and a large $\lambda$ gives a curve close to the [[least squares|0BYTQ4X1HC]] line.
