---
tag: E8FQ2R87VX
kind: definition
name: Immersed boundary method
msc: [65M85, 76D05, 76M20]
defines: 720QQR553X
uses: [18KXZHVF4M, 0KPHENZ5S7, X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Immersed_boundary_method
---

## Definition

Let $\Omega \subset \R^d$ be a fluid domain with density $\rho > 0$ and viscosity $\mu > 0$.
Let a structure be a curve or surface $X(s, t) \in \Omega$, with parameter $s$ in a set $S$.
Let $F(s, t)$ be the elastic force density of the structure, a given function of the configuration $X(\cdot, t)$.
The *immersed boundary formulation* couples the incompressible [[Navier–Stokes equations|18KXZHVF4M]]
$$\rho (u_t + u \cdot \nabla u) = -\nabla p + \mu \Delta u + f, \qquad \nabla \cdot u = 0,$$
with two interaction equations, written with the [[Dirac delta function|0KPHENZ5S7]] $\delta$:
$$f(x, t) = \int_S F(s, t) \, \delta(x - X(s, t)) \, ds, \qquad \frac{\partial X}{\partial t}(s, t) = \int_\Omega u(x, t) \, \delta(x - X(s, t)) \, dx.$$
The *immersed boundary method* discretizes it in three parts:

1. the fluid equations on a fixed Cartesian grid of width $h$, by [[finite differences|X7HYEBA5SA]] or another grid method;
2. the structure by a finite set of points $X_k$;
3. $\delta$ by a smooth discrete delta function $\delta_h$, supported on a few grid cells.

## Remarks

The second interaction equation says that the structure moves with the local fluid velocity, which is the no-slip condition.
The same $\delta_h$ spreads forces and interpolates velocities, so spreading is the adjoint of interpolation.
Hence the power given by the structure equals the power received by the fluid.
A standard $\delta_h$ in $d$ dimensions is a product $\prod_{i=1}^{d} h^{-1} \phi(x_i / h)$ of one-dimensional kernels $\phi$ supported in $[-2, 2]$.

Example: a closed elastic membrane $X(s, t)$, $s \in [0, 2\pi)$, in a fluid at rest, with tension force $F = \kappa \, \partial_s^2 X$ and $\kappa > 0$.
If the initial membrane is an ellipse, the forces drive the fluid, and the membrane relaxes towards a circle of the same enclosed area.

Non-example: a method that meshes the fluid region outside the structure with a body-fitted mesh that moves with the structure fails clause 1.
Its grid is not fixed, so it is not an immersed boundary method.
