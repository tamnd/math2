---
tag: 17RASDZEBS
kind: concept
name: Least mean squares filter
msc: ["93E24", 94A12, "93E35"]
sources:
  - url: https://en.wikipedia.org/wiki/Least_mean_squares_filter
same_as:
  wikidata: Q1426666
  wikipedia: Least mean squares filter
---

## Summary

The least mean squares (LMS) filter is an adaptive filter.
After each sample, it moves its coefficients by a small step against the gradient of the current squared error.
It is [[stochastic gradient descent|MBQSZ6VYFC]] applied to the [[mean squared error|05NZ1HHQMV]] of a linear filter.
It seeks the coefficients of the [[Wiener filter|K1GQXRY0K9]] without knowing the signal statistics.
Its cost per sample is linear in the number of coefficients.
This makes it a common tool in signal processing, for example in echo cancellation and channel equalization.

## Explanations

### L1 human

An LMS filter guesses an output from the recent inputs, compares the guess with the desired value, and nudges its coefficients to make the error smaller next time.
The nudge is proportional to the error and to the input, scaled by a step size $\mu$.
A small step gives slow but smooth learning; a step that is too large makes the coefficients blow up.
For a single coefficient that must learn a constant $c$ from the input $1$, the update is $w_{k+1} = w_k + \mu (c - w_k)$.
The error is multiplied by $1 - \mu$ at each step, so it shrinks exactly when $0 < \mu < 2$.
