---
tag: GNF88GT1BR
kind: definition
name: Grand canonical ensemble
msc: [82B03, 82B05]
defines: 1C5S72A9JX
uses: [M0JYTP1C8B, G1P1A0N7NZ, S1NST0AG71]
sources:
  - url: https://en.wikipedia.org/wiki/Grand_canonical_ensemble
---

## Definition

Let a system have, for each particle number $N \in \set{0, 1, 2, \dots}$, a countable set $\Omega_N$ of [[microstates|S1NST0AG71]] with energy $H_N \colon \Omega_N \to \R$.
Let $\beta = 1 / (k_B T) > 0$ and let $\mu \in \R$ be the chemical potential.
Assume that the grand partition function
$$\Xi(\beta, \mu) = \sum_{N \ge 0} \sum_{\omega \in \Omega_N} e^{-\beta (H_N(\omega) - \mu N)}$$
is finite.
The *grand canonical ensemble* is the probability distribution on the disjoint union of the $\Omega_N$ that gives $\omega \in \Omega_N$ the probability
$$p(N, \omega) = \frac{e^{-\beta (H_N(\omega) - \mu N)}}{\Xi(\beta, \mu)}.$$

## Remarks

Equivalently, $\Xi = \sum_{N} z^N Z_N(\beta)$, where $z = e^{\beta \mu}$ is the activity and $Z_N$ is the [[canonical|G1P1A0N7NZ]] partition function with $N$ particles.
For classical particles in a box, $Z_N$ is the canonical integral with the factor $1 / (N! \, h^{3N})$.
Example: a single site that is empty ($N = 0$, energy $0$) or holds one particle ($N = 1$, energy $\varepsilon$) has $\Xi = 1 + e^{-\beta (\varepsilon - \mu)}$.
Its mean occupation is $\langle N \rangle = 1 / (e^{\beta (\varepsilon - \mu)} + 1)$.
Non-example: for one bosonic mode of energy $\varepsilon$ with $\mu > \varepsilon$, the series $\sum_{N \ge 0} e^{-\beta (\varepsilon - \mu) N}$ diverges, so no grand canonical ensemble exists.
The grand potential is $\Phi = -\beta^{-1} \ln \Xi$, and for a homogeneous system $\Phi = -pV$, where $p$ is the pressure.
