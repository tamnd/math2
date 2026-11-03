---
tag: WS0QZZEZD4
kind: definition
name: Normal modes of the Earth
msc: [86A15, 74H45, 74J05]
defines: NKN1ZDMTG6
uses: [JVM27J1FTF, 3F32Y21HP4, 6W00ZECYT0, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_mode
---

## Definition

Model the Earth as a ball of radius $a$, spherically symmetric, non-rotating, isotropic and [[linearly elastic|6W00ZECYT0]], in hydrostatic equilibrium under its own gravity.
Linearize the equations of motion and of self-gravitation about this state, with zero traction on the surface $r = a$.
A *normal mode of the Earth* is a non-zero solution of the form $u(x, t) = s(x) e^{i\omega t}$, with real angular frequency $\omega$.
It is a [[normal mode|JVM27J1FTF]] of this linear system.
In spherical coordinates, every mode is a combination of modes of two kinds, built from [[spherical harmonics|3F32Y21HP4]] $Y_l^m$:

1. *spheroidal* modes, $s = U(r) Y_l^m \hat r + V(r) \nabla_1 Y_l^m$;
2. *toroidal* modes, $s = W(r)\, \hat r \times \nabla_1 Y_l^m$, with no radial component.

Here $\nabla_1$ is the gradient on the unit sphere.
For each degree $l$ the radial functions solve an ordinary differential eigenvalue problem.
Its [[eigenvalues|0BQAA2BK3Q]] $\omega^2$ are numbered by the overtone number $n = 0, 1, 2, \dots$, and the modes are written ${}_nS_l$ and ${}_nT_l$.

## Remarks

The eigenfrequency of ${}_nS_l$ or ${}_nT_l$ does not depend on $m$, so it is shared by $2l + 1$ modes, $m = -l, \dots, l$.
The rotation, the ellipticity and the lateral heterogeneity of the real Earth split this degeneracy.
Example: the gravest spheroidal mode ${}_0S_2$ has a period of about $54$ minutes, and the gravest toroidal mode ${}_0T_2$ about $44$ minutes.
The radial mode ${}_0S_0$, with $l = 0$ and only $U \ne 0$, has a period of about $20.5$ minutes.
Non-example: ${}_0T_1$ is a rigid rotation of the solid Earth; it has $\omega = 0$, so it is not an oscillation and is excluded.
Toroidal modes live only in solid regions; the liquid outer core separates mantle and inner core toroidal modes.
The wave field of an earthquake is a sum of normal modes, and long-period seismograms are computed by such sums.
