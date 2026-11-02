---
tag: CMAX3KF9H0
kind: concept
name: Akaike information criterion
msc: [62B10]
sources:
  - url: https://en.wikipedia.org/wiki/Akaike_information_criterion
same_as:
  wikidata: Q1662573
  wikipedia: Akaike information criterion
---

## Summary

The Akaike information criterion (AIC) scores a fitted statistical model by its maximized [[likelihood|0VW9E4QXR6]], with a penalty for the number of parameters.
Among candidate models, one prefers the model with the smallest AIC.
It rests on an estimate of the expected [[Kullback–Leibler divergence|PQBW43X5RE]] between the true law and the fitted model, and it aims at good prediction.

## Explanations

### L1 human

A model with more parameters always fits the data at hand at least as well, but it may only be fitting noise.
AIC balances the fit, measured by the likelihood, against the complexity, measured by the number of parameters.
Each extra parameter costs $2$ units, so it must raise twice the log-likelihood by more than $2$ to be worth adding.
For example, a cubic regression is preferred to a straight line only if its better fit pays for its two extra coefficients.
