---
tag: 1DHYFN8KT5
kind: concept
name: Density matrix renormalization group
msc: [82B20, 65Z05, 81P40]
sources:
  - url: https://en.wikipedia.org/wiki/Density_matrix_renormalization_group
same_as:
  wikidata: Q5259335
  wikipedia: Density matrix renormalization group
---

## Summary

The density matrix renormalization group (DMRG) is a numerical method that finds low-energy states of quantum lattice systems, above all one-dimensional chains.
It was introduced by Steven White in 1992.
In modern form it minimises the energy over [[matrix product states|H578T160KS]] of a fixed bond dimension, optimising one or two sites at a time.
It keeps, at each cut of the chain, the states of largest weight in the reduced density matrix, which is where its name comes from.

## Explanations

### L1 human

The exact ground state of a chain of $N$ spins lives in a space of dimension $2^N$, which is hopeless for $N = 100$.
DMRG only searches among states that can be written with matrices of a bounded size $D$.
It sweeps back and forth along the chain, and at each site it improves the local matrices while keeping the others fixed.
At each step it throws away the directions that carry the least weight in the reduced density matrix of one half of the chain.
For gapped chains the answers are often accurate to many digits with a modest $D$.
