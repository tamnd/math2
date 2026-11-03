---
tag: PF8BST0MZ9
kind: definition
name: Statistical mechanics
msc: [82B03, 82B05, 82C03]
defines: X3QSEMFQWW
uses: [S1NST0AG71, M0JYTP1C8B, CPEC2NW2KF, MPM0RHWCN6, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Statistical_mechanics
---

## Definition

*Statistical mechanics* is the part of mathematical physics that studies systems of many interacting components through probability.
A model of statistical mechanics consists of the following data.

1. A set $\Omega$ of [[microstates|S1NST0AG71]], such as the [[phase space|CPEC2NW2KF]] of $N$ particles or the set of spin configurations on a finite graph.
2. An energy function, the Hamiltonian $H \colon \Omega \to \R$, as in [[Hamiltonian mechanics|MPM0RHWCN6]].
3. A [[statistical ensemble|M0JYTP1C8B]], that is, a probability measure on $\Omega$ built from $H$ and from macroscopic parameters such as temperature, volume and particle number.

A macroscopic observable is a function $A \colon \Omega \to \R$, and its predicted value is its [[expected value|0WQNRCNY3M]] under the ensemble.
Equilibrium statistical mechanics studies ensembles that do not change in time; nonequilibrium statistical mechanics studies how distributions evolve.

## Remarks

Example: for $N$ independent spins $\sigma_i \in \set{-1, +1}$ in a magnetic field $h$, take $\Omega = \set{-1, +1}^N$ and $H(\sigma) = -h \sum_i \sigma_i$.
The canonical ensemble at inverse temperature $\beta$ gives the mean magnetization per spin $\tanh(\beta h)$, since each spin is $+1$ with probability $e^{\beta h} / (e^{\beta h} + e^{-\beta h})$.
Non-example: a single planet moving around the sun is a mechanical system.
It carries no probability distribution over states, so it is not a model of statistical mechanics in this sense.
In quantum statistical mechanics the set $\Omega$ is replaced by a Hilbert space and the probability measure by a density operator.
