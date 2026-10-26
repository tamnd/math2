---
tag: 0KJ7ZS8AJA
kind: concept
name: Posterior probability
aliases: [posterior, posterior-distribution]
msc: [62F15]
uses: [0NM6E9VW04, 00NBBSXRQS, 0FJB06AD2P]
sources:
  - url: https://en.wikipedia.org/wiki/Posterior_probability
    locator: Definition in the distributional case
same_as:
  wikidata: Q278079
  wikipedia: Posterior probability
---

## Summary

The posterior probability of a hypothesis $H$ is its [[conditional probability|0FJB06AD2P]] $P(H \mid D)$ given the observed data $D$.
By [[Bayes' theorem|0NM6E9VW04]], $P(H \mid D) = P(D \mid H) \, P(H) / P(D)$. So the posterior is proportional to the likelihood $P(D \mid H)$ times the [[prior probability|00NBBSXRQS]] $P(H)$.
For an unknown parameter $\theta$ with prior density $\pi(\theta)$ and likelihood $L(\theta \mid x)$, the posterior density is $\pi(\theta \mid x) = L(\theta \mid x) \, \pi(\theta) / \int L(t \mid x) \, \pi(t) \, dt$.

## Remarks

The posterior of one experiment can be the prior of the next experiment. So Bayesian updates can be done one observation at a time.
A credible interval is an interval that has a given posterior probability, for example $95\%$.

## Explanations

### L1 human

The posterior is what you believe after you see the data.
It mixes what you believed before (the prior) with how well each hypothesis explains the data (the likelihood).
