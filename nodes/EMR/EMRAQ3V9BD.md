---
tag: EMRAQ3V9BD
kind: definition
name: Biharmonic plate equation
msc: [74K20, 35J30, 74G05]
defines: X1SGK619VJ
uses: [9E6E0SCEYA, AS8A9F5SKE, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Kirchhoff–Love_plate_theory
---

## Definition

Let $\Omega \subset \R^2$ be the mid-plane of a thin isotropic plate of thickness $h$, with Young's modulus $E$ and Poisson's ratio $\nu$, and let $D = Eh^3/(12(1 - \nu^2))$.
Let $q$ be the transverse load per unit area and $w$ the deflection, in the same direction.
The *biharmonic plate equation* is
$$D \, \Delta^2 w = q \quad \text{in } \Omega, \qquad \Delta^2 w = \frac{\partial^4 w}{\partial x^4} + 2 \frac{\partial^4 w}{\partial x^2 \partial y^2} + \frac{\partial^4 w}{\partial y^4},$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
It is completed by two boundary conditions on each part of $\partial \Omega$.
These are $w = \partial_n w = 0$ on a clamped edge, and $w = 0$ with vanishing normal bending moment on a simply supported edge.

## Remarks

Example: a simply supported rectangle $0 < x < a$, $0 < y < b$ under the load $q = q_0 \sin(\pi x/a) \sin(\pi y/b)$ has
$$w = \frac{q_0}{D \pi^4 (1/a^2 + 1/b^2)^2} \sin\frac{\pi x}{a} \sin\frac{\pi y}{b}.$$
Check: $\Delta^2$ multiplies this product of sines by $\pi^4 (1/a^2 + 1/b^2)^2$, and $w = \Delta w = 0$ on the edges, which on a straight edge is equivalent to $w = 0$ with zero normal moment.

Non-example: the membrane equation $-T \Delta w = q$, for a stretched membrane with tension $T$, is a second-order equation and describes a body with no bending stiffness.

The equation follows from [[Kirchhoff–Love plate theory|9E6E0SCEYA]] and is a case of the [[biharmonic equation|AS8A9F5SKE]] with a right-hand side.
Expanding $q$ in double sine series gives Navier's solution for any load on a simply supported rectangle.
