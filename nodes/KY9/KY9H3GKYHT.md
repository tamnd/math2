---
tag: KY9H3GKYHT
kind: definition
name: Seismic moment
msc: [86A15, 74R10]
defines: 88YRH7XQDX
uses: [J2GWW1NPTC]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_moment
---

## Definition

Let an earthquake be a shear slip on a fault surface $\Sigma$ of area $A$ in a medium with [[shear modulus|J2GWW1NPTC]] $\mu$.
Let $D$ be the average over $\Sigma$ of the final slip, the jump of the tangential displacement across $\Sigma$.
The *seismic moment* of the earthquake is
$$M_0 = \mu A D.$$
If $\mu$ varies on $\Sigma$, then $M_0 = \int_\Sigma \mu\, \abs{\Delta u}\, dA$, where $\Delta u$ is the slip, provided the slip has a constant direction.

## Remarks

The unit is the newton metre, the unit of torque; $M_0$ is the moment of each of the two force couples equivalent to the slip.
Example: $\mu = 3 \times 10^{10}$ Pa, a fault of $10$ km by $10$ km, so $A = 10^8$ m², and $D = 1$ m give $M_0 = 3 \times 10^{10} \cdot 10^8 \cdot 1 = 3 \times 10^{18}$ N·m.
Non-example: an underground explosion pushes the rock outward with no slip on any fault, so it has no $\mu A D$ of this form.
It is described by an isotropic moment tensor instead.
For a shear source the seismic moment equals $\sqrt{\tfrac12 \sum_{i,j} M_{ij}^2}$, where $M_{ij}$ is the moment tensor.
In practice $M_0$ is estimated from the amplitude of long-period seismic waves, which is proportional to it.
