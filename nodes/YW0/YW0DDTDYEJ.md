---
tag: YW0DDTDYEJ
kind: definition
name: Grand potential
msc: [80A10, 82B30]
defines: PAYJBE73G4
uses: [F6JVQ12X43, SPY89W0RJ7, AJ8M9MGZGF, WVH4PVW64P, JXKY6C8JTA]
sources:
  - url: https://en.wikipedia.org/wiki/Grand_potential
---

## Definition

Let a thermodynamic system of one substance be in equilibrium.
Let $U$ be its [[internal energy|F6JVQ12X43]], $T$ its [[thermodynamic temperature|AJ8M9MGZGF]] and $S$ its [[entropy|SPY89W0RJ7]].
Let $N$ be its number of particles and $\mu$ its [[chemical potential|WVH4PVW64P]].
Its *grand potential* is
$$\Omega = U - TS - \mu N = F - \mu N,$$
where $F = U - TS$ is the [[Helmholtz free energy|JXKY6C8JTA]].
For several substances with amounts $N_i$ and chemical potentials $\mu_i$, $\Omega = U - TS - \sum_i \mu_i N_i$.

## Remarks

From $dU = T \, dS - p \, dV + \mu \, dN$ one gets $d\Omega = -S \, dT - p \, dV - N \, d\mu$, where $p$ is the pressure and $V$ the volume.
So the natural variables of $\Omega$ are $T$, $V$ and $\mu$, and $N = -(\partial \Omega / \partial \mu)_{T, V}$.
For a homogeneous system, the Euler relation $U = TS - pV + \mu N$ gives $\Omega = -pV$.
Example: for a classical ideal gas, $\Omega = -pV = -NkT$, where $k$ is the Boltzmann constant.
Non-example: $F + \mu N$ is not the grand potential, since the sign of $\mu N$ is wrong and its natural variables would not be $T, V, \mu$.

## Explanations

### L1 human

The grand potential is the Helmholtz free energy minus chemical potential times particle number.
It is the right potential when temperature, volume and chemical potential are held fixed.
