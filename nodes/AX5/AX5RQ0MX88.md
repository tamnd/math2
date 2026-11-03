---
tag: AX5RQ0MX88
kind: definition
name: Fluid mechanics
msc: [76A02, 76-01]
defines: H27M44BV4M
uses: [0299VCW1TH, PV8DQ41Q55]
sources:
  - url: https://en.wikipedia.org/wiki/Fluid_mechanics
---

## Definition

A *fluid* is a material that deforms without limit under any shear stress, however small.
In the continuum model, a fluid fills a region $\Omega \subseteq \R^3$.
At each time $t$ it is described by a density field $\rho(x, t) > 0$, a velocity [[vector field|0299VCW1TH]] $\mathbf{u}(x, t)$ and a pressure field $p(x, t)$.
*Fluid mechanics* is the branch of mechanics that studies these fields through the conservation laws of mass, momentum and energy, written as [[partial differential equations|PV8DQ41Q55]].
It consists of fluid statics, where $\mathbf{u} = 0$, and fluid dynamics, where the fluid moves.

## Remarks

Example: in a fluid at rest of constant density $\rho$ under gravity $g$, the balance of forces gives $\partial p / \partial z = -\rho g$, so $p = p_0 - \rho g z$ with $z$ the height.
This is a problem of fluid statics.
Non-example: a steel beam under a small shear stress deforms by a fixed small amount and then stops, so it is a solid and not a fluid.
The continuum model fails when the mean free path of the molecules is comparable to the size of the flow, as in very thin gases.
