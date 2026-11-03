---
tag: 49CZM6QZD1
kind: example
name: Dedekind ellipsoid
msc: [85A15, 76U05]
illustrates: [4FC5XQA2RK]
uses: [4FC5XQA2RK, WBSY27NTD1]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_ellipsoid
---

## Example

Consider a homogeneous, incompressible fluid of density $\rho$ that attracts itself by Newtonian gravity.
A *Dedekind ellipsoid* is a triaxial ellipsoid $x^2/a^2 + y^2/b^2 + z^2/c^2 \le 1$, with $a > b$, that is a steady equilibrium of this fluid of the following kind.
The boundary does not move at all in an inertial frame.
The fluid inside moves with a velocity field of uniform vorticity about the $z$-axis, tangent to the boundary.
Check: the velocity field $v = \lambda \left( -\frac{a}{b} y, \frac{b}{a} x, 0 \right)$, for a constant $\lambda$, has zero divergence and is tangent to every ellipse $x^2/a^2 + y^2/b^2 = \text{const}$, so the boundary stays fixed.
Its vorticity is $\left(0, 0, \lambda \left( \frac{b}{a} + \frac{a}{b} \right) \right)$, which is uniform.
Let $P$ be the pressure and $\Phi$ the gravitational potential, which is quadratic inside the ellipsoid.
Since $(v \cdot \nabla) v = -\lambda^2 (x, y, 0)$, the steady Euler equations reduce to $P + \rho \Phi - \frac{1}{2} \rho \lambda^2 (x^2 + y^2) = \text{const}$.
Requiring $P = 0$ on the boundary gives conditions on $a$, $b$, $c$ and $\lambda$.
These conditions are met exactly by the ellipsoids with the same axes as the [[Jacobi ellipsoids|WBSY27NTD1]].
This is an instance of Dedekind's theorem, which exchanges the roles of the rotation of the figure and of the internal vorticity.

## Remarks

The Jacobi ellipsoid rotates rigidly without internal motion, while the Dedekind ellipsoid has the same shape at rest with internal circulation.
Both are special cases of the [[Riemann ellipsoids|597TZ97P97]], in which the figure rotates and the fluid also circulates inside it.
They are named after Richard Dedekind, who found them in 1860.

## Explanations

### L1 human

A Jacobi ellipsoid is a lopsided blob of liquid that spins as a whole.
A Dedekind ellipsoid has the very same shape but does not turn at all; instead, the liquid inside flows around in loops along the surface.
Gravity holds the shape in place, and the flow inside provides the outward push that spinning gave in the Jacobi case.
