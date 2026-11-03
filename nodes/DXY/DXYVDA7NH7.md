---
tag: DXYVDA7NH7
kind: definition
name: Plate theory
msc: [74K20, 74B05]
defines: 782XMC21FH
uses: [6W00ZECYT0, T8ENJX1905, NWYZ9QBA84]
sources:
  - url: https://en.wikipedia.org/wiki/Plate_theory
---

## Definition

Let $\Omega \subset \R^2$ be a bounded domain and $h > 0$ a thickness much smaller than the diameter of $\Omega$.
A *plate* is a body occupying $\Omega \times (-h/2, h/2)$, made of a [[linear elastic|6W00ZECYT0]] material, with mid-plane $\Omega \times \set{0}$.
A *plate theory* is a model of the plate in which:

1. The unknowns are fields on $\Omega$, such as the in-plane displacements $u_1, u_2$ and the deflection $w$ of the mid-plane.
   They may include the rotations of the normals.
2. The displacement of each point $(x, z)$ of the body, with $x \in \Omega$ and $\abs{z} < h/2$, is an assumed function of $z$ whose coefficients are these fields.
3. Integrating the stresses through the thickness gives stress resultants on $\Omega$: membrane forces $N_{\alpha\beta}$, bending moments $M_{\alpha\beta}$ and transverse shear forces $Q_\alpha$.
4. These resultants satisfy two-dimensional equilibrium equations, with a constitutive law derived from the three-dimensional one and from the assumption of clause 2.

## Remarks

Example: Kirchhoff–Love theory assumes $u_\alpha(x, z) = u^0_\alpha(x) - z \, \partial_\alpha w(x)$ and $u_3(x, z) = w(x)$.
For an isotropic plate with [[Young's modulus|T8ENJX1905]] $E$ and [[Poisson's ratio|NWYZ9QBA84]] $\nu$ this leads to the bending stiffness $D = Eh^3/(12(1 - \nu^2))$ and to $D \Delta^2 w = q$ for a transverse load $q$.

Non-example: a model for a thin body with a curved mid-surface, such as a dome, is a shell theory.
It is not a plate theory, since clause 2 refers to a flat mid-plane.

In linear theories the in-plane and bending problems decouple for a plate symmetric about its mid-plane.
Nonlinear theories, such as the Föppl–von Kármán equations, couple them.
