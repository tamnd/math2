---
tag: 277YCHBJKH
kind: definition
name: Isothermal–isobaric ensemble
msc: [82B03, 82B05]
defines: M2EASY53HE
uses: [M0JYTP1C8B, G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Isothermal–isobaric_ensemble
---

## Definition

Consider a system of $N$ particles whose volume $V > 0$ can vary.
For each $V$, let $Z(N, V, \beta)$ be the [[canonical|G1P1A0N7NZ]] partition function in volume $V$ at $\beta = 1 / (k_B T) > 0$.
Let $P > 0$ be the pressure and let $V_0 > 0$ be a fixed reference volume.
Assume that the isothermal–isobaric partition function
$$\Delta(N, P, \beta) = \frac{1}{V_0} \int_0^\infty e^{-\beta P V} Z(N, V, \beta) \, dV$$
is finite.
The *isothermal–isobaric ensemble* is the [[statistical ensemble|M0JYTP1C8B]] on pairs $(V, \omega)$, where $\omega$ is a microstate in volume $V$.
Its joint weight is proportional to $e^{-\beta (H(\omega) + P V)}$, normalized by $V_0 \Delta$.
In particular the volume has probability density $e^{-\beta P V} Z(N, V, \beta) / (V_0 \Delta)$.

## Remarks

The Gibbs free energy is $G = -\beta^{-1} \ln \Delta$; the reference volume $V_0$ only shifts $G$ by a term that is negligible per particle.
Example: for a classical ideal gas, $Z(N, V, \beta) = c_N V^N$ with $c_N > 0$ independent of $V$.
Then $\Delta = c_N N! / (V_0 (\beta P)^{N + 1})$, and the volume has a gamma distribution with mean $\langle V \rangle = (N + 1) / (\beta P)$.
Non-example: the canonical ensemble at fixed $V$ is not of this form, since it gives probability $1$ to a single volume.
