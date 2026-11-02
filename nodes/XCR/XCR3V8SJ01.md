---
tag: XCR3V8SJ01
kind: concept
name: Probit model
msc: [62J12, 62P20]
specializes: [K6C48KMRKC]
sources:
  - url: https://en.wikipedia.org/wiki/Probit_model
same_as:
  wikidata: Q635217
  wikipedia: Probit model
---

## Summary

The probit model is a regression model for a binary response.
The probability of the outcome $1$ is the standard normal [[cumulative distribution function|0H8H7ZTHW2]] evaluated at a linear combination of regressors.
It can be read as a latent variable model: an unobserved normal quantity crosses a threshold exactly when the outcome is $1$.
It is a [[generalized linear model|K6C48KMRKC]] for Bernoulli responses with the probit link, and it is fitted by [[maximum likelihood|0FREPFKNS7]].
It is close to [[logistic regression|JN1PJ5AJJS]] in practice, and the choice between them is often a matter of convention in the field.

## Explanations

### L1 human

Think of each person as having a hidden score, equal to a linear formula in their characteristics plus a normal random term.
The person says yes when the hidden score is above zero.
The probability of a yes is then the normal distribution function at the linear formula.
For example, if the linear formula equals $0$, the probability is $1/2$, and if it equals $1.96$, the probability is about $0.975$.
