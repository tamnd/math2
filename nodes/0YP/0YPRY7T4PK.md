---
tag: 0YPRY7T4PK
kind: definition
name: Flux through a surface
msc: [26B15]
defines: 026J1MG2NW
uses: [0EKZW08FQ5, 0DQ8ERJZNS, 0BJDQ2HBH1, 05788J51WZ, 0N67NBKQ5T]
sources:
  - url: https://en.wikipedia.org/wiki/Flux
    locator: General mathematical definition (surface integral)
  - url: https://en.wikipedia.org/wiki/Surface_integral
    locator: Surface integrals of vector fields
  - url: https://en.wikipedia.org/wiki/Surface_integral
    locator: Dependence on parametrization
---

## Definition

Let $S \subseteq \mathbb{R}^3$ be an [[oriented surface|0EKZW08FQ5]] with unit normal field $n$, and let $F$ be a continuous [[vector field|0N67NBKQ5T]] on $S$.
The flux of $F$ through $S$ is the [[surface integral|0DQ8ERJZNS]]
$$\iint_S F \cdot n \, dS.$$

## Remarks

If $r \colon D \to \mathbb{R}^3$ is a regular [[parametrisation|05788J51WZ]] of $S$ with $r_u \times r_v$ pointing in the direction of $n$, then the flux is $\iint_D F\big( r(u, v) \big) \cdot \big( r_u \times r_v \big) \, du \, dv$.
Reversing the orientation of $S$ changes the sign of the flux. The notation $\iint_S F \cdot d\mathbf{S}$, with $d\mathbf{S} = n \, dS$, is common.
Example: for $F(x, y, z) = (x, y, z)$ and the unit sphere with the outward normal $n(p) = p$, we get $F \cdot n = 1$, so the flux is the area $4\pi$.
If $F$ is the velocity field of a fluid, the flux is the volume of fluid that crosses $S$ per unit time. Flow in the direction of $n$ counts as positive.

## Explanations

### L1 human

Flux measures how much of a field goes through a surface.
Only the part of the field perpendicular to the surface counts. Flow along the surface does not cross it.
