---
tag: 23ATBZMJHR
kind: concept
name: Rubin causal model
msc: [62D20, 62A01]
sources:
  - url: https://en.wikipedia.org/wiki/Rubin_causal_model
same_as:
  wikidata: Q7376137
  wikipedia: Rubin causal model
---

## Summary

The Rubin causal model, or potential outcomes framework, defines causal effects by comparing the outcomes that the same unit would have under different treatments.
Each unit has one potential outcome for each treatment, but only the one for the treatment actually received is observed.
Causal effects such as the average treatment effect are then parameters of the joint distribution of potential outcomes.
The framework goes back to Jerzy Neyman's work on experiments and was developed by Donald Rubin for observational studies.
It is a basic language of [[causal inference|V3QJFN5800]].

## Explanations

### L1 human

For a patient, think of two versions of the future: one in which she takes the drug and one in which she does not.
The effect of the drug for her is the difference between the two outcomes.
We can only ever see one of these futures, so individual effects are never observed directly.
Averages over many patients can still be learned, for example when a coin flip decides who gets the drug.
