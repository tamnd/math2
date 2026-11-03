---
tag: PTYDXT3MJV
kind: definition
name: K-epsilon turbulence model
msc: [76F60, 76F55]
defines: S7RYQN3T1H
uses: [4EYAHQDA7Q, 4K9W1VP58R, FDQE4PF63G, V47TX9AFKF]
sources:
  - url: https://en.wikipedia.org/wiki/K-epsilon_turbulence_model
---

## Definition

Consider an incompressible turbulent flow with kinematic viscosity $\nu$, mean velocity $\bar u_i$ and fluctuations $u_i'$ from the [[Reynolds decomposition|V47TX9AFKF]].
Let $k = \frac12 \overline{u_i' u_i'}$ be the turbulent kinetic energy and $\varepsilon = \nu \, \overline{(\partial u_i' / \partial x_j)(\partial u_i' / \partial x_j)}$ its dissipation rate.
The standard *$k$–$\varepsilon$ model* closes the [[Reynolds-averaged Navier–Stokes equations|4EYAHQDA7Q]] as follows.

1. The [[Reynolds stress|FDQE4PF63G]] is given by the [[Boussinesq eddy viscosity hypothesis|4K9W1VP58R]] with eddy viscosity $\nu_t = C_\mu k^2 / \varepsilon$.
2. The field $k$ satisfies
$$\frac{\partial k}{\partial t} + \bar u_j \frac{\partial k}{\partial x_j} = \frac{\partial}{\partial x_j} \left[ \left( \nu + \frac{\nu_t}{\sigma_k} \right) \frac{\partial k}{\partial x_j} \right] + P_k - \varepsilon.$$
3. The field $\varepsilon$ satisfies
$$\frac{\partial \varepsilon}{\partial t} + \bar u_j \frac{\partial \varepsilon}{\partial x_j} = \frac{\partial}{\partial x_j} \left[ \left( \nu + \frac{\nu_t}{\sigma_\varepsilon} \right) \frac{\partial \varepsilon}{\partial x_j} \right] + C_{1\varepsilon} \frac{\varepsilon}{k} P_k - C_{2\varepsilon} \frac{\varepsilon^2}{k}.$$

Here $P_k = -\overline{u_i' u_j'} \, \partial \bar u_i / \partial x_j$ is the production of turbulent kinetic energy, and $C_\mu$, $\sigma_k$, $\sigma_\varepsilon$, $C_{1\varepsilon}$, $C_{2\varepsilon}$ are positive constants.

## Remarks

The usual values, due to Launder and Spalding, are $C_\mu = 0.09$, $\sigma_k = 1.0$, $\sigma_\varepsilon = 1.3$, $C_{1\varepsilon} = 1.44$ and $C_{2\varepsilon} = 1.92$.
The $k$ equation is a modelled form of the exact transport equation for $k$, while the $\varepsilon$ equation is largely empirical.
Near walls the model needs wall functions or low-Reynolds-number modifications.

Example: in decaying homogeneous isotropic turbulence, $\bar u = 0$ and $P_k = 0$, so the model reduces to $k' = -\varepsilon$, $\varepsilon' = -C_{2\varepsilon} \varepsilon^2 / k$.
These have the solutions $k \propto t^{-n}$ with $n = 1 / (C_{2\varepsilon} - 1) \approx 1.09$, a decay rate in the range seen in grid turbulence experiments.
Non-example: a mixing-length model prescribes $\nu_t$ by an algebraic formula.
It has no transport equations for $k$ and $\varepsilon$, so it is a zero-equation model, not a $k$–$\varepsilon$ model.
