---
tag: ENWMTRJRND
kind: concept
name: Correlation function
msc: [82B05, 82B20, 60G60]
sources:
  - url: https://en.wikipedia.org/wiki/Correlation_function_(statistical_mechanics)
same_as:
  wikidata: Q5172856
  wikipedia: Correlation function (statistical mechanics)
---

## Summary

A correlation function of a statistical system measures how the values of a local quantity at several points depend on each other.
The basic one is the truncated two-point function $\langle \sigma_x \sigma_y \rangle - \langle \sigma_x \rangle \langle \sigma_y \rangle$ of a spin system.
Its rate of decay with the distance $\abs{x - y}$ defines the correlation length.
Away from a critical point it typically decays exponentially.
At a critical point it decays like a power, and the power gives a [[critical exponent|SQ41AZGZ2P]].

## Explanations

### L1 human

Flip a spin at one place in a magnet: how much does a spin far away notice?
The correlation function answers this question as a function of the distance between the two places.
In a hot magnet, the answer drops off fast, like $e^{-r/\xi}$ for a distance $r$, and $\xi$ is the size of a typical patch of aligned spins.
Near the critical point the patches become huge, and the drop becomes a slow power of $r$.
In a chain of Ising spins at zero field, the correlation of two spins at distance $n$ is $(\tanh \beta J)^n$.
