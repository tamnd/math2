---
tag: JSZRW5GQMC
kind: definition
name: Canonical ensemble
msc: [82B03, 82B05]
defines: G1P1A0N7NZ
uses: [M0JYTP1C8B, S1NST0AG71, GYNMZ9201M, CPEC2NW2KF]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_ensemble
---

## Definition

Let $\Omega$ be the set of [[microstates|S1NST0AG71]] of a system with a fixed number of particles, and let $H \colon \Omega \to \R$ be its energy.
Let $\beta = 1 / (k_B T) > 0$, where $T$ is the temperature and $k_B$ the Boltzmann constant.

1. Discrete case: let $\Omega$ be countable with $Z(\beta) = \sum_{\omega \in \Omega} e^{-\beta H(\omega)} < \infty$. The *canonical ensemble* gives $\omega$ the probability $p(\omega) = e^{-\beta H(\omega)} / Z(\beta)$.
2. Classical case: let $\Omega$ be the [[phase space|CPEC2NW2KF]] of $N$ identical particles in a box $V \subset \R^3$. Let $Z(\beta) = \frac{1}{N! \, h^{3N}} \int_{\Omega} e^{-\beta H} \, d\Gamma$ be finite, where $h > 0$ is a constant with the units of action. The canonical ensemble has density $e^{-\beta H} / (N! \, h^{3N} Z(\beta))$ with respect to Liouville measure $d\Gamma$.

The number $Z(\beta)$ is the canonical partition function, and $F = -\beta^{-1} \ln Z(\beta)$ is the Helmholtz free energy.

## Remarks

The canonical ensemble is the [[Boltzmann distribution|GYNMZ9201M]] applied to the microstates of the whole system.
It is a [[statistical ensemble|M0JYTP1C8B]] in which the temperature, the volume and the particle number are fixed.
Example: for $N$ independent two-level units with energies $0$ and $\varepsilon$, one gets $Z = (1 + e^{-\beta \varepsilon})^N$.
The mean energy is $\langle H \rangle = -\partial_\beta \ln Z = N \varepsilon / (e^{\beta \varepsilon} + 1)$.
Non-example: for a free particle on the whole line, $\int_\R \int_\R e^{-\beta p^2 / 2m} \, dq \, dp = \infty$, so no canonical ensemble exists; a finite box is needed.
In quantum statistical mechanics the canonical ensemble is the density operator $e^{-\beta H} / \tr e^{-\beta H}$, when $e^{-\beta H}$ is trace class.
