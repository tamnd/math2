---
tag: 00NBBSXRQS
kind: concept
name: Prior probability
aliases: [prior, prior-distribution]
msc: [62F15]
uses: [0NM6E9VW04]
sources:
  - url: https://en.wikipedia.org/wiki/Prior_probability
    locator: lead section
same_as:
  wikidata: Q278090
  wikipedia: Prior probability
---

## Summary

A prior probability is the probability that we give to a hypothesis before we see the data.
More generally, a prior distribution is the distribution that we give to an unknown quantity before we see the data.
In [[Bayes' theorem|0NM6E9VW04]] the prior is combined with the likelihood of the data, and the result is the [[posterior probability|0KJ7ZS8AJA]].

## Remarks

An informative prior uses real knowledge about the quantity. An uninformative prior tries to express little knowledge, for example a uniform distribution on the possible values.
An improper prior is a "distribution" with infinite total mass, such as the uniform measure on $\mathbb{R}$. It can still give a proper posterior.

## Explanations

### L1 human

The prior is what you believe before the experiment.
If $1\%$ of people have a disease, then the prior probability that a random person is sick is $0.01$, before any test is done.
