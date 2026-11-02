---
tag: 6DMQ97EBVG
kind: concept
name: Local asymptotic normality
msc: [62F12, "62E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Local_asymptotic_normality
same_as:
  wikidata: Q6664277
  wikipedia: Local asymptotic normality
---

## Summary

A sequence of statistical models is locally asymptotically normal (LAN) at a parameter value if its log-likelihood ratios have a special form at scale $1/\sqrt{n}$.
At that scale they look like those of a single observation from a normal location model.
The notion is due to Lucien Le Cam.
Smooth i.i.d. parametric models are LAN, with the Fisher information as the covariance.
LAN is the setting of the asymptotic optimality theory of estimators and tests: the convolution theorem and the local asymptotic minimax theorem.

## Explanations

### L1 human

With $n$ observations, parameter values that differ by much more than $1/\sqrt{n}$ are easy to tell apart, and values that differ by much less are impossible to tell apart.
The interesting scale is exactly $1/\sqrt{n}$.
LAN says that at this scale, every smooth model behaves like the simplest model there is: one normal observation whose mean is the unknown local parameter.
So asymptotic questions about complicated models reduce to easy questions about the normal distribution.
