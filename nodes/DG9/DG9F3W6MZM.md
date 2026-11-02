---
tag: DG9F3W6MZM
kind: concept
name: Gibbs measure
msc: ["37D35", "82B05", "37B10"]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_measure
same_as:
  wikidata: Q2510435
  wikipedia: Gibbs measure
---

## Summary

A Gibbs measure is a probability measure in which the weight of a configuration is proportional to $e^{-\text{energy}}$.
It comes from statistical mechanics, where it describes a system in thermal equilibrium.
In dynamics, the thermodynamic formalism uses Gibbs measures on [[shift spaces|A1XE59ZHNM]].
There the measure of a cylinder of length $n$ is comparable to the exponential of a Birkhoff sum of a potential.
For a Hölder potential on a mixing [[subshift of finite type|624XDXX8FN]] the Gibbs measure is unique and is the equilibrium state of the potential.

## Explanations

### L1 human

Imagine a long row of coins, and give each possible row an energy.
A Gibbs measure picks rows at random so that low-energy rows are more likely, with odds given by the exponential of minus the energy.
In dynamics the "row" is the sequence of regions an orbit visits, and the energy is the sum of a function along the orbit.
On the full shift on two symbols, when the function is constant, every block of $n$ symbols gets the same weight, and one gets fair coin tossing.
