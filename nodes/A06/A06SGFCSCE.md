---
tag: A06SGFCSCE
kind: concept
name: General linear model
msc: [62J05, 62J10, 62H12]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_model
same_as:
  wikidata: Q1826488
  wikipedia: General linear model
---

## Summary

The general linear model writes a matrix of responses as a known design matrix times an unknown coefficient matrix, plus random errors with mean zero.
It contains multiple [[linear regression|41FVC4P5JB]], [[analysis of variance|M9AQ5HKGP4]], analysis of covariance, [[multivariate analysis of variance|8J3B7N8CAT]] and the $t$-test and [[F-test|8MTVCMAATD]] as special cases.
Its theory rests on [[ordinary least squares|YM708KHV2W]] and on projections in $\R^n$.
It should not be confused with the [[generalized linear model|K6C48KMRKC]], which allows non-normal responses and a link function.

## Explanations

### L1 human

Many classical methods look different but share one shape: response equals a linear combination of known columns plus noise.
The known columns can be measured quantities, like height or dose, or indicator variables that say which group an observation belongs to.
For example, comparing the means of two groups is a regression on two indicator columns, one for each group.
Writing all these methods as one model lets a single theory of estimation and testing cover them all.
