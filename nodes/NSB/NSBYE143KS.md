---
tag: NSBYE143KS
kind: concept
name: Bayes factor
msc: [62F15, 62F03]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes_factor
same_as:
  wikidata: Q4165283
  wikipedia: Bayes factor
---

## Summary

The Bayes factor of two models is the ratio of the probabilities that each model gives to the observed data.
In each model the probability is averaged over the prior of its parameters.
It is the factor by which the data change the odds between the two models.
It is the Bayesian tool to compare hypotheses and models, an alternative to [[p-values|0GGKJGZF6D]] and likelihood-ratio tests.

## Explanations

### L1 human

Two theories compete to explain the same data.
Each theory predicts the data with some probability, averaged over what it leaves uncertain.
The Bayes factor is the ratio of these two predictions: a value of $10$ means that the data were $10$ times more expected under the first theory.
Whatever odds you gave the theories before, you multiply them by the Bayes factor to get your odds after seeing the data.
