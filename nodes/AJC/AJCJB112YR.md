---
tag: AJCJB112YR
kind: concept
name: Rauch–Tung–Striebel smoother
msc: ["93E14", "93E11", 62M20]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman_filter
---

## Summary

The Rauch–Tung–Striebel smoother computes estimates of the states of a linear Gaussian state-space model that use all measurements of a fixed interval, past and future.
It runs the [[Kalman filter|DFM9YXF9AG]] forward in time and then a backward recursion that corrects each filtered estimate with information from later measurements.
For linear Gaussian models it gives exactly the [[conditional expectation|0TTDGTEFMN]] of each state given all the data and its error [[covariance matrix|0V7G6WMFK0]].
It was published by Rauch, Tung and Striebel in 1965.

## Explanations

### L1 human

A filter answers: where is the object now, given what has been seen so far?
A smoother answers a later question: where was the object at that earlier time, given everything recorded in the whole session?
Later measurements help to locate earlier positions, just as knowing where a walk ended helps to reconstruct where it passed.
The smoother adds this hindsight with one backward pass over the stored filter results.
