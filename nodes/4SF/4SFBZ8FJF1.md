---
tag: 4SFBZ8FJF1
kind: concept
name: Generalized Lotka–Volterra equation
msc: [92D25, 34C60, 92D40]
specializes: [1YEMFQ1H32]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Lotka%E2%80%93Volterra_equation
same_as:
  wikidata: Q5532443
  wikipedia: Generalized Lotka–Volterra equation
---

## Summary

The generalized Lotka–Volterra equation is a system of [[ordinary differential equations|0NT64JV96A]] for $n$ interacting species.
In it, the per capita growth rate of each species is an affine function of all population sizes.
It contains the classical [[Lotka–Volterra predator–prey equations|00Y5QZ82AA]] and the competition equations as special cases.
It is the basic model of community ecology, and it is equivalent to the replicator equation of evolutionary game theory.

## Explanations

### L1 human

Each species has its own growth rate, and each pair of species affects each other in a fixed way.
A predator gains from its prey and the prey loses from the predator; two competitors both lose; partners in a mutualism both gain.
The equation adds up all these effects, each proportional to the size of the other species.
For two species with $x' = x(1 - y)$ and $y' = y(-1 + x)$, the first species is prey and the second is its predator.
