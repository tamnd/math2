---
tag: Y87ATBGP9T
kind: definition
name: Poroelasticity
msc: [74F10, 76S05, 74L10]
defines: 987R9XR8KH
uses: [6W00ZECYT0, 80737NDZ4V, 8QS6QMJF5Z, KG2XWEMJ30, DX8RV2XG6H]
sources:
  - url: https://en.wikipedia.org/wiki/Poroelasticity
---

## Definition

Consider a fluid-saturated porous solid with displacement $u$ of the solid skeleton and [[infinitesimal strain|8QS6QMJF5Z]] $\varepsilon = \tfrac12 (\nabla u + \nabla u^T)$.
Let $\sigma$ be the total [[stress|KG2XWEMJ30]] (tension positive), $p$ the pore pressure, and $\zeta$ the variation of fluid content per unit volume.
Let $\lambda, \mu$ be the drained [[Lamé parameters|80737NDZ4V]] of the skeleton, $\alpha \in (0, 1]$ the Biot coefficient and $M > 0$ the Biot modulus.
Let $k > 0$ be the permeability and $\eta_f > 0$ the fluid viscosity.
*Linear isotropic poroelasticity* is the system of the following four relations, with body force $f$.

1. Stress law: $\sigma = \lambda (\tr \varepsilon) I + 2\mu \varepsilon - \alpha p I$.
2. Fluid content: $\zeta = \alpha \tr \varepsilon + p / M$.
3. [[Darcy's law|DX8RV2XG6H]] for the fluid flux $q$ relative to the solid: $q = -(k/\eta_f) \nabla p$.
4. Balance laws: $\nabla \cdot \sigma + f = 0$ and $\partial \zeta / \partial t + \nabla \cdot q = 0$.

## Remarks

Example: a uniform state with constant pore pressure $p_0$ and strain $\varepsilon = \frac{\alpha p_0}{3\lambda + 2\mu} I$ has $\sigma = 0$ by (1).
With $q = 0$ and constant $\zeta$, it satisfies (1) to (4) with $f = 0$: the pore pressure inflates the free skeleton.
Non-example: if $\alpha = 0$, the pore pressure leaves the stress law and the fluid content no longer depends on the strain.
Solid and fluid then decouple into plain [[linear elasticity|6W00ZECYT0]] and pressure diffusion, so there is no poroelastic coupling.
The quantity $\sigma + \alpha p I$ is Biot's effective stress, the part of the stress carried by the skeleton.
When the solid grains and the fluid are incompressible compared with the skeleton, $\alpha = 1$ and $1/M = 0$.
