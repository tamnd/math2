---
tag: RK84ANP6BP
kind: concept
name: Noncentral chi-squared distribution
msc: ["62E15", "60E05"]
specializes: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
same_as:
  wikidata: Q1052990
  wikipedia: Noncentral chi-squared distribution
---

## Summary

The noncentral chi-squared distribution is the distribution of a sum of squares of independent normal variables with unit variance and arbitrary means.
It has two parameters: the number $k$ of terms and the noncentrality $\lambda$, the sum of the squared means.
For $\lambda = 0$ it is the ordinary chi-squared distribution.
It describes the distribution of chi-squared test statistics under alternatives, so it is used to compute the power of these tests.

## Explanations

### L1 human

Throw a dart at a target in $k$ dimensions, with independent normal errors in each direction, but aim at a point at distance $\sqrt{\lambda}$ from the centre.
The squared distance of the dart from the centre has the noncentral chi-squared distribution.
When the aim is at the centre, this is the usual chi-squared distribution.
For example, if $X$ is normal with mean $2$ and variance $1$, then $X^2$ is noncentral chi-squared with $k = 1$ and $\lambda = 4$, and its mean is $1 + 4 = 5$.
