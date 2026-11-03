---
tag: EDBPDTG7BS
kind: statement
role: proposition
name: Charge conservation
msc: [78A25, 35Q61]
uses: [9BWWD4QK8Y, 6XPSV47R56, 0MWV6ZTK6S, 0JX86PSSA9, 0F56CMMC5P]
about: [6XPSV47R56]
sources:
  - url: https://en.wikipedia.org/wiki/Charge_conservation
same_as:
  wikidata: Q304054
  wikipedia: Charge conservation
---

## Statement

Let $\rho \colon \R^3 \times \R \to \R$ be a charge density and $J \colon \R^3 \times \R \to \R^3$ a current density.
Let $E$ and $B$ be $C^2$ fields that solve [[Maxwell's equations|9BWWD4QK8Y]] with these sources.
Then $\rho$ and $J$ satisfy the continuity equation
$$\frac{\partial \rho}{\partial t} + \nabla \cdot J = 0.$$
Consequently, for every bounded region $V$ with smooth boundary and outward unit normal $n$, fixed in time,
$$\frac{d}{dt} \int_V \rho \, dV = - \int_{\partial V} J \cdot n \, dA.$$

## Remarks

Take the [[divergence|0MWV6ZTK6S]] of the Ampère–Maxwell law $\nabla \times B = \mu_0 J + \mu_0 \varepsilon_0 \partial_t E$.
The left side vanishes because the [[divergence of a curl is zero|0F56CMMC5P]], and Gauss's law $\nabla \cdot E = \rho / \varepsilon_0$ turns the right side into $\mu_0 (\nabla \cdot J + \partial_t \rho)$.
The integral form follows from the [[divergence theorem|0JX86PSSA9]].
The $C^2$ hypothesis lets the divergence pass through the time derivative and the mixed partial derivatives commute.

Physically, conservation of [[electric charge|6XPSV47R56]] is an experimental law that holds independently of Maxwell's theory.
The proposition shows that Maxwell's equations are consistent only with sources that conserve charge.
Without the displacement term $\mu_0 \varepsilon_0 \partial_t E$, the same computation would force $\nabla \cdot J = 0$, which fails for a charging capacitor.

Example: a charge $q$ moving with constant velocity $v$ has $\rho = q \, \delta(x - vt)$ and $J = q v \, \delta(x - vt)$, and indeed $\partial_t \rho = -v \cdot \nabla \rho = -\nabla \cdot J$ in the sense of distributions.

## Explanations

### L1 human

Electric charge is never created or destroyed.
If the charge inside a box goes up, exactly that much charge has flowed in through the walls of the box.
This rule is built into Maxwell's equations: they could not be solved for sources that broke it.

### L2 human

The continuity equation is the local form of conservation, and it has the same shape as conservation of mass in fluid mechanics.
In the covariant formulation it reads $\partial_\mu J^\mu = 0$ for the four-current $J^\mu = (c\rho, J)$, and it follows from the antisymmetry of the electromagnetic tensor.
By Noether's theorem the conservation of charge also corresponds to the gauge symmetry of electromagnetism.
