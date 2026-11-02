---
tag: PP1A0JB47Q
kind: concept
name: Bayes estimator
msc: [62C10, 62F15]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes_estimator
same_as:
  wikidata: Q842217
  wikipedia: Bayes estimator
---

## Summary

A Bayes estimator is an estimator that minimizes the [[Bayes risk|VEBDNCJJTN]], the risk averaged over a prior distribution on the parameter.
In practice it minimizes, for each observed data set, the expected loss under the [[posterior distribution|0KJ7ZS8AJA]].
Under squared error loss it is the posterior mean.
Bayes estimators link [[Bayesian inference|0JWRJX2RMP]] with frequentist decision theory, since they are central in the study of admissible and minimax rules.

## Explanations

### L1 human

Before seeing the data, a Bayesian describes beliefs about the unknown quantity by a prior distribution.
After seeing the data, the beliefs are updated to a posterior distribution.
The Bayes estimator is the single number that is best on average according to these updated beliefs.
For a coin with a uniform prior on its heads probability, $x$ heads in $n$ tosses give the Bayes estimate $(x + 1)/(n + 2)$ under squared error.
