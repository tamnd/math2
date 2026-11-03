---
tag: 6JPP9KNXHF
kind: concept
name: Faddeev equations
msc: [81U10]
sources:
  - url: https://en.wikipedia.org/wiki/Faddeev_equations
same_as:
  wikidata: Q3777171
  wikipedia: Faddeev equations
---

## Summary

The Faddeev equations are a system of linear equations for a quantum system of three particles with pairwise interactions.
They split the three-body transition operator, or the wave function, into three components, one for each interacting pair.
Unlike the direct three-body Lippmann–Schwinger equation, their kernel becomes compact after iteration.
So Fredholm theory applies, and the equations have a unique solution in the generic case.
They are the basis of the rigorous three-body [[scattering theory|CSHWP5PK4P]] and of practical computations in nuclear and atomic physics.

## Explanations

### L1 human

With two particles, a collision is a single encounter.
With three, one pair can interact while the third particle flies by untouched, and this makes the naive equations ill-behaved.
Faddeev's idea is to split the process into three parts.
They are the parts in which the last interaction was between particles 2 and 3, between 3 and 1, and between 1 and 2.
Each part is built from the known two-body scattering of its pair, and the three parts feed into each other.
For example, the bound states of three nucleons, such as the triton, are computed in this way.
