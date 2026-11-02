---
tag: JP1QV1KQ0P
kind: concept
name: Accelerated failure time model
msc: [62N01, 62N05, 62N02]
sources:
  - url: https://en.wikipedia.org/wiki/Accelerated_failure_time_model
same_as:
  wikidata: Q4672282
  wikipedia: Accelerated failure time model
---

## Summary

An accelerated failure time model says that covariates stretch or shrink the time scale of a lifetime.
The [[survival function|QTM1HZM53Q]] for covariates $x$ is the baseline survival function evaluated at a rescaled time $t e^{-\beta^T x}$.
Equivalently, $\log T$ is a linear function of the covariates plus an error term, so the model is a linear regression for log-times.
It is the main alternative to the [[proportional hazards model|N029V3JX60]] in [[survival analysis|443ZWDX88P]]; the Weibull family is the only one that satisfies both.

## Explanations

### L1 human

The common saying that one dog year equals seven human years is an accelerated failure time idea.
Dogs go through the same life stages as people, only seven times faster.
In such a model a treatment does not add a fixed risk; it makes the clock run slower or faster.
For example, a coefficient with $e^{\beta} = 2$ means that every lifetime quantile, such as the median, is doubled.
