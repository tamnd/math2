---
tag: RATW595XR9
kind: concept
name: Huber loss
msc: [62F35, 62G35]
specializes: [3BTG6VVCGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Huber_loss
same_as:
  wikidata: Q17027770
  wikipedia: Huber loss
---

## Summary

The Huber loss is a [[loss function|3BTG6VVCGZ]] that is quadratic for small residuals and linear for large ones.
It combines the efficiency of [[least squares|0BYTQ4X1HC]] for well-behaved data with the resistance of absolute loss to outliers.
Peter Huber introduced it in 1964 to define a robust [[M-estimator|4503R8BVF8]] of location, and it is now also common in regression and machine learning.

## Explanations

### L1 human

Squared error punishes a residual of $10$ a hundred times as much as a residual of $1$, so a single outlier can dominate a fit.
Absolute error is gentler on outliers but has a sharp corner at zero.
The Huber loss uses squared error near zero and switches to a straight line beyond a cutoff $\delta$.
So small errors are treated as in least squares, while large errors count only in proportion to their size.
