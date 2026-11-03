---
tag: H6AWC7DNNE
kind: concept
name: Unscented Kalman filter
msc: ["93E11", 60G35, 93C10]
sources:
  - url: https://en.wikipedia.org/wiki/Unscented_transform
---

## Summary

The unscented Kalman filter is an approximate state estimator for nonlinear systems, introduced by Julier and Uhlmann.
It replaces the linearization of the [[extended Kalman filter|3E6E4VQGFJ]] by the unscented transform.
A small set of sigma points with the same mean and [[covariance|0V7G6WMFK0]] as the current estimate is pushed through the nonlinear model.
The mean and covariance of the images give the new estimate.
It needs no derivatives of the model, and it captures the mean and covariance of the transformed distribution more accurately than linearization in many cases.

## Explanations

### L1 human

To see how a cloud of uncertainty is bent by a nonlinear map, one could push thousands of random points through it.
The unscented transform uses only a few carefully placed points: the center and two points on each side along each principal direction of the cloud.
Their images give a new center and a new spread.
The unscented Kalman filter uses this trick in each predict and update step of the Kalman filter.
