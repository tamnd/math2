---
tag: ZM10T2MCY2
kind: definition
name: Laplace tidal equations
msc: [86A05, 76U60, 35Q86]
defines: 9BF0QWFZA9
uses: [NT73Y95RY5, 6HZRX3WSQD, 2E2KCFNMHE]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_of_tides
---

## Definition

Consider a thin ocean on a sphere of radius $a$ that rotates with constant angular velocity $\Omega$, with gravity $g$.
Use latitude $\varphi$ and longitude $\lambda$, and let $D(\varphi, \lambda) > 0$ be the depth of the ocean at rest.
Let $\zeta(\varphi, \lambda, t)$ be the elevation of the surface, and let $u$ and $v$ be the eastward and northward velocities averaged over depth.
Let $U(\varphi, \lambda, t)$ be the [[tide-generating potential|2E2KCFNMHE]] at the surface.
The *Laplace tidal equations* are
$$\frac{\partial \zeta}{\partial t} + \frac{1}{a\cos\varphi}\left( \frac{\partial (uD)}{\partial \lambda} + \frac{\partial (vD\cos\varphi)}{\partial \varphi} \right) = 0,$$
$$\frac{\partial u}{\partial t} - 2\Omega\sin\varphi\; v = -\frac{1}{a\cos\varphi}\, \frac{\partial (g\zeta - U)}{\partial \lambda},$$
$$\frac{\partial v}{\partial t} + 2\Omega\sin\varphi\; u = -\frac{1}{a}\, \frac{\partial (g\zeta - U)}{\partial \varphi}.$$

## Remarks

The first equation is conservation of mass, and the other two are the linearised momentum equations with the [[Coriolis force|6HZRX3WSQD]] terms $\mp 2\Omega\sin\varphi$.
They are the linear [[shallow water equations|NT73Y95RY5]] on the rotating sphere, forced by $U$.
Example: if $\Omega = 0$, $U = 0$ and $D$ is constant, the equations reduce to free gravity waves of speed $\sqrt{gD}$ on a non-rotating sphere.
Non-example: a system with the nonlinear advection terms $(u \cdot \nabla) u$ kept is not the Laplace tidal equations; those terms are dropped because tidal velocities are small.
The equations neglect the vertical acceleration of the water, which is valid because the ocean is thin compared with the tidal wavelength.
In refined versions $U$ is replaced by $(1 + k_2 - h_2) U$ and terms for ocean self-attraction and friction are added.
