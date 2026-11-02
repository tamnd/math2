---
tag: ZPCPW4W1Y9
kind: concept
name: Stochastic approximation
msc: [62L20]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_approximation
same_as:
  wikidata: Q97663916
  wikipedia: Stochastic approximation
---

## Summary

Stochastic approximation is a family of iterative methods for finding a root or an extremum of a function observed only with random noise.
Each step moves the current guess by a decreasing step size times a noisy measurement.
The first methods were the Robbins–Monro algorithm of 1951, for roots, and the Kiefer–Wolfowitz algorithm of 1952, for maxima.
Stochastic gradient descent, the workhorse of machine learning, is a stochastic approximation method.

## Explanations

### L1 human

Suppose a machine has a dial, and its average output depends on the dial setting, but every single reading is noisy.
To find the setting where the average output equals a target, turn the dial a little against each error you read.
The turns get smaller over time, so the noise averages out while the dial still travels far enough to reach the right place.
For example, to estimate a mean $m$ from samples $Z_1, Z_2, \dots$, the update $\theta_{n+1} = \theta_n + \frac{1}{n} (Z_n - \theta_n)$ with $\theta_1 = 0$ gives exactly the running average of the samples.
