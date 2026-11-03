---
tag: XZTM94H0BE
kind: definition
name: Gibbs entropy
msc: [82B03, 94A17, 82B30]
defines: 1SFZNN31JW
uses: [M0JYTP1C8B, 0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_(statistical_thermodynamics)
---

## Definition

Let a [[statistical ensemble|M0JYTP1C8B]] be a [[probability distribution|0DVDCMA2DK]] $(p_i)_{i \in I}$ on a countable set $I$ of microstates.
Let $k_B$ be the Boltzmann constant.
The *Gibbs entropy* of the ensemble is
$$S = -k_B \sum_{i \in I} p_i \ln p_i,$$
with the convention $0 \ln 0 = 0$; the sum lies in $[0, \infty]$.
For a classical ensemble with density $\rho$ on phase space, one sets $S = -k_B \int \rho \ln (h^{3N} \rho) \, d\Gamma$, where $h^{3N}$ is a fixed unit of phase-space volume.

## Remarks

Example: the uniform distribution on $W$ states has $p_i = 1/W$, so $S = -k_B \sum_{i=1}^{W} \frac{1}{W} \ln \frac{1}{W} = k_B \ln W$.
A distribution concentrated on one state has $S = 0$.
Non-example: the weights $q_i = 1/2$ on three states sum to $3/2$, so they are not a probability distribution and their Gibbs entropy is not defined.
For a quantum ensemble with density operator $\rho$, the analogue is the von Neumann entropy $-k_B \tr(\rho \ln \rho)$.
The continuous version depends on the choice of the unit $h$ and can be negative, unlike the discrete one.
