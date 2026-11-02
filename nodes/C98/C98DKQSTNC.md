---
tag: C98DKQSTNC
kind: concept
name: Mixture model
msc: [62H30, "62E10"]
specializes: [C63RVH96TF]
sources:
  - url: https://en.wikipedia.org/wiki/Mixture_model
same_as:
  wikidata: Q2260434
  wikipedia: Mixture model
---

## Summary

A mixture model describes a population made of several subpopulations, each with its own distribution.
The density of an observation is a weighted average of the component densities, with weights equal to the subpopulation proportions.
It is a [[latent variable model|C63RVH96TF]] in which the hidden variable is the label of the subpopulation.
Mixture models are usually fitted by the [[expectation–maximization algorithm|11N1AXSXYK]] and are a basis of model-based [[cluster analysis|D9Y3A9RH6J]].

## Explanations

### L1 human

The heights of adults form a mixture of the heights of women and the heights of men.
Each group alone gives a bell-shaped curve, and the population curve is a weighted sum of the two bells.
If the two groups are far apart, the population curve has two humps.
A mixture model starts from such a sum and tries to recover the groups, their proportions and their shapes from the data.
