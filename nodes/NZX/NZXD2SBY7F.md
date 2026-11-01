---
tag: NZXD2SBY7F
kind: concept
name: Coupling from the past
msc: [65C05, 60J10, 60J22]
sources:
  - url: https://en.wikipedia.org/wiki/Coupling_from_the_past
same_as:
  wikidata: Q5178037
  wikipedia: Coupling from the past
---

## Summary

Coupling from the past is an algorithm due to Propp and Wilson.
It produces an exact sample from the [[stationary distribution|0KRH5157WP]] of an ergodic finite [[Markov chain|0G48PYM96Q]].
It runs copies of the chain from all states, starting further and further in the past with the same randomness.
It stops when all copies agree at time $0$.
Unlike ordinary [[Markov chain Monte Carlo|ZGNBR2SPZ0]], its output has exactly the stationary law, with no bias from stopping too early.

## Explanations

### L1 human

Imagine the chain has been running since the infinite past, so that today it is exactly in equilibrium.
If all possible starting states at some past time lead, with the same random choices, to the same state today, then that state is what the eternal chain shows today.
The algorithm looks further back in time until this happens.
The trick is to reuse the same random numbers for each past time step whenever one restarts from further back.
For chains with an order that the update preserves, it suffices to follow only the top and the bottom states.
