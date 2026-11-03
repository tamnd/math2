---
tag: 5E290FZRJG
kind: definition
name: Barotropic vorticity equation
msc: [76U60, 35Q86, 86A10]
defines: W4V4FXSR5R
uses: [F2D7MXW8V1, B3SXT9TWFA, E66111XRRA, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Barotropic_vorticity_equation
---

## Definition

Work on a [[beta plane|F2D7MXW8V1]] with coordinates $x$ (east), $y$ (north) and Coriolis parameter $f = f_0 + \beta y$.
Let $\psi(x, y, t)$ be a [[stream function|E66111XRRA]], with velocity $(u, v) = (-\partial_y \psi, \partial_x \psi)$ and relative [[vorticity|B3SXT9TWFA]] $\zeta = \nabla^2 \psi$, where $\nabla^2 = \partial_x^2 + \partial_y^2$ is the [[Laplacian|0E0B6RA8K0]].
For functions $a, b$ let $J(a, b) = \partial_x a \, \partial_y b - \partial_y a \, \partial_x b$.
The *barotropic vorticity equation* is
$$\frac{\partial \zeta}{\partial t} + J(\psi, \zeta + f) = 0, \qquad \text{that is} \qquad \frac{\partial}{\partial t} \nabla^2 \psi + J(\psi, \nabla^2 \psi) + \beta \frac{\partial \psi}{\partial x} = 0.$$

## Remarks

Since $J(\psi, q) = u \, \partial_x q + v \, \partial_y q$, the equation says $D(\zeta + f)/Dt = 0$, where $D/Dt$ is the derivative along the flow: absolute vorticity is conserved by each fluid column.
On the sphere the same form holds with $f = 2 \Omega \sin \varphi$ and the spherical Laplacian and Jacobian.

Example: $\psi = A \cos(kx + ly - \omega t)$ with $K^2 = k^2 + l^2 > 0$ solves the equation exactly when $\omega = -\beta k / K^2$.
Indeed $\nabla^2 \psi = -K^2 \psi$, so $J(\psi, \nabla^2 \psi) = 0$, and the remaining terms give $(-K^2 \omega - \beta k) A \sin(kx + ly - \omega t) = 0$.
This is the dispersion relation of [[Rossby waves|6N1MQMA9TM]]; their phase moves westward.

Non-example: a flow with nonzero horizontal divergence $\partial_x u + \partial_y v \ne 0$, such as a flow with stretching of vortex columns, is not described by the equation, which assumes a stream function.

The integrals of the energy $\frac12 \int \abs{\nabla \psi}^2$ and of the enstrophy $\frac12 \int \zeta^2$ over a doubly periodic domain are conserved.
