---
tag: F2SMTMBDP0
kind: concept
name: Wardrop equilibrium
msc: [90B20, 91A14, 90C35]
sources:
  - url: https://en.wikipedia.org/wiki/Wardrop_equilibrium
same_as:
  wikidata: Q123752521
  wikipedia: Wardrop equilibrium
---

## Summary

A Wardrop equilibrium is the state of traffic in a network when every driver uses a quickest route given the choices of all others.
Each driver is so small that alone it does not change travel times, which depend on the total flow on each road.
At equilibrium, all used routes between the same origin and destination have equal travel time, and no unused route is quicker.
It was formulated by John Glen Wardrop in 1952.
It is the basic model of selfish routing, a [[Nash equilibrium|745WYP9YJ0]] of a game with infinitely many players.

## Explanations

### L1 human

Imagine a city where every commuter picks the fastest way to work.
If one road were faster than another used road, some drivers would switch, and the extra traffic would slow it down.
Switching stops when all used roads take the same time.
For example, take two roads: one always takes $1$ hour, and the other takes $x$ hours when a fraction $x$ of drivers uses it.
Then everyone takes the second road, and all travel $1$ hour.
