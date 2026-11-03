---
tag: DFM9YXF9AG
kind: concept
name: Kalman filter
msc: ["93E11", 60G35, 62M20]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman_filter
same_as:
  wikidata: Q846780
  wikipedia: Kalman filter
---

## Summary

The Kalman filter is a recursive algorithm that estimates the state of a linear dynamical system from noisy measurements.
At each step it predicts the state with the model and then corrects the prediction with the new measurement, weighting the two by their uncertainties.
For linear systems with Gaussian noise, it computes exactly the [[conditional expectation|0TTDGTEFMN]] of the state given the measurements, and its error [[covariance matrix|0V7G6WMFK0]].
So it solves the [[filtering problem|T97B6NBPA8]] in this case.
Rudolf Kálmán published it in 1960, and it is used in navigation, tracking, econometrics and many other fields.

## Explanations

### L1 human

A ship's position is estimated from its speed and heading, but the estimate drifts.
Now and then a noisy position fix arrives.
The Kalman filter blends the two: if the fix is precise it moves the estimate a lot toward it, if the fix is poor it moves little.
It also keeps track of how uncertain the estimate is, and it needs only the last estimate, not the whole past, to process the next measurement.
