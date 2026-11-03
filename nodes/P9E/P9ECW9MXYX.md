---
tag: P9ECW9MXYX
kind: concept
name: Kalman–Bucy filter
msc: ["93E11", 60G35, 60H10]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman_filter
---

## Summary

The Kalman–Bucy filter is the continuous-time version of the [[Kalman filter|DFM9YXF9AG]], introduced by Kálmán and Bucy in 1961.
It estimates the state of a linear [[stochastic differential equation|B219G9SHJA]] from a continuous stream of noisy linear observations.
The estimate solves a linear stochastic differential equation driven by the observations, and its error covariance solves a matrix [[Riccati equation|0VT2QK6X6Q]].
For Gaussian initial data it gives the exact [[conditional expectation|0TTDGTEFMN]], and so it solves the [[filtering problem|T97B6NBPA8]] in the linear case.

## Explanations

### L1 human

The discrete Kalman filter processes one measurement at a time.
When measurements arrive continuously, as from an analog sensor, the steps become infinitely small and the filter becomes a differential equation.
The estimate moves according to the model, plus a correction proportional to the mismatch between what is measured and what the estimate predicts.
The size of the correction is set by a matrix that is computed in advance from a Riccati equation.
