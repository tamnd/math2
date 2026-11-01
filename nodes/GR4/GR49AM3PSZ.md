---
tag: GR49AM3PSZ
kind: concept
name: Interacting particle system
msc: [60K35, 82C22]
specializes: [4HS3C12472]
sources:
  - url: https://en.wikipedia.org/wiki/Interacting_particle_system
same_as:
  wikidata: Q6045167
  wikipedia: Interacting particle system
---

## Summary

An interacting particle system is a continuous-time Markov process on configurations of a lattice or graph, in which each site carries a state.
The state at a site changes at rates that depend on the states of nearby sites.
Each local change is simple, but infinitely many sites interact, and the system can show phase transitions.
Main examples are the [[contact process|9RVKQJQ5JJ]], the [[voter model|YBAE5QCH1A]], the [[exclusion process|TXC6PZT8CF]] and stochastic dynamics of the [[Ising model|R0KGM32QN6]].
They model epidemics, opinions, traffic and magnets.

## Explanations

### L1 human

Put a person at each point of an infinite grid, each healthy or sick.
A sick person recovers after a random time, and a healthy person gets sick at a rate that grows with the number of sick neighbours.
Each person follows simple local rules, yet the whole grid may behave in very different ways: the illness may die out or spread forever.
Interacting particle systems are the models of this kind.
