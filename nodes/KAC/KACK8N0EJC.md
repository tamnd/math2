---
tag: KACK8N0EJC
kind: definition
name: Charney–Hasegawa–Mima equation
msc: [76U60, 35Q86, 82D10]
defines: 2CPNJNDE52
uses: [F2D7MXW8V1, MT3A0DDAA8, W4V4FXSR5R, E66111XRRA, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Hasegawa%E2%80%93Mima_equation
---

## Definition

Work on a [[beta plane|F2D7MXW8V1]] with coordinates $x$ (east), $y$ (north) and Coriolis parameter $f_0 + \beta y$.
Let $L_d > 0$ be a [[Rossby radius of deformation|MT3A0DDAA8]].
Let $\psi(x, y, t)$ be a [[stream function|E66111XRRA]] with velocity $(u, v) = (-\partial_y \psi, \partial_x \psi)$, let $\nabla^2$ be the horizontal [[Laplacian|0E0B6RA8K0]] and $J(a, b) = \partial_x a \, \partial_y b - \partial_y a \, \partial_x b$.
The *Charney–Hasegawa–Mima equation* is
$$\frac{\partial}{\partial t} \left( \nabla^2 \psi - \frac{\psi}{L_d^2} \right) + J(\psi, \nabla^2 \psi) + \beta \frac{\partial \psi}{\partial x} = 0.$$

## Remarks

Equivalently, $q = \nabla^2 \psi - \psi / L_d^2 + \beta y$ satisfies $\partial_t q + J(\psi, q) = 0$, since $J(\psi, \psi) = 0$: the potential vorticity $q$ is carried by the flow.
As $L_d \to \infty$ it becomes the [[barotropic vorticity equation|W4V4FXSR5R]].
In plasma physics, after scaling, $\psi$ is the electrostatic potential and $L_d$ is the ion sound gyroradius.
The $\beta$ term then comes from the background density gradient, and the sign conventions vary between texts.

Example: $\psi = A \cos(kx + ly - \omega t)$ with $K^2 = k^2 + l^2$ solves the equation exactly when
$$\omega = -\frac{\beta k}{K^2 + L_d^{-2}}.$$
The nonlinear term vanishes because $\nabla^2 \psi = -K^2 \psi$, and the linear terms give $\left(-(K^2 + L_d^{-2}) \omega - \beta k\right) A \sin(kx + ly - \omega t) = 0$.
Compared with the barotropic case, waves longer than $L_d$ are much slower.

Non-example: the shallow water equations on a beta plane are not of this form; they also contain gravity waves, which the equation filters out.

The energy $\frac12 \int \left( \abs{\nabla \psi}^2 + \psi^2 / L_d^2 \right)$ and the enstrophy $\frac12 \int (\nabla^2 \psi - \psi / L_d^2)^2$ are conserved on a doubly periodic domain.
