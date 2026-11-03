---
tag: 1DGJYHG10E
kind: concept
name: Mean-field theory
msc: [82B26, 82B20, 82B27]
sources:
  - url: https://en.wikipedia.org/wiki/Mean-field_theory
same_as:
  wikidata: Q626011
  wikipedia: Mean-field theory
---

## Summary

Mean-field theory approximates a system of many interacting parts by independent parts, each of which feels only the average effect of the others.
For a lattice spin system it replaces the Gibbs measure by the best product measure, which leads to a self-consistency equation for the magnetization.
It is exact for models in which every spin interacts weakly with all others.
For short-range models, it gives the correct critical behaviour above the [[upper critical dimension|BRYCFH5RB2]].
It is the first approximation used for a new model and gives a first picture of its phase diagram.

## Explanations

### L1 human

Think of a crowd where each person decides what to do by looking at what everyone else does on average.
A spin in a magnet does the same in mean-field theory: it ignores the detailed state of its neighbours and responds to their average magnetization $m$.
This gives one equation for $m$, namely $m = \tanh(\beta z J m)$ for an Ising magnet whose spins have $z$ neighbours each.
For small $\beta$ the only solution is $m = 0$.
For $\beta z J > 1$ two more solutions $\pm m_0$ appear, and the magnet is ordered.
