---
tag: 2N1KQKT34G
kind: definition
name: Stokes drift
msc: [76B15]
defines: SXX1PJVS5V
uses: [5E6K4ATM9W, ZWF8B7T5NX]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes_drift
---

## Definition

Let $u(x, t)$ be a velocity field on a region of $\R^n$ that is periodic in $t$ with period $T > 0$.
Write $\overline{f} = \frac{1}{T}\int_0^T f(t)\,dt$ for the time average over one period.
For a point $x_0$, let $X(t)$ be the path of the fluid particle with $X(0) = x_0$, that is $X'(t) = u(X(t), t)$, a [[pathline|ZWF8B7T5NX]] of the flow.
The *Eulerian mean velocity* at $x_0$ is $\overline{u_E} = \overline{u(x_0, \cdot)}$.
The *Lagrangian mean velocity* is $\overline{u_L} = \overline{u(X(\cdot), \cdot)}$, the mean velocity of the particle in the [[Lagrangian description|5E6K4ATM9W]].
The *Stokes drift velocity* at $x_0$ is
$$u_S = \overline{u_L} - \overline{u_E}.$$

## Remarks

For a small oscillation, expand $u(X(t), t) \approx u(x_0, t) + (\xi(t) \cdot \nabla) u(x_0, t)$ with $\xi(t) = \int_0^t u(x_0, s)\,ds$; this gives the standard approximation $u_S \approx \overline{(\xi \cdot \nabla) u}$.
Example: take the linear deep-water wave with surface $\eta = a\cos(kx - \omega t)$ and $\omega^2 = gk$.
Its Eulerian mean velocity below the troughs is zero, while the approximation gives the horizontal drift $u_S = \omega k a^2 e^{2kz}$ at depth $z < 0$.
So the drift is of second order in the amplitude and decays twice as fast with depth as the wave motion.
A spatially uniform oscillation $u(x, t) = U_0\cos(\omega t)\,e_1$ has zero Stokes drift, since the particle sees the same velocity as the fixed point; drift needs a velocity that varies in space.
Non-example: the field $u(x, t) = (t, 0, \dots, 0)$ is not periodic in $t$, so the averages above, and the Stokes drift, are not defined for it.
