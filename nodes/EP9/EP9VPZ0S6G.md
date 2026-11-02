---
tag: EP9VPZ0S6G
kind: concept
name: Exponential family
msc: [62B05, "60E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_family
same_as:
  wikidata: Q1188504
  wikipedia: Exponential family
---

## Summary

An exponential family is a parametric family of probability distributions whose densities have the form $h(x) \exp\big(\sum_i \eta_i(\theta) T_i(x) - A(\theta)\big)$.
Most standard distributions belong to one: normal, binomial, Poisson, gamma, beta and many more.
The statistics $T_i$ are sufficient, and the structure makes estimation, testing and Bayesian updating explicit.

## Explanations

### L1 human

In an exponential family the parameter and the data meet only through a few products $\eta_i(\theta) T_i(x)$ in an exponent.
So the data can be compressed to the values of $T_1, \dots, T_k$ without losing any information about the parameter.
For example, the Poisson probabilities $e^{-\lambda} \lambda^x / x!$ can be written as $\frac{1}{x!} \exp(x \log \lambda - \lambda)$, with $T(x) = x$ and $\eta = \log \lambda$.
For a sample of Poisson counts, only the total count matters for $\lambda$.
