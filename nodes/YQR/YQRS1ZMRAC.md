---
tag: YQRS1ZMRAC
kind: concept
name: BGK collision operator
msc: [82C40, 76P05, 35Q20]
sources:
  - url: https://en.wikipedia.org/wiki/Bhatnagar%E2%80%93Gross%E2%80%93Krook_operator
same_as:
  wikidata: Q4901423
  wikipedia: Bhatnagar–Gross–Krook operator
---

## Summary

The BGK collision operator is a simple model of the collision term of the [[Boltzmann equation|MH6CSWD7F0]].
It replaces the quadratic collision integral by a relaxation of the distribution function towards the local [[Maxwell–Boltzmann distribution|3QSVWQJX11]] with the same density, velocity and temperature.
It keeps the conservation of mass, momentum and energy and the H-theorem, but is much easier to analyse and to compute with.
It was introduced by Bhatnagar, Gross and Krook in 1954 and underlies the [[lattice Boltzmann method|PMGS1JJPHK]].
See the [[definition|DS66JCJS7Y]].

## Explanations

### L1 human

Collisions in a gas push the velocity distribution towards the bell-shaped equilibrium.
The BGK model keeps only this effect: at each place, the distribution moves towards the equilibrium bell curve at a fixed rate.
The equilibrium it aims at has the same density, average velocity and temperature as the gas at that place, so nothing is created or lost.
It is like a cup of coffee that cools towards room temperature at a rate proportional to the difference.
