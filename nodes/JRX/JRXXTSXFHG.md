---
tag: JRXXTSXFHG
kind: concept
name: Debye–Hückel theory
msc: [82D15, 82D10]
sources:
  - url: https://en.wikipedia.org/wiki/Debye%E2%80%93H%C3%BCckel_theory
same_as:
  wikidata: Q3526757
  wikipedia: Debye–Hückel theory
---

## Summary

Debye–Hückel theory describes dilute solutions of ions, such as salt dissolved in water.
It combines [[Poisson's equation in electrostatics|FC64B1A65B]] with the [[Boltzmann distribution|GYNMZ9201M]] of the ions and linearizes the result.
Its main prediction is screening: the potential of an ion decays like $e^{-r/\lambda_D}/r$, where $\lambda_D$ is the [[Debye length|ZSNW9FC08R]].
It also gives the activity coefficient of the ions in very dilute solutions.
Its logarithm decreases like the square root of the ionic strength.

## Explanations

### L1 human

In salt water each positive ion attracts a small cloud of negative ions around it, and the other way round.
Seen from far away, the ion and its cloud almost cancel, so the electric field of the ion is hidden.
Debye–Hückel theory computes the shape of this cloud by treating the ions as point charges at thermal equilibrium whose electric energy is small compared to their thermal energy.
The result is that the potential of the ion falls off exponentially beyond a distance called the Debye length.
For table salt at $0.1$ mol per litre in water at room temperature, this distance is about one nanometre.
