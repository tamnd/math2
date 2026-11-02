---
tag: DMTFJY6CS0
kind: concept
name: Random dynamical system
msc: [37H05, 37H10, 37H12]
specializes: [BBZP1R872N]
sources:
  - url: https://en.wikipedia.org/wiki/Random_dynamical_system
same_as:
  wikidata: Q7291964
  wikipedia: Random dynamical system
---

## Summary

A random dynamical system is a [[dynamical system|BBZP1R872N]] whose rule of evolution is chosen at random at each time.
The randomness comes from a noise that is itself a measure-preserving dynamical system.
The evolution is a cocycle over the noise.
The state after time $s + t$ is obtained by first evolving for time $s$ and then evolving for time $t$ with the shifted noise.
Stochastic differential equations and random iterations of maps give random dynamical systems.
The framework allows notions of deterministic dynamics, such as attractors, invariant measures and [[Lyapunov exponents|NJ1FJSNK6A]], to be used for systems with noise.

## Explanations

### L1 human

Imagine moving a point by one of two maps, and choosing which map by tossing a coin each time.
Each sequence of coin tosses gives one sequence of maps, and the point follows the composition of these maps.
A random dynamical system keeps track of all coin sequences at once, together with their probabilities.
The rule that ties it together is simple.
Running for $s$ steps and then $t$ steps is the same as running for $s + t$ steps, as long as the coin tosses are read in the right order.
