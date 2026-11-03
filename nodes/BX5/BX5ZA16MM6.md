---
tag: BX5ZA16MM6
kind: concept
name: Compartmental models in epidemiology
msc: [92D30, 34C60]
specializes: [AKP63KCK02]
sources:
  - url: https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)
same_as:
  wikidata: Q2572354
  wikipedia: Compartmental models (epidemiology)
---

## Summary

A compartmental model divides a population into a few compartments by infection status and follows the size of each compartment in time.
Hosts flow between compartments at given rates, usually through a system of ordinary differential equations.
The [[SIR model|J5FHBDJGJA]] and the [[SIS and SEIR models|P1ANHAY6XY]] are the basic examples.
These models are the standard first tool of [[mathematical modelling of infectious diseases|AKP63KCK02]].

## Explanations

### L1 human

Picture a set of buckets labelled S, I and R, with water flowing from one bucket to the next.
The water is the population, split into susceptible, infected and recovered people.
The flow from S to I is faster when there is more water in both S and I, because infection needs contact.
The flow from I to R is a steady leak, since infected people recover at a fixed rate.
Writing these flows as equations gives the SIR model.
