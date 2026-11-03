---
tag: EBZFZ6W6K0
kind: definition
name: Richards equation
msc: [76S05, 86A05]
defines: 5GA1QB5VFM
uses: [DX8RV2XG6H, FD4NR553YR]
sources:
  - url: https://en.wikipedia.org/wiki/Richards_equation
---

## Definition

Consider water in a rigid porous medium partly filled with air, with the coordinate $z$ pointing upward.
Let $h(x, t)$ be the pressure head of the water, which is negative where the medium is unsaturated.
Let $\theta(h)$ be the volumetric water content and $K(h) > 0$ the hydraulic conductivity.
The functions $\theta$ and $K$ are given, and they describe the medium.
The *Richards equation* is
$$\frac{\partial \theta(h)}{\partial t} = \nabla \cdot \big( K(h) \, (\nabla h + e_z) \big),$$
where $e_z$ is the upward unit vector.
In one vertical dimension it reads $\partial_t \theta = \partial_z \big( K(h) (\partial_z h + 1) \big)$.

## Remarks

It is the [[continuity equation|FD4NR553YR]] $\partial_t \theta + \nabla \cdot q = 0$ for the water, with the flux given by the Darcy–Buckingham law $q = -K(h) \nabla (h + z)$.
This law is [[Darcy's law|DX8RV2XG6H]] with a conductivity that depends on the water content.

Example: if $K$ is constant and $\theta(h) = C h$ with a constant $C > 0$, the equation is the linear heat equation $C \partial_t h = K \Delta h$, since $\nabla \cdot e_z = 0$.
Real soils have $K$ that decreases by orders of magnitude as the soil dries, so the equation is strongly nonlinear.

Non-example: the equation $\partial_t \theta = \nabla \cdot (K(h) \nabla h)$ without the term $e_z$ is not the Richards equation; it omits gravity and describes horizontal flow only.

Other common forms use $\theta$ as the unknown, with the soil-water diffusivity $D(\theta) = K \, dh / d\theta$.
That form fails where the medium is saturated, since $d\theta / dh = 0$ there.
