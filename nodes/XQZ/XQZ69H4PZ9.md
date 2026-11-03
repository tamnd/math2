---
tag: XQZ69H4PZ9
kind: definition
name: Quasi-geostrophic equations
msc: [76U60, 35Q86, 86A10]
defines: 8Z4QBWTWVR
uses: [CZ1S1P465Y, SCYK4FMY59, XQ82TE42FH, TXQQQG9T2S, E66111XRRA]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-geostrophic_equations
---

## Definition

Consider a stably stratified [[Boussinesq|TXQQQG9T2S]] fluid on a $\beta$-plane, with Coriolis parameter $f = f_0 + \beta y$ for constants $f_0 \ne 0$ and $\beta$.
Let $N(z) > 0$ be the [[Brunt–Väisälä frequency|XQ82TE42FH]] of the background state.
Let $\psi(x, y, z, t)$ be the geostrophic [[stream function|E66111XRRA]], with horizontal velocity $(u, v) = (-\partial_y \psi, \partial_x \psi)$.
The *quasi-geostrophic equations* are
$$\frac{\partial q}{\partial t} + J(\psi, q) = 0, \qquad q = \Delta_h \psi + \beta y + \frac{\partial}{\partial z} \left( \frac{f_0^2}{N^2} \frac{\partial \psi}{\partial z} \right),$$
where $\Delta_h = \partial_x^2 + \partial_y^2$ and $J(a, b) = \partial_x a \, \partial_y b - \partial_y a \, \partial_x b$.
The quantity $q$ is the *quasi-geostrophic potential vorticity*.
At horizontal boundaries $z = z_0$ with no vertical velocity, the buoyancy $b = f_0 \partial_z \psi$ satisfies $\partial_t b + J(\psi, b) = 0$.

## Remarks

They are derived from the Boussinesq equations by an expansion in the [[Rossby number|SCYK4FMY59]].
The expansion also assumes $\abs{\beta y} \ll \abs{f_0}$ and small deviations of the stratification from the background.
The leading order is [[geostrophic balance|CZ1S1P465Y]] with $\psi = p / (\rho_0 f_0)$.
Given $q$ and boundary data, $\psi$ is found by inverting an elliptic operator, and the velocity follows.

Example: if $\psi$ does not depend on $z$, the equations reduce to the barotropic vorticity equation $\partial_t (\Delta_h \psi) + J(\psi, \Delta_h \psi) + \beta \partial_x \psi = 0$, whose linearisation about rest has the Rossby waves as solutions.

Non-example: gravity waves and sound waves are not described by the model.
In the interior the only time derivative in the quasi-geostrophic equations is that of $q$, and these fast waves are filtered out.

The shallow water and two-layer forms are also called quasi-geostrophic equations.
They replace the stretching term by $-\psi / L_d^2$, with a deformation radius $L_d$, or by an interaction between layers.
