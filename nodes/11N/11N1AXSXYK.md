---
tag: 11N1AXSXYK
kind: concept
name: Expectation–maximization algorithm
msc: [62F10, 65C60]
sources:
  - url: https://en.wikipedia.org/wiki/Expectation–maximization_algorithm
same_as:
  wikidata: Q1275153
  wikipedia: Expectation–maximization algorithm
---

## Summary

The expectation–maximization (EM) algorithm is an iterative method to compute maximum likelihood estimates when the data are incomplete or the model has latent variables.
Each iteration has two steps.
The expectation step averages the complete-data log-likelihood over the missing part, given the current parameter; the maximization step maximizes this average.
Each iteration does not decrease the likelihood of the observed data.
It is the standard method for fitting mixture models and hidden Markov models; Dempster, Laird and Rubin gave its general formulation in 1977.

## Explanations

### L1 human

Suppose heights come from a mix of two groups, but nobody recorded who belongs to which group.
If you knew the groups, estimating each group's average would be easy; if you knew the averages, guessing the groups would be easy.
EM goes back and forth: it guesses soft group memberships from the current averages, then recomputes the averages from these memberships, and repeats.
Each round makes the fit to the data at least as good as before.
