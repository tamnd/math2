---
tag: S9R68QM2NG
kind: definition
name: Primitive equations
msc: [86A10, 86A05, 35Q86]
defines: QANHETP404
uses: [18KXZHVF4M, TXQQQG9T2S, 2MNWD70JN3, NM5Q4845Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_equations
---

## Definition

Consider a thin layer of fluid on a rotating planet, in local coordinates $x$, $y$ (horizontal) and $z$ (up).
Let $f$ be the Coriolis parameter and $g$ the gravitational acceleration.
The unknowns are the horizontal velocity $u_h = (u, v)$, the vertical velocity $w$, the pressure $p$, the density $\rho$ and a thermodynamic variable $T$.
The *primitive equations* are the equations of [[geophysical fluid dynamics|2MNWD70JN3]] with the vertical momentum equation replaced by hydrostatic balance.
In the [[Boussinesq|TXQQQG9T2S]] form, with reference density $\rho_0$, the horizontal momentum equation is
$$\frac{\partial u_h}{\partial t} + (u_h \cdot \nabla_h) u_h + w \frac{\partial u_h}{\partial z} + f e_z \times u_h = -\frac{1}{\rho_0} \nabla_h p + \mathcal{F}.$$
The hydrostatic balance and the conservation of mass are
$$\frac{\partial p}{\partial z} = -\rho g, \qquad \nabla_h \cdot u_h + \frac{\partial w}{\partial z} = 0.$$
The thermodynamic equation is
$$\frac{\partial T}{\partial t} + u_h \cdot \nabla_h T + w \frac{\partial T}{\partial z} = Q.$$
An equation of state $\rho = \rho(T)$ closes the system.
In the ocean $\rho$ depends also on salinity, which obeys an equation like that of $T$.
Here $\nabla_h = (\partial_x, \partial_y)$, $e_z$ is the upward unit vector, and $\mathcal{F}$ and $Q$ are the friction and heating terms.
A typical friction term is $\mathcal{F} = \nu_h \Delta_h u_h + \nu_v \partial_z^2 u_h$ with [[viscosities|NM5Q4845Z4]] $\nu_h, \nu_v \ge 0$.

## Remarks

The vertical velocity is not a prognostic variable: it is found from the continuity equation by integration in $z$.
The pressure is found from the hydrostatic equation up to its surface value.
For the atmosphere one usually writes a compressible version in pressure coordinates, with an ideal gas law and the potential temperature as thermodynamic variable.

Example: a state of rest, $u_h = 0$ and $w = 0$, with $T = T(z)$, $\rho = \rho(T(z))$ and $p(z) = p_0 - g \int_0^z \rho \, dz'$, solves the equations with $\mathcal{F} = 0$ and $Q = 0$.

Non-example: the full Boussinesq equations are not the primitive equations.
They keep the vertical momentum equation $\partial_t w + u \cdot \nabla w = -\rho_0^{-1} \partial_z p - g \rho / \rho_0 + \dots$ with its vertical acceleration.
So they also describe non-hydrostatic motions such as convection plumes.

With full viscosity and diffusivity, the three-dimensional primitive equations are globally well-posed for initial data in $H^1$, a result of Cao and Titi (2007).
