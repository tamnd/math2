---
tag: MSRAD0X7H4
kind: concept
name: Willmore flow
msc: ["53E40", "53A05"]
sources:
  - url: https://en.wikipedia.org/wiki/Willmore_energy
---

## Summary

The Willmore flow is the gradient flow of the [[Willmore energy|R7WFJGJBV4]] for closed surfaces immersed in $\R^3$.
Each point of the surface moves along the normal with a speed given by a fourth-order expression in the surface.
In this way the energy decreases as fast as possible.
Its stationary surfaces are the Willmore surfaces, such as round spheres.
It is a tool for finding surfaces that minimize bending energy.

## Explanations

### L1 human

The Willmore energy measures how much a closed surface bends, by integrating the square of its [[mean curvature|PA78NFEPCF]].
A round sphere has the least energy, $4\pi$, among all closed surfaces.
The Willmore flow deforms a surface step by step so that this energy drops.
A bumpy sphere tends to smooth out toward a round shape, while a round sphere does not move at all.
Unlike mean curvature flow, the flow does not simply shrink surfaces, because the energy does not change under scaling.
