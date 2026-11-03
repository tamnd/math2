---
tag: GWR4DGJR23
kind: definition
name: Föppl–von Kármán equations
msc: [74K20, 74B20, 74G60]
defines: JHEQAM6Z8M
uses: [9E6E0SCEYA, X1SGK619VJ, 7ZGSJRYBGK, SQVQ5DQT6W]
sources:
  - url: https://en.wikipedia.org/wiki/Föppl–von_Kármán_equations
---

## Definition

Let $\Omega \subset \R^2$ be the mid-plane of a thin isotropic plate of thickness $h$, with Young's modulus $E$, Poisson's ratio $\nu$ and bending stiffness $D = Eh^3/(12(1 - \nu^2))$.
Let $q$ be the transverse load per unit area, $w$ the deflection and $F$ an [[Airy stress function|7ZGSJRYBGK]] for the membrane forces, so that
$$N_{xx} = \partial_y^2 F, \qquad N_{yy} = \partial_x^2 F, \qquad N_{xy} = -\partial_x \partial_y F.$$
For functions $f, g$ on $\Omega$ put
$$[f, g] = \partial_x^2 f \, \partial_y^2 g + \partial_y^2 f \, \partial_x^2 g - 2 \, \partial_x \partial_y f \, \partial_x \partial_y g.$$
The *Föppl–von Kármán equations* are
$$D \, \Delta^2 w - [F, w] = q, \qquad \Delta^2 F = -\frac{E h}{2} [w, w].$$

## Remarks

Here $[w, w] = 2 (\partial_x^2 w \, \partial_y^2 w - (\partial_x \partial_y w)^2)$, which is twice the linearised [[Gaussian curvature|SQVQ5DQT6W]] of the deflected surface.
The first equation is vertical equilibrium, in which the membrane forces act on the curvature; the second is the compatibility of the in-plane strains.

Example: if $w = 0$, the equations reduce to $\Delta^2 F = 0$ with $q = 0$, the plane stress problem of a flat plate.
For a cylindrical bending $w = c x^2/2$ one has $[w, w] = 0$, so $F = 0$ is allowed: the plate can bend into a cylinder without stretching.

Non-example: the pair $D\Delta^2 w = q$ and $F = 0$ is the linear [[biharmonic plate equation|X1SGK619VJ]]; it fails the second equation whenever $w$ has non-zero Gaussian curvature, such as $w = c(x^2 + y^2)/2$ with $[w, w] = 2c^2$.

Sign conventions for $F$ and $[\cdot, \cdot]$ differ between texts.
