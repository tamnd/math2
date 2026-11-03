---
tag: H5PQFQS6CE
kind: concept
name: Block spin transformation
msc: [82B28, 82B20]
specializes: [5XTSCZCF7Z]
sources:
  - url: https://en.wikipedia.org/wiki/Renormalization_group
---

## Summary

A block spin transformation is a coarse-graining step for a [[lattice model|PAEME5EQRM]] of spins.
It groups the spins into blocks of side $b$ and replaces each block by one new spin, for example by majority vote.
The new spins live on a coarser lattice, and their law defines a new effective Hamiltonian.
Repeating this step is the prototype of a real-space [[renormalization group|5XTSCZCF7Z]] transformation, introduced by Leo Kadanoff.

## Explanations

### L1 human

Look at a black and white picture of an [[Ising model|R0KGM32QN6]] from far away: small details blur, and only large patches remain.
A block spin transformation does this blurring in a controlled way.
On the square lattice with $b = 3$, each $3 \times 3$ square of nine spins becomes a single spin.
That spin is $+1$ if most of the nine spins are $+1$, and $-1$ otherwise.
So a block with six spins $+1$ and three spins $-1$ becomes one spin $+1$.
The new picture has nine times fewer spins, but it keeps the large-scale shape of the old one.
