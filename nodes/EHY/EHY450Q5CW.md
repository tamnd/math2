---
tag: EHY450Q5CW
kind: concept
name: Conjugate prior
msc: [62F15]
specializes: [00NBBSXRQS]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_prior
same_as:
  wikidata: Q3711784
  wikipedia: Conjugate prior
---

## Summary

A conjugate prior for a likelihood is a [[prior distribution|00NBBSXRQS]] from a family that the update by Bayes' theorem maps into itself.
The [[posterior distribution|0KJ7ZS8AJA]] then lies in the same family, and only its parameters change.
This gives closed-form posteriors, which made conjugate priors central in [[Bayesian inference|0JWRJX2RMP]] before simulation methods became common.

## Explanations

### L1 human

A Bayesian update multiplies the prior by the likelihood.
For a well-chosen family of priors the product has the same shape as the prior, with new parameters.
For a coin with unknown chance $p$, a beta prior $\mathrm{Beta}(a, b)$ plus $k$ heads and $m$ tails gives the posterior $\mathrm{Beta}(a + k, b + m)$.
So the prior acts like $a$ earlier heads and $b$ earlier tails, and the data just add to these counts.
