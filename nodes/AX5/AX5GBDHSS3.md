---
tag: AX5GBDHSS3
kind: definition
name: Monin–Obukhov similarity theory
msc: [76F40, 86A10]
defines: EC5Y40QXRB
uses: [4R7HASDQ6Q, 4Q9PB2WPAY, 7AX1EA410X, VY307F8Z0S]
sources:
  - url: https://en.wikipedia.org/wiki/Monin%E2%80%93Obukhov_similarity_theory
---

## Definition

Consider the horizontally homogeneous, stationary surface layer of the [[planetary boundary layer|4R7HASDQ6Q]], at heights $z$ above the roughness elements.
Let $U(z)$ be the mean wind speed and $\Theta(z)$ the mean virtual potential temperature, with reference value $\theta_v$.
Primes denote [[turbulent|VY307F8Z0S]] fluctuations and overbars denote means.
Let $u_* > 0$ be the friction velocity, defined by $u_*^2 = \abs{\overline{u'w'}}$ at the surface.
Let $\overline{w'\theta_v'}_0$ be the surface kinematic flux of virtual potential temperature.
Let $\kappa \approx 0.4$ be the von Kármán constant and $g$ the gravitational acceleration.
The *Obukhov length* is
$$L = -\frac{u_*^3 \, \theta_v}{\kappa \, g \, \overline{w'\theta_v'}_0},$$
and the temperature scale is $\theta_* = -\overline{w'\theta_v'}_0 / u_*$.
*Monin–Obukhov similarity theory* is the hypothesis that there are universal functions $\phi_m$ and $\phi_h$ such that
$$\frac{\kappa z}{u_*} \frac{dU}{dz} = \phi_m\!\left( \frac{z}{L} \right), \qquad \frac{\kappa z}{\theta_*} \frac{d\Theta}{dz} = \phi_h\!\left( \frac{z}{L} \right).$$

## Remarks

The hypothesis comes from dimensional analysis.
In the surface layer the only relevant parameters are taken to be $z$, $u_*$, $\overline{w'\theta_v'}_0$ and the buoyancy parameter $g / \theta_v$.
By the [[Buckingham π theorem|4Q9PB2WPAY]] they form a single dimensionless group, which can be taken to be $z / L$.
The functions $\phi_m$ and $\phi_h$ are not given by the theory and are fitted to measurements.

The sign of $L$ gives the stability: $L < 0$ for an unstable layer (surface heating), $L > 0$ for a stable layer (surface cooling), and $\abs{L} = \infty$ in the neutral case.

Example: in neutral conditions $\phi_m(0) = 1$, and integration gives $U(z) = (u_* / \kappa) \ln(z / z_0)$ with a roughness length $z_0$, the logarithmic [[law of the wall|7AX1EA410X]].
Commonly used empirical forms are $\phi_m = 1 + 5 z / L$ for $z / L \ge 0$ and $\phi_m = (1 - 16 z / L)^{-1/4}$ for $z / L < 0$.

Non-example: the theory does not apply over strongly heterogeneous terrain, inside a plant canopy, or well above the surface layer, where other parameters such as the boundary-layer depth enter.
