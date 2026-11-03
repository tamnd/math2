---
tag: ZCMQGKHGSV
kind: definition
name: Microcanonical ensemble
msc: [82B03, 82B05]
defines: TDGEGWHXCT
uses: [M0JYTP1C8B, S1NST0AG71, CPEC2NW2KF, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Microcanonical_ensemble
---

## Definition

Let $\Omega$ be the set of [[microstates|S1NST0AG71]] of a system and let $H \colon \Omega \to \R$ be its energy.

1. Discrete case: let $\Omega$ be countable and let $E$ be a value of $H$ with $W(E) = \#\set{\omega \in \Omega : H(\omega) = E}$ finite. The *microcanonical ensemble* at energy $E$ is the uniform distribution on $\set{H = E}$: it gives each such $\omega$ the probability $1 / W(E)$.
2. Classical case: let $\Omega = \Gamma$ be a [[phase space|CPEC2NW2KF]] $\R^{2n}$ with [[Lebesgue measure|2Z2QVWZ262]] (Liouville measure) $d\Gamma$. Fix $E$ and a width $\delta > 0$, and let $\Gamma_{E, \delta} = \set{x \in \Gamma : E \le H(x) < E + \delta}$ have finite positive measure. The microcanonical ensemble is the uniform probability measure on $\Gamma_{E, \delta}$, with density $\mathbf{1}_{\Gamma_{E, \delta}} / \abs{\Gamma_{E, \delta}}$.

It is a [[statistical ensemble|M0JYTP1C8B]] in which the energy, the volume and the number of particles are fixed.

## Remarks

Example: take $N$ two-level units, each with energy $0$ or $\varepsilon > 0$, and the total energy $E = K \varepsilon$ with $0 \le K \le N$.
Then $W(E) = \binom{N}{K}$, and each configuration with exactly $K$ excited units has probability $1 / \binom{N}{K}$.
Non-example: the distribution that gives the configuration with $K$ excited units probability proportional to $e^{-\beta K \varepsilon}$ is not microcanonical, since it spreads over many energies.
In the classical case one may also let $\delta \to 0$ and use the measure $d\sigma / \abs{\nabla H}$ on the surface $H = E$, where $d\sigma$ is surface measure.
The microcanonical entropy is $S(E) = k_B \ln W(E)$, with $k_B$ the Boltzmann constant.
