---
tag: AKP85F38KP
kind: concept
name: Glauber dynamics
msc: [82C20, 60J10, 82C22]
sources:
  - url: https://en.wikipedia.org/wiki/Glauber_dynamics
same_as:
  wikidata: Q72148753
  wikipedia: Glauber dynamics
---

## Summary

Glauber dynamics is a random time evolution of a spin system, such as the [[Ising model|R0KGM32QN6]], in which one spin at a time is updated.
The chosen spin is redrawn from its conditional law given all the other spins under the [[Gibbs measure|DG9F3W6MZM]].
The dynamics is a reversible [[Markov chain|0G48PYM96Q]] whose equilibrium is the Gibbs measure.
So it is both a model of relaxation to equilibrium and a [[Markov chain Monte Carlo|ZGNBR2SPZ0]] method.
Its speed of convergence is closely tied to phase transitions of the model.

## Explanations

### L1 human

Think of a grid of small magnets, each pointing up or down.
At each step, pick one magnet at random and let it choose its direction again, preferring to agree with its neighbours more strongly when the temperature is low.
Repeating this many times, the grid settles into the typical pictures of the Ising model at that temperature.
At high temperature the grid quickly looks like noise; at low temperature large patches of agreeing magnets form and change only slowly.
