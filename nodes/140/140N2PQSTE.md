---
tag: 140N2PQSTE
kind: concept
name: Rate function
msc: [60F10]
sources:
  - url: https://en.wikipedia.org/wiki/Rate_function
same_as:
  wikidata: Q7295534
  wikipedia: Rate function
---

## Summary

A rate function is a lower semicontinuous function $I$ from a topological space to $[0, \infty]$.
In [[large deviations theory|Q702WCDQQ3]], it gives the exponential rate at which the probability of a rare event decays: roughly, $P(Z_n \approx x) \approx e^{-n I(x)}$.
It is called good when its sublevel sets are compact.
Examples are the Legendre transforms in [[Cramér's theorem|RZZK51CXMN]] and the [[Kullback–Leibler divergence|PQBW43X5RE]] in [[Sanov's theorem|QWEF2WAXJM]].

## Explanations

### L1 human

A rate function measures how costly it is for a random system to end up at a given state.
The typical state costs nothing, and states far from typical cost more.
The probability of a state falls like $e^{-n \cdot \text{cost}}$, where $n$ is the size of the system.
For the average of $n$ standard normal variables, the cost of the value $x$ is $x^2/2$.
