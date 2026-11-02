---
tag: 2XX0A85WSF
kind: concept
name: Errors-in-variables model
msc: [62J05, 62P20]
sources:
  - url: https://en.wikipedia.org/wiki/Errors-in-variables_model
same_as:
  wikidata: Q5395728
  wikipedia: Errors-in-variables model
---

## Summary

An errors-in-variables model is a regression model in which the regressors are measured with error, not only the response.
In that case [[ordinary least squares|YM708KHV2W]] on the observed regressors is biased and not [[consistent|0AS800VAYX]].
In the simple linear case the slope is pulled towards zero, an effect called attenuation or regression dilution.
Consistent estimation needs extra information, such as the ratio of the error variances, repeated measurements, or [[instrumental variables|6ETK64HYK6]].
Deming regression and total least squares are methods for such models.

## Explanations

### L1 human

Suppose the true effect of a quantity $\xi$ on $y$ has slope $2$, but $\xi$ can only be measured with noise.
The noisy readings spread out more than the true values, and the extra spread is unrelated to $y$.
The fitted line therefore looks flatter than the true one.
If the measurement noise has the same variance as the true values, the least squares slope tends to $1$ instead of $2$.
