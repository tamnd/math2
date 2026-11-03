---
tag: T4FZCAQC0D
kind: concept
name: Mayer f-function
msc: [82B05, 82B21, 82D05]
sources:
  - url: https://en.wikipedia.org/wiki/Mayer_f-function
same_as:
  wikidata: Q3075227
  wikipedia: Mayer f-function
---

## Summary

The Mayer $f$-function of a pair potential $\varphi$ at inverse temperature $\beta$ is $f(x) = e^{-\beta \varphi(x)} - 1$.
It turns the Boltzmann factor of a pair of particles into a quantity that vanishes when the particles are far apart.
Expanding products of factors $1 + f$ gives sums over graphs.
This is the starting point of the [[cluster expansion|XH2XEVGNSK]] and of the virial expansion of a real gas.

## Explanations

### L1 human

Two molecules of a gas only feel each other when they are close.
The Boltzmann factor of their interaction is $1$ when they are far apart, so subtracting $1$ leaves a function that is zero at large distances.
This makes it a small quantity in a dilute gas, suitable for an expansion.
For hard spheres of diameter $\sigma$, the function is $-1$ when the centres are closer than $\sigma$ and $0$ otherwise.
