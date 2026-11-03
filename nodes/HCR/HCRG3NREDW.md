---
tag: HCRG3NREDW
kind: definition
name: Combustion theory
msc: [80A25, 76V05]
defines: SXSCYXH068
uses: [F2JRWJNYN4, TAAHWE917M, DG49VBBT91]
sources:
  - url: https://en.wikipedia.org/wiki/Combustion
---

## Definition

Consider a gas mixture that fills a region of $\R^3$ and moves with a velocity field $\mathbf{u}(x, t)$.
Let $T(x, t)$ be its temperature and $Y(x, t) \in [0, 1]$ the mass fraction of a fuel that burns in one irreversible step.
*Combustion theory* is the study of the reacting flow equations, of which the basic model is
$$\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T = \kappa \Delta T + \frac{q}{c_p} \, \omega, \qquad \frac{\partial Y}{\partial t} + \mathbf{u} \cdot \nabla Y = D \Delta Y - \omega,$$
with the Arrhenius reaction rate
$$\omega = B \, Y \exp\!\left( -\frac{E}{R T} \right).$$
Here $\kappa > 0$ is the thermal diffusivity, $D > 0$ the diffusivity of the fuel and $c_p$ the specific heat.
The constant $q > 0$ is the heat released per unit mass of fuel, and $B > 0$ is a rate constant.
Finally, $E > 0$ is the activation energy and $R$ is the gas constant.
In the full theory, $\mathbf{u}$ and the density solve the compressible flow equations, coupled to $T$ through the heat release.

## Remarks

Each equation is an [[advection–diffusion equation|DG49VBBT91]] with a source, so the system is a [[reaction–diffusion system|TAAHWE917M]] carried by the flow.
Example: a gas at rest with $Y \equiv 0$ and $T$ constant is a solution, since then $\omega = 0$ and all derivatives vanish; this is the fully burnt state.
Non-example: an inert mixing problem with $B = 0$ has the same transport terms but no reaction, so it is not a combustion problem.
The ratio $E/(R T)$ is large at flame temperatures, which makes $\omega$ switch on sharply.
The Zeldovich number $\beta = E (T_b - T_u)/(R T_b^2)$, with $T_u$ and $T_b$ the unburnt and burnt temperatures, measures this sharpness.
The limit $\beta \to \infty$, called large activation energy asymptotics, reduces flames to moving surfaces.
The ratio $\mathrm{Le} = \kappa / D$ is the Lewis number.
