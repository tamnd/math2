---
tag: VHQA7XPMQ4
kind: concept
name: Master equation
msc: [82C31, 60J27, 82C05]
sources:
  - url: https://en.wikipedia.org/wiki/Master_equation
same_as:
  wikidata: Q722878
  wikipedia: Master equation
---

## Summary

A master equation is a system of linear differential equations for probabilities $P_t(x)$.
Here $P_t(x)$ is the probability that a system is in the state $x$ at time $t$.
It balances the flow of probability into each state against the flow out of it, using the transition rates between states.
It is the forward equation of a [[continuous-time Markov chain|TWQFE0FZZS]], written in the form used in physics and chemistry.
Master equations model chemical reactions, population dynamics, queues and stochastic lattice dynamics.

## Explanations

### L1 human

Think of the possible states of a system as rooms, and of probability as a fluid spread among them.
Fluid leaves each room through doors at given rates and enters it from other rooms.
The master equation says that the change in a room's amount is the inflow minus the outflow.
For a machine that breaks at rate $a$ and is repaired at rate $b$, the probability $P_t$ of being broken changes at rate $a(1 - P_t) - b P_t$.
In the long run $P_t$ settles at $a/(a + b)$.
