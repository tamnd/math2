---
tag: K1GQXRY0K9
kind: concept
name: Wiener filter
msc: [60G35, 62M20, "93E11"]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_filter
same_as:
  wikidata: Q25523
  wikipedia: Wiener filter
---

## Summary

The Wiener filter is the linear time-invariant filter that estimates a [[stationary|DT0QXJE705]] signal from a noisy stationary observation with the least [[mean squared error|05NZ1HHQMV]].
Norbert Wiener derived it in the 1940s.
Without a causality constraint, its frequency response is the ratio of the cross spectral density to the spectral density of the observation.
With causality, it solves the [[Wiener–Hopf equation|QYY4NMDY5H]], see [[the Wiener filter equation|BVFGX5JH7X]].
The [[Kalman filter|DFM9YXF9AG]] later extended optimal linear estimation to nonstationary signals in state-space form.

## Explanations

### L1 human

A recording contains music and hiss.
The music is strong at some frequencies and the hiss is spread evenly over all of them.
The Wiener filter keeps each frequency in proportion to how much of it is music: frequencies where the music dominates pass almost unchanged, frequencies where hiss dominates are damped.
Among all filters that act the same way at all times, this choice makes the average squared error smallest.
