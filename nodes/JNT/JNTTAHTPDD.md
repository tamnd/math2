---
tag: JNTTAHTPDD
kind: concept
name: Mixed model
msc: [62J05]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_model
same_as:
  wikidata: Q1501135
  wikipedia: Mixed model
---

## Summary

A mixed model is a linear model with both fixed effects and random effects.
Fixed effects are unknown constants, and random effects are random variables whose covariance is to be estimated.
Random effects describe correlated groups of observations that share a source of variation.
Examples are repeated measurements on the same person or pupils in the same school.
It extends the [[general linear model|A06SGFCSCE]], and its covariance parameters are usually estimated by maximum likelihood or restricted maximum likelihood.
Mixed models are standard for longitudinal, clustered and hierarchical data.

## Explanations

### L1 human

Measure the blood pressure of ten patients five times each.
The five values of one patient are closer to each other than to the values of other patients, because each patient has a personal level.
A mixed model gives each patient a random personal shift around the population mean, plus independent measurement noise.
The fixed part answers questions about the population, and the variance of the random shifts says how much patients differ.
