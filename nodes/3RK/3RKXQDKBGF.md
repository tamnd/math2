---
tag: 3RKXQDKBGF
kind: definition
name: Displacement current
msc: [78A25, 35Q61]
defines: AZKM3NQ4VD
uses: [NJVXQZ780B, YZ7Q9DP8RT, HK2E8BX09G, 9BWWD4QK8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Displacement_current_density
---

## Definition

Let $D$ be the [[electric displacement field|NJVXQZ780B]] in a region of space, $C^1$ in time.
The *displacement current density* is the vector field
$$J_D = \frac{\partial D}{\partial t}.$$
In vacuum $D = \varepsilon_0 E$, where $E$ is the [[electric field|YZ7Q9DP8RT]] and $\varepsilon_0 > 0$ is the vacuum permittivity, so $J_D = \varepsilon_0 \, \partial E / \partial t$.
The *displacement current* through an oriented surface is the flux of $J_D$ through it.

## Remarks

With it the [[Ampère's circuital law|HK2E8BX09G]] becomes the Ampère–Maxwell law $\nabla \times H = J_f + J_D$ of [[Maxwell's equations|9BWWD4QK8Y]], where $J_f$ is the free current density.
Taking the divergence gives $\nabla \cdot J_f + \partial_t (\nabla \cdot D) = 0$, and Gauss's law $\nabla \cdot D = \rho_f$ turns this into the continuity equation for charge.
So the displacement term is exactly what makes the law consistent with conservation of charge.

Example: a capacitor with parallel plates of area $a$ in vacuum carries charges $\pm Q(t)$.
Neglecting edge effects, the field between the plates has size $Q / (\varepsilon_0 a)$, so the displacement current through a surface between the plates is $a \, \varepsilon_0 \, \frac{d}{dt} \frac{Q}{\varepsilon_0 a} = \frac{dQ}{dt}$.
This equals the conduction current $I$ in the wires.

Non-example: in electrostatics and magnetostatics the fields do not depend on time, so $J_D = 0$ and Ampère's original law holds.

Despite its name, the displacement current is not a flow of charge in vacuum.
