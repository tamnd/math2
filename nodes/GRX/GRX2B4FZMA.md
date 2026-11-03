---
tag: GRX2B4FZMA
kind: definition
name: Vibration of plates
msc: [74K20, 74H45, 35P15]
defines: Z8F5VBZQ5M
uses: [9E6E0SCEYA, X1SGK619VJ, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Vibration_of_plates
---

## Definition

Let a thin isotropic plate have mid-plane $\Omega \subset \R^2$, thickness $h$, density $\rho$ and bending stiffness $D = Eh^3/(12(1 - \nu^2))$, with Young's modulus $E$ and Poisson's ratio $\nu$.
Let $q(x, t)$ be a transverse load.
In [[Kirchhoff–Love plate theory|9E6E0SCEYA]] the deflection $w(x, t)$ satisfies
$$D \, \Delta^2 w + \rho h \, \frac{\partial^2 w}{\partial t^2} = q,$$
with boundary conditions on $\partial\Omega$ as in the static [[biharmonic plate equation|X1SGK619VJ]].
A *free vibration mode* is a solution $w(x, t) = W(x) \cos(\omega t)$ with $q = 0$ and $W \ne 0$.
Then
$$D \, \Delta^2 W = \rho h \, \omega^2 \, W \quad \text{in } \Omega,$$
with the same boundary conditions.
The number $\omega \ge 0$ is a *natural frequency* and $W$ its *mode shape*.
The *nodal lines* of the mode are the curves in $\Omega$ where $W = 0$.

## Remarks

Example: a simply supported rectangle $0 < x < a$, $0 < y < b$ has the modes $W_{mn} = \sin(m\pi x/a) \sin(n\pi y/b)$ for integers $m, n \ge 1$.
Check: $\Delta^2 W_{mn} = \pi^4 (m^2/a^2 + n^2/b^2)^2 W_{mn}$, and $W_{mn} = \Delta W_{mn} = 0$ on the edges, so
$$\omega_{mn} = \pi^2 \left( \frac{m^2}{a^2} + \frac{n^2}{b^2} \right) \sqrt{\frac{D}{\rho h}}.$$
Its nodal lines are the segments $x = ka/m$ with $0 < k < m$ and $y = lb/n$ with $0 < l < n$.

Non-example: $W = \sin(\pi x/a)$ on the same rectangle solves $D \Delta^2 W = \rho h \omega^2 W$ for a suitable $\omega$.
It does not vanish on the edges $y = 0$ and $y = b$, so it is not a mode of the simply supported plate.

For a bounded plate with clamped or simply supported edges the natural frequencies form an increasing sequence tending to infinity.
The mode shapes are orthogonal in $L^2(\Omega)$.
This holds because $\omega^2$ are the [[eigenvalues|0BQAA2BK3Q]] of a positive self-adjoint operator with compact resolvent.
