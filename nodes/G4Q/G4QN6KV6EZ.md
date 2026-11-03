---
tag: G4QN6KV6EZ
kind: concept
name: Distributed parameter system
msc: [93C20, 93C25]
sources:
  - url: https://en.wikipedia.org/wiki/Distributed_parameter_system
same_as:
  wikidata: Q1482001
  wikipedia: Distributed parameter system
---

## Summary

A distributed parameter system is a control system whose state is a function of space, so that its state space is infinite-dimensional.
Such systems are usually governed by [[partial differential equations|GC5BDZ6QBC]], such as the heat equation, the wave equation or the equations of fluid flow.
They are opposed to lumped parameter systems, whose state is a finite vector governed by ordinary differential equations.
Their control theory uses operator semigroups on Hilbert spaces, and notions such as controllability split into exact and approximate versions.

## Explanations

### L1 human

The temperature in a metal rod is not one number but a whole profile along the rod.
If heaters along the rod are the input, the controlled object is this entire profile, which changes according to the heat equation.
That is a distributed parameter system: the quantities are spread out in space.
A single well-mixed tank of water, described by one temperature, is instead a lumped system.
