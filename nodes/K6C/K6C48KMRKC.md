---
tag: K6C48KMRKC
kind: concept
name: Generalized linear model
msc: [62J12]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_linear_model
same_as:
  wikidata: Q1501882
  wikipedia: Generalized linear model
---

## Summary

A generalized linear model relates the mean of a response to a linear combination of regressors through a link function.
The response distribution is taken from an [[exponential family|EP9VPZ0S6G]].
It unifies [[linear regression|41FVC4P5JB]], [[logistic regression|JN1PJ5AJJS]], [[Poisson regression|STHTW16717]] and the [[probit model|XCR3V8SJ01]] in one framework, with one fitting method and one theory of inference.
The framework was introduced by John Nelder and Robert Wedderburn in 1972.
Its coefficients are estimated by [[maximum likelihood|0FREPFKNS7]], usually with iteratively reweighted least squares.

## Explanations

### L1 human

Ordinary regression predicts a number that can be any real value, with normal noise.
Many responses are not like that: a yes/no answer, a count, a waiting time.
A generalized linear model keeps the simple linear formula $x^T \beta$, but passes it through a link function that fits the range of the mean.
It also uses a noise distribution that suits the data.
For counts, for example, the logarithm of the mean is linear in the regressors and the counts are Poisson.
