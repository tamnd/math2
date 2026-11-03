---
tag: Z5J0Z6MD6G
kind: concept
name: Metabolic control analysis
msc: [92C42, 92C45]
sources:
  - url: https://en.wikipedia.org/wiki/Metabolic_control_analysis
same_as:
  wikidata: Q502671
  wikipedia: Metabolic control analysis
---

## Summary

Metabolic control analysis is a framework that measures how strongly each enzyme in a metabolic pathway controls the steady-state fluxes and concentrations.
It was developed in the early 1970s by Henrik Kacser and James Burns, and independently by Reinhart Heinrich and Tom Rapoport.
Its basic quantities are control coefficients, which are scaled sensitivities of the whole system, and elasticities, which are scaled sensitivities of single reactions.
Its theorems, such as the summation theorem, show that control is shared among enzymes rather than held by one rate-limiting step.

## Explanations

### L1 human

In a production line, people often look for the one slow step that limits everything.
Metabolic control analysis asks a more careful question: if one enzyme is made $1\%$ more active, by what percentage does the output of the pathway change?
The answers, one per enzyme, are the flux control coefficients.
For a pathway they add up to $1$, so if one enzyme has a large share of control, the others must have little.
