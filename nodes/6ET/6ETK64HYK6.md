---
tag: 6ETK64HYK6
kind: concept
name: Instrumental variables estimation
msc: [62P20, 62J05]
sources:
  - url: https://en.wikipedia.org/wiki/Instrumental_variables_estimation
same_as:
  wikidata: Q1665305
  wikipedia: Instrumental variables estimation
---

## Summary

Instrumental variables estimation recovers the coefficients of a linear model when some regressors are correlated with the error term, a situation called endogeneity.
Endogeneity arises from omitted variables, simultaneous equations or [[measurement error|2XX0A85WSF]], and it makes [[ordinary least squares|YM708KHV2W]] inconsistent.
An instrument is a variable that is correlated with the endogenous regressor but uncorrelated with the error.
It isolates the part of the regressor's variation that is free of the confounding.
Two-stage least squares is the standard instrumental variables estimator, and it is a special case of the [[generalized method of moments|ZPVMCCDYZ5]].

## Explanations

### L1 human

Suppose one wants the effect of years of schooling on wages, but ability raises both, and ability is not observed.
Least squares then mixes the effect of schooling with the effect of ability.
An instrument is something that shifts schooling but has no direct link to wages or to ability.
An example is a rule that changes the age at which pupils may leave school.
Comparing how wages and schooling both move with the instrument gives the effect of schooling alone.
With one regressor and one instrument $z$, the estimate is the ratio $\operatorname{Cov}(z, y) / \operatorname{Cov}(z, x)$ of sample covariances.
