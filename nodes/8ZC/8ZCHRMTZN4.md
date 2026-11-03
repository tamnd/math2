---
tag: 8ZCHRMTZN4
kind: definition
name: Heat flux
msc: [80A19, 80A17]
defines: 1Y36434YTE
uses: [CY4GJQGF06, 0299VCW1TH, 026J1MG2NW]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_flux
---

## Definition

Let a body occupy an open set $\Omega \subseteq \R^3$, and let $I$ be a time interval.
The *heat flux* is a [[vector field|0299VCW1TH]] $\mathbf{q} \colon \Omega \times I \to \R^3$ with this property.
Let $S \subseteq \Omega$ be any oriented smooth surface with unit normal $\mathbf{n}$, and let $t \in I$.
Then the rate at which [[heat|CY4GJQGF06]] crosses $S$ in the direction of $\mathbf{n}$ is the [[flux|026J1MG2NW]]
$$\int_S \mathbf{q}(x, t) \cdot \mathbf{n}(x) \, dA(x).$$
Its unit is the watt per square metre.

## Remarks

Example: in a slab $0 < x_1 < L$ whose faces are held at temperatures $T_1 > T_2$, at steady state with constant conductivity $k$, the flux is $\mathbf{q} = \left(k (T_1 - T_2)/L, 0, 0\right)$.
Take a square of area $A$ parallel to the faces, with $\mathbf{n} = (1, 0, 0)$.
The heat rate through it is $k A (T_1 - T_2)/L > 0$, so heat goes from the hot face to the cold face.

Non-example: the total heat rate $Q$ through a wall, in watts, is not a heat flux.
It is the integral of the normal component of the flux, and it does not depend on a point.

Some texts call the scalar $q_n = \mathbf{q} \cdot \mathbf{n}$ on a given surface the heat flux.
The vector is also written $\mathbf{q}''$ or $\boldsymbol{\phi}$.
