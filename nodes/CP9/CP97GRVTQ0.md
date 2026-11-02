---
tag: CP97GRVTQ0
kind: concept
name: Score
msc: [62F10, 62B10]
sources:
  - url: https://en.wikipedia.org/wiki/Informant_function
same_as:
  wikidata: Q3952743
  wikipedia: Informant function
---

## Summary

The score is the gradient of the log-likelihood with respect to the parameter.
It measures how sensitive the log-likelihood of the observed data is to small changes of the parameter.
Under regularity conditions its expectation at the true parameter is zero, and its covariance is the Fisher information.
Setting the score equal to zero gives the likelihood equations, whose solutions are candidates for the maximum likelihood estimate.

## Explanations

### L1 human

Imagine the log-likelihood as a hill over the parameter axis.
The score is the slope of the hill at a given parameter value.
At the top of the hill, the maximum likelihood estimate, the slope is zero.
For one observation $x$ from a normal distribution with mean $\mu$ and variance $1$, the score is $x - \mu$: it is positive when the observation suggests a larger mean.
