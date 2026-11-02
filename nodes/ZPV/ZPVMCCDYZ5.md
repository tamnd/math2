---
tag: ZPVMCCDYZ5
kind: concept
name: Generalized method of moments
msc: [62F10, 62P20]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_method_of_moments
same_as:
  wikidata: Q683131
  wikipedia: Generalized method of moments
---

## Summary

The generalized method of moments (GMM) estimates parameters from moment conditions $E[g(X, \theta_0)] = 0$, possibly more conditions than parameters.
It chooses $\theta$ to make the sample averages of the moment functions as close to zero as possible in a weighted quadratic norm.
It contains the method of moments, least squares and instrumental variables estimation as special cases.
It was introduced in econometrics by Lars Peter Hansen.
It is a standard tool there because it does not need a full model of the data.

## Explanations

### L1 human

Suppose the theory gives you more facts about averages than you have unknown numbers.
With noisy data you usually cannot make all the sample averages match exactly.
GMM picks the parameter that makes the mismatches as small as possible, giving more weight to the averages that are measured more precisely.
For Poisson counts, both the mean and the variance equal the parameter $\lambda$, and GMM combines the two facts into one estimate.
