---
tag: 3MCVMBAGD1
kind: concept
name: Brownian bridge
msc: [60J65, 60G15]
specializes: [22WEM6RTW0]
sources:
  - url: https://en.wikipedia.org/wiki/Brownian_bridge
same_as:
  wikidata: Q628309
  wikipedia: Brownian bridge
---

## Summary

A Brownian bridge is a Brownian motion on $[0, 1]$ forced to return to $0$ at time $1$.
It is a continuous centred [[Gaussian process|22WEM6RTW0]] with covariance $\min(s, t) - st$.
It is the limit of the uniform [[empirical process|XKFG1676CG]], which makes it central in goodness-of-fit tests such as the Kolmogorov–Smirnov test.

## Explanations

### L1 human

Imagine a Brownian path that starts at $0$, wanders at random, and is tied down so that it must be back at $0$ at time $1$.
This pinned random path is a Brownian bridge.
A simple recipe: take a Brownian path $W$ and subtract the straight line from $(0, 0)$ to $(1, W_1)$.
Near the two ends it is almost fixed, and in the middle, at $t = 1/2$, it varies most, with variance $1/4$.
