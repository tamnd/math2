---
tag: Y0CN7V3B7E
kind: concept
name: Finite-dimensional distributions
msc: [60G05, 60G07]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-dimensional_distribution
same_as:
  wikidata: Q5450380
  wikipedia: Finite-dimensional distribution
---

## Summary

The finite-dimensional distributions of a [[stochastic process|0QH5ENKZM1]] $(X_t)_{t \in T}$ are the joint laws of the random vectors $(X_{t_1}, \dots, X_{t_k})$ for finitely many times $t_1, \dots, t_k$.
They determine the law of the process on the product $\sigma$-algebra.
By the Kolmogorov extension theorem, a consistent family of such laws comes from some process, which is the usual way to construct processes.
They do not determine path properties such as continuity.

## Explanations

### L1 human

A random process is a random quantity that evolves over time.
To describe it, one can list, for each finite set of times, the joint distribution of its values at those times.
These are the finite-dimensional distributions.
For example, take a sequence of independent fair coin tosses.
The values at any $k$ times are independent and each is fair.
So each such joint law gives probability $2^{-k}$ to each of the $2^k$ outcomes.
