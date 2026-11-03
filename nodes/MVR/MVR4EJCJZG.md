---
tag: MVR4EJCJZG
kind: definition
name: Johnson–Kendall–Roberts model of adhesive contact
msc: [74M15, 74A50]
defines: 98BMFJ17D9
uses: [XNCND3KYNP, T0R3FBPTJ2]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_mechanics
---

## Definition

Consider two elastic spheres with effective radius $R$ and effective modulus $E^*$ as in [[Hertz's theory|XNCND3KYNP]].
Let $w > 0$ be the work of adhesion of their surfaces, the energy per unit area needed to separate them.
The *Johnson–Kendall–Roberts model* assumes linear elasticity and a circular contact region of radius $a$.
It also assumes that the contact edge is in equilibrium for the total energy.
This total is the elastic energy plus the potential of the load plus the surface energy $-\pi a^2 w$.
Under these assumptions the applied force $F$, positive in compression, and $a$ satisfy
$$a^3 = \frac{3R}{4E^*} \left( F + 3 \pi w R + \sqrt{6 \pi w R F + (3 \pi w R)^2} \right).$$

## Remarks

Example: at zero load $F = 0$ the formula gives a positive contact radius, $a^3 = 9 \pi w R^2 / (2E^*)$.
Under tension the square root stays real while $F \ge -\tfrac{3}{2} \pi w R$, and the surfaces separate at the pull-off force of magnitude $\tfrac{3}{2} \pi w R$, which does not depend on $E^*$.

Non-example: for $w = 0$ the formula reduces to the Hertz relation $a^3 = 3FR/(4E^*)$, which has no adhesion and no pull-off force.

The model fits large, soft bodies with strong adhesion.
For small, stiff bodies with long-range attraction, the Derjaguin–Muller–Toporov model is used instead.
