---
tag: GEYXNW1CE6
kind: definition
name: Microstate
msc: [82B03, 82B05]
defines: S1NST0AG71
uses: [CPEC2NW2KF, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Microstate_(statistical_mechanics)
---

## Definition

Consider a physical system made of many components.

1. Take a classical system of $N$ point particles in $\R^d$. A *microstate* is a point $(q_1, \dots, q_N, p_1, \dots, p_N)$ of the [[phase space|CPEC2NW2KF]] $\Gamma = \R^{dN} \times \R^{dN}$. Here $q_i$ is the position and $p_i$ the momentum of particle $i$.
2. Take a lattice model with a finite set $\Lambda$ of sites and a finite set $S$ of single-site values. A microstate is a configuration $\sigma \in S^\Lambda$.
3. Take a quantum system with [[Hilbert space|HM2HHE3J51]] $\mathcal{H}$. A microstate is a pure state, that is, a unit vector of $\mathcal{H}$ up to a phase. In counting arguments one uses the vectors of an orthonormal basis of energy eigenstates.

A *macrostate* is a set of microstates singled out by the values of a few macroscopic quantities.
Typical such quantities are the energy $E$, the volume $V$ and the number $N$ of particles.

## Remarks

Example: in a chain of $N$ spins with values in $S = \set{-1, +1}$, the configuration $(+1, -1, \dots, -1)$ is a microstate, and the set of configurations with $\sum_i \sigma_i = M$ is a macrostate.
That macrostate contains $\binom{N}{(N + M)/2}$ microstates when $N + M$ is even and lies in $[0, 2N]$.
Non-example: the pair $(E, V)$ of energy and volume of a gas is not a microstate, since it does not fix the position and momentum of each particle.
The number $W$ of microstates in a macrostate enters Boltzmann's formula $S = k_B \ln W$.
