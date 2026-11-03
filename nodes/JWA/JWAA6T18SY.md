---
tag: JWAA6T18SY
kind: definition
name: Extended irreversible thermodynamics
msc: [80A17, 82C35]
defines: ESAD60QZ72
uses: [WC6CK8PXPX, STR73R5MX4, SPY89W0RJ7, 1Y36434YTE]
sources:
  - url: https://en.wikipedia.org/wiki/Extended_irreversible_thermodynamics
---

## Definition

*Extended irreversible thermodynamics* is the theory of [[non-equilibrium thermodynamics|WC6CK8PXPX]] built on these assumptions.

1. The state variables are the classical ones, such as the specific internal energy $u$ and specific volume $v$, and the dissipative fluxes. Examples of fluxes are the [[heat flux|1Y36434YTE]] $q$ and the viscous stress.
2. There is a generalised specific [[entropy|SPY89W0RJ7]] $s(u, v, q, \dots)$, which agrees with the local equilibrium entropy when the fluxes are zero.
3. The fluxes obey first-order evolution equations, chosen so that the [[entropy production|STR73R5MX4]] of the generalised entropy is non-negative.

## Remarks

Example: for heat conduction in a rigid solid, take $s(u, q) = s_{eq}(u) - \frac{\tau}{2 \rho k T^2} \abs{q}^2$ with relaxation time $\tau > 0$, density $\rho$, conductivity $k > 0$ and temperature $T$.
Requiring non-negative entropy production in the simplest linear way gives the Maxwell–Cattaneo law
$$\tau \frac{\partial q}{\partial t} + q = -k \nabla T,$$
which reduces to Fourier's law when $\tau = 0$.
Non-example: classical linear irreversible thermodynamics with Fourier's law fails clause 1, since there $q$ is a function of $\nabla T$, not an independent variable.
