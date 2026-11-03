---
tag: EW2FBPAXEW
kind: example
name: Majumdar–Ghosh model
msc: [82B20, 82B23, 82D40]
instance_of: [PAEME5EQRM]
uses: [5QG15H8P5J, PAEME5EQRM]
sources:
  - url: https://en.wikipedia.org/wiki/Majumdar–Ghosh_model
same_as:
  wikidata: Q6738495
  wikipedia: Majumdar–Ghosh model
---

## Example

Let $L \ge 4$ be even and consider a ring of $L$ spins $\tfrac12$ with spin operators $\mathbf{S}_j$ and $\mathbf{S}_{j + L} = \mathbf{S}_j$.
For $J > 0$, the *Majumdar–Ghosh model* (1969) has Hamiltonian
$$H = J \sum_{j=1}^{L} \Big( \mathbf{S}_j \cdot \mathbf{S}_{j+1} + \tfrac12\, \mathbf{S}_j \cdot \mathbf{S}_{j+2} \Big).$$
It is a [[quantum Heisenberg model|5QG15H8P5J]] chain with next-nearest-neighbour coupling equal to half the nearest-neighbour coupling.
Check: with $\mathbf{T}_j = \mathbf{S}_{j-1} + \mathbf{S}_j + \mathbf{S}_{j+1}$, summing $\mathbf{T}_j^2 = \tfrac94 + 2(\mathbf{S}_{j-1}\cdot\mathbf{S}_j + \mathbf{S}_j\cdot\mathbf{S}_{j+1} + \mathbf{S}_{j-1}\cdot\mathbf{S}_{j+1})$ over $j$ gives
$$H = \frac{J}{4}\sum_{j=1}^{L} \mathbf{T}_j^2 - \frac{9}{16} J L.$$
Three spins $\tfrac12$ have total spin $\tfrac12$ or $\tfrac32$, so $\mathbf{T}_j^2 \ge \tfrac34$ and $H \ge -\tfrac38 J L$.

## Remarks

The two dimer states, in which the pairs $(1,2), (3,4), \dots$ or the pairs $(2,3), (4,5), \dots, (L,1)$ form singlets, attain this bound.
In each triple $j-1, j, j+1$, two of the three spins form a singlet, so $\mathbf{T}_j^2 = \tfrac34$.
So both dimer states are ground states with energy $-\tfrac38 JL$, and the ground state spontaneously breaks translation symmetry in the infinite chain.
It was later shown that the model has a spectral gap above these ground states.
The model is a frustrated chain and a basic example of a valence-bond solid with an exactly known ground state.

## Explanations

### L1 human

In this chain each spin interacts with its nearest and next-nearest neighbours, and the second coupling is exactly half the first.
At this special ratio the lowest-energy state can be written down by hand: spins pair up into singlets, like dancers in couples.
There are two ways to pair them, shifted by one site, and both have the same lowest energy.
