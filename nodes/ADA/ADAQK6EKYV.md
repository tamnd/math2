---
tag: ADAQK6EKYV
kind: concept
name: Flux balance analysis
msc: [92C42, 90C05]
sources:
  - url: https://en.wikipedia.org/wiki/Flux_balance_analysis
same_as:
  wikidata: Q5463029
  wikipedia: Flux balance analysis
---

## Summary

Flux balance analysis predicts the reaction rates of a metabolic network at steady state by solving a [[linear program|VNMXB0J2KA]].
It uses only the stoichiometry of the reactions and bounds on the fluxes, not the kinetic rate laws, which are usually unknown.
The steady-state condition makes the flux vector lie in the [[null space|0PHDYNR24D]] of the stoichiometric matrix.
An objective, such as the rate of biomass production, then picks one flux vector.
It scales to genome-scale networks with thousands of reactions and is widely used in metabolic engineering.

## Explanations

### L1 human

Think of a city's water pipes: at every junction, water in must equal water out.
In a cell, each metabolite is a junction and each reaction is a pipe, and at steady state each metabolite is made as fast as it is used.
These balance rules, plus limits on how fast each pipe can flow, leave many possible flow patterns.
Flux balance analysis picks the one that makes the most of something, usually the material for cell growth.
