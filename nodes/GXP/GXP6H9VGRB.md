---
tag: GXP6H9VGRB
kind: concept
name: Bayesian information criterion
msc: [62F15, 62B10]
sources:
  - url: https://en.wikipedia.org/wiki/Bayesian_information_criterion
same_as:
  wikidata: Q1988242
  wikipedia: Bayesian information criterion
---

## Summary

The Bayesian information criterion (BIC), also called the Schwarz criterion, scores a fitted model by its maximized [[likelihood|0VW9E4QXR6]] with a penalty of $\ln n$ per parameter.
Among candidate models, one prefers the model with the smallest BIC.
It comes from a large-sample approximation of the marginal likelihood of a model in [[Bayesian inference|0JWRJX2RMP]].
Its penalty is heavier than that of the [[Akaike information criterion|CMAX3KF9H0]] once $n \ge 8$.

## Explanations

### L1 human

Like the AIC, the BIC trades the fit of a model against its number of parameters.
Its price for each parameter grows slowly with the sample size $n$, as $\ln n$.
So with much data, the BIC prefers simpler models than the AIC does.
For $n = 100$ observations, each parameter costs about $4.6$ units instead of $2$.
