---
tag: G1P1A0N7NZ
kind: concept
name: Canonical ensemble
msc: [82B03, 82B05]
specializes: [M0JYTP1C8B]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_ensemble
same_as:
  wikidata: Q1077753
  wikipedia: Canonical ensemble
---

## Summary

The canonical ensemble describes a system with a fixed number of particles in contact with a heat bath at a fixed temperature $T$.
It gives each [[microstate|S1NST0AG71]] of energy $E$ a weight proportional to $e^{-E / (k_B T)}$, the [[Boltzmann distribution|GYNMZ9201M]].
The normalizing constant $Z$ is the [[partition function|0CV69WDRXW]], and the free energy $F = -k_B T \ln Z$ gives all thermodynamic quantities by differentiation.
It is the ensemble used most often in calculations, because independent parts of a system give independent factors of $Z$.

## Explanations

### L1 human

Put a small cup of tea in a large room.
Energy flows back and forth between them, so the energy of the tea is not fixed, but its temperature settles at that of the room.
In the canonical ensemble, high-energy states are possible but exponentially unlikely.
For one atom with two levels of energy $0$ and $\varepsilon$, the upper level has probability $e^{-\varepsilon / (k_B T)} / (1 + e^{-\varepsilon / (k_B T)})$.
At low temperature this is almost $0$, and at very high temperature it is almost $1/2$.
