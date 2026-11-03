---
tag: PJFC3HJEDK
kind: definition
name: Bose–Einstein statistics
msc: [82B10, 81V73]
defines: R5HWSRAK4H
uses: [1C5S72A9JX]
sources:
  - url: https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_statistics
---

## Definition

Consider a system of non-interacting identical particles in the [[grand canonical ensemble|1C5S72A9JX]] at temperature $T > 0$ and chemical potential $\mu$.
Let $k_B$ be the Boltzmann constant and $\beta = 1/(k_B T)$.
Assume that $\mu < \varepsilon$ for every single-particle energy $\varepsilon$.
The particles obey *Bose–Einstein statistics* if each single-particle state can hold any number $n = 0, 1, 2, \ldots$ of particles.
States that differ only by a permutation of the particles count as the same state.
Then the mean occupation number of a single-particle state of energy $\varepsilon$ is
$$\bar n(\varepsilon) = \frac{1}{e^{\beta (\varepsilon - \mu)} - 1}.$$

## Remarks

The grand partition function of one state is the geometric series $\sum_{n \ge 0} e^{-n\beta(\varepsilon - \mu)} = 1/(1 - e^{-\beta(\varepsilon - \mu)})$.
It converges exactly when $\varepsilon > \mu$, which is why $\mu$ must lie below every energy level.
Taking the mean of $n$ with these weights gives the formula above.

Example: for photons $\mu = 0$, and a mode of energy $\varepsilon = k_B T \ln 2$ has $\bar n = 1/(2 - 1) = 1$.

Non-example: if $\mu > \varepsilon$ for some level, the series diverges and no equilibrium state exists, so the hypothesis $\mu < \varepsilon$ cannot be dropped.
When $\mu$ approaches the lowest level, the occupation of that level grows without bound; this is the mechanism behind Bose–Einstein condensation.

When $\beta(\varepsilon - \mu) \gg 1$, $\bar n$ is close to the [[Maxwell–Boltzmann|B60C1S87XB]] value $e^{-\beta(\varepsilon - \mu)}$.
