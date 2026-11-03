---
tag: SP7JWN9RD5
kind: definition
name: Geostrophic balance
msc: [76U60, 86A10, 86A05]
defines: CZ1S1P465Y
uses: [2MNWD70JN3, SCYK4FMY59]
sources:
  - url: https://en.wikipedia.org/wiki/Geostrophic_wind
---

## Definition

Consider a fluid of density $\rho > 0$ in a frame rotating with a planet, with local Cartesian coordinates $x$ (east), $y$ (north) and $z$ (up).
Let $f \ne 0$ be the Coriolis parameter, $f = 2 \abs{\Omega} \sin \varphi$ at latitude $\varphi$.
Let $e_z$ be the upward unit vector and $\nabla_h = (\partial_x, \partial_y)$ the horizontal gradient.
A horizontal velocity $u_h = (u, v)$ is in *geostrophic balance* with the pressure $p$ when
$$f \, e_z \times u_h = -\frac{1}{\rho} \nabla_h p,$$
that is, when $u = -\dfrac{1}{\rho f} \dfrac{\partial p}{\partial y}$ and $v = \dfrac{1}{\rho f} \dfrac{\partial p}{\partial x}$.
Such a velocity is called the *geostrophic velocity*, or the *geostrophic wind* in the atmosphere.

## Remarks

The relation is the horizontal momentum equation of [[geophysical fluid dynamics|2MNWD70JN3]] with the acceleration and friction dropped, which is justified when the [[Rossby number|SCYK4FMY59]] and the Ekman number are small.
Since $u_h \cdot \nabla_h p = 0$, the geostrophic velocity is parallel to the isobars.

Example: with $f = 10^{-4}$ s$^{-1}$, $\rho = 1.2$ kg/m$^3$ and a pressure that increases northward by $1$ hPa per $100$ km, $\partial_y p = 10^{-3}$ Pa/m, so $u = -10^{-3} / (1.2 \cdot 10^{-4}) \approx -8.3$ m/s, a wind from east to west.

Non-example: near the equator $f \to 0$, and the balance cannot hold for a nonzero pressure gradient; geostrophy breaks down in the tropics.

When $\rho$ and $f$ are constant, the geostrophic velocity is horizontally nondivergent and has the stream function $\psi = p / (\rho f)$, with $u = -\partial_y \psi$ and $v = \partial_x \psi$.
