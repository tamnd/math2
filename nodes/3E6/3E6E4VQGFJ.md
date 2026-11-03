---
tag: 3E6E4VQGFJ
kind: concept
name: Extended Kalman filter
msc: ["93E11", 60G35, 93C10]
sources:
  - url: https://en.wikipedia.org/wiki/Extended_Kalman_filter
same_as:
  wikidata: Q5421817
  wikipedia: Extended Kalman filter
---

## Summary

The extended Kalman filter is an approximate state estimator for nonlinear systems with additive noise.
It runs the steps of the [[Kalman filter|DFM9YXF9AG]], but propagates the estimate through the nonlinear model.
In place of the matrices of a linear model, it uses the [[Jacobian matrices|047NDTEPCV]] of the model at the current estimate.
It is not optimal in general, and it can diverge when the nonlinearity is strong or the initial error is large.
Still it is simple and widely used, for example in navigation.
The [[unscented Kalman filter|H6AWC7DNNE]] and the [[particle filter|BZK7HQDMT0]] are common alternatives.

## Explanations

### L1 human

The Kalman filter works for straight-line models, where effects are proportional to causes.
Most real models bend.
The extended Kalman filter replaces the bent model, at each step, by its tangent at the current best guess, and applies the Kalman filter to that tangent model.
When the guess is good and the bending is mild, this works well.
