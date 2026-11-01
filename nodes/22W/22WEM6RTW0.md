---
tag: 22WEM6RTW0
kind: concept
name: Gaussian process
msc: [60G15]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_process
same_as:
  wikidata: Q1496376
  wikipedia: Gaussian process
---

## Summary

A Gaussian process is a [[stochastic process|0QH5ENKZM1]] all of whose [[finite-dimensional distributions|Y0CN7V3B7E]] are [[multivariate normal|0XN3K7RSZY]].
Its law is determined by its mean function and its covariance function, and any positive semidefinite covariance function arises.
The [[Wiener process|22735FGJV6]], the [[Brownian bridge|3MCVMBAGD1]], the [[Ornstein–Uhlenbeck process|HZM2ASCDY4]] and [[fractional Brownian motion|VC6R7XSKRQ]] are Gaussian processes.
In statistics and machine learning, Gaussian processes serve as prior distributions on unknown functions.

## Explanations

### L1 human

A Gaussian process is a random function whose values at any finitely many points have a joint normal distribution.
One describes it by an average curve and by a rule saying how strongly the values at two points move together.
For example, take a standard normal number $Z$ and set $X_t = Z t$; this random straight line through the origin is a Gaussian process with mean $0$ and covariance $st$.
