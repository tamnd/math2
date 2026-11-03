---
tag: WBSY27NTD1
kind: example
name: Jacobi ellipsoid
msc: [85A15, 76U05]
illustrates: [4FC5XQA2RK]
uses: [4FC5XQA2RK, JVFQZ155S9]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_ellipsoid
same_as:
  wikidata: Q33728375
  wikipedia: Jacobi ellipsoid
---

## Example

Consider a homogeneous, incompressible fluid of density $\rho$ that attracts itself by Newtonian gravity and rotates rigidly with angular velocity $\Omega$ about the $z$-axis.
A *Jacobi ellipsoid* is a triaxial ellipsoid $x^2/a^2 + y^2/b^2 + z^2/c^2 \le 1$, with $a > b > c > 0$, that is a figure of equilibrium of this fluid.
This means that in the rotating frame the fluid is in [[hydrostatic equilibrium|4FC5XQA2RK]] and the pressure vanishes on the boundary.
Write $\Delta(u) = \sqrt{(a^2 + u)(b^2 + u)(c^2 + u)}$ and let $G$ be the gravitational constant.
Equilibrium holds exactly when the axes satisfy
$$a^2 b^2 \int_0^\infty \frac{du}{(a^2 + u)(b^2 + u) \Delta(u)} = c^2 \int_0^\infty \frac{du}{(c^2 + u) \Delta(u)},$$
and then the angular velocity is given by
$$\frac{\Omega^2}{\pi G \rho} = 2 a b c \int_0^\infty \frac{u \, du}{(a^2 + u)(b^2 + u) \Delta(u)}.$$
Check: the gravitational potential inside a homogeneous ellipsoid is a quadratic form in $x, y, z$ plus a constant, and so is the centrifugal potential $-\frac{1}{2} \Omega^2 (x^2 + y^2)$.
The total potential is constant on the boundary exactly when its three coefficients are proportional to $1/a^2$, $1/b^2$, $1/c^2$.
These are two conditions, and they give the two displayed equations.
For each ratio $b/a$ in a certain range, the first equation fixes $c$, so the Jacobi ellipsoids form a one-parameter family up to scale.

## Remarks

As $b \to a$ the Jacobi ellipsoids tend to one of the axisymmetric [[Maclaurin spheroids|JVFQZ155S9]].
The Jacobi family meets the Maclaurin family at eccentricity $e \approx 0.8127$, where $\Omega^2 / (\pi G \rho) \approx 0.3742$; beyond this point, at equal angular momentum, the Jacobi ellipsoid has lower energy than the Maclaurin spheroid.
They were found by Carl Gustav Jacob Jacobi in 1834, contrary to the expectation that a rotating fluid figure must be symmetric about its axis.

## Explanations

### L1 human

A spinning ball of liquid held by its own gravity flattens into a squashed sphere.
Jacobi found that, if it spins fast enough, it can also take the shape of an elongated ellipsoid with three different axes, spinning about its shortest axis.
At high spin this lopsided shape is the more stable one.
This was a surprise, because one expects a spinning body to stay round around its axis.
