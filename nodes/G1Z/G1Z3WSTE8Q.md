---
tag: G1Z3WSTE8Q
kind: concept
name: Fisher information
msc: [62B10, 62F10]
sources:
  - url: https://en.wikipedia.org/wiki/Fisher_information
same_as:
  wikidata: Q1420659
  wikipedia: Fisher information
---

## Summary

The Fisher information $I(\theta)$ measures how much an observation tells about an unknown parameter $\theta$ of a statistical model.
It is the variance of the score, the derivative in $\theta$ of the log-likelihood.
It bounds the precision of unbiased estimators through the [[Cramér–Rao bound|1JFKTEQVRX]], and its inverse is the asymptotic variance of the [[maximum likelihood estimator|0FREPFKNS7]].

## Explanations

### L1 human

If a small change of the parameter changes the distribution of the data a lot, then the data pin the parameter down well, and the information is large.
If the distribution hardly moves, the information is small.
Picture the log-likelihood as a hill: high information means a sharp peak, low information a flat top.
For one observation of a normal variable with mean $\theta$ and variance $\sigma^2$, the information is $1/\sigma^2$, so less noise means more information.
With $n$ independent observations the information adds up to $n/\sigma^2$.
