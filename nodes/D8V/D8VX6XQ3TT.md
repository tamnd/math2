---
tag: D8VX6XQ3TT
kind: concept
name: Heteroscedasticity
msc: [62J05, 62J20]
sources:
  - url: https://en.wikipedia.org/wiki/Homoscedasticity_and_heteroscedasticity
---

## Summary

A collection of random variables is heteroscedastic when their variances are not all equal; it is homoscedastic when they are.
In regression the term refers to errors whose variance changes with the regressors, for example noise that grows with the size of the response.
Under heteroscedasticity [[ordinary least squares|YM708KHV2W]] remains unbiased but is no longer the best linear unbiased estimator.
Also, the usual formula for its standard errors is wrong.
Remedies include [[weighted least squares|H5CGZHBR58]] and heteroscedasticity-consistent standard errors, and tests such as the Breusch–Pagan and White tests detect it.
The spelling heteroskedasticity is also common.

## Explanations

### L1 human

Plot household spending on food against income.
Poor households spend similar amounts, but rich households differ a lot, so the cloud of points fans out as income grows.
That fanning out is heteroscedasticity: the scatter around the trend is not the same everywhere.
It matters because a method that treats all points as equally precise will be overconfident about some conclusions.
