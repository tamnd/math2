---
tag: GT80CMMQRR
kind: definition
name: Rossby wave
msc: [76U60, 86A10]
defines: 6N1MQMA9TM
uses: [E66111XRRA, B3SXT9TWFA, CZ1S1P465Y]
sources:
  - url: https://en.wikipedia.org/wiki/Rossby_wave
---

## Definition

Consider a two-dimensional incompressible flow on a $\beta$-plane, where the Coriolis parameter is $f = f_0 + \beta y$ with constants $f_0$ and $\beta > 0$.
Let $\psi(x, y, t)$ be its [[stream function|E66111XRRA]], so that the velocity is $(u, v) = (-\partial_y \psi, \partial_x \psi)$ and the relative [[vorticity|B3SXT9TWFA]] is $\zeta = \Delta \psi$.
The linearised barotropic vorticity equation about a state of rest is
$$\frac{\partial}{\partial t} \Delta \psi + \beta \, \frac{\partial \psi}{\partial x} = 0.$$
A *Rossby wave* is a plane-wave solution $\psi = A \cos(k x + l y - \omega t)$ of this equation with $A \ne 0$ and $(k, l) \ne (0, 0)$.
Such a function is a solution exactly when
$$\omega = -\frac{\beta k}{k^2 + l^2}.$$

## Remarks

Indeed $\Delta \psi = -(k^2 + l^2) \psi$, so the equation becomes $\big( -\omega (k^2 + l^2) - \beta k \big) A \sin(k x + l y - \omega t) = 0$.
The zonal phase speed $\omega / k = -\beta / (k^2 + l^2)$ is negative, so the crests move westward.
On a sphere of radius $a$ at latitude $\varphi_0$, $\beta = 2 \abs{\Omega} \cos \varphi_0 / a$.
In a uniform eastward flow $U$ the relation becomes $\omega = U k - \beta k / (k^2 + l^2)$, and the waves are stationary when $U = \beta / (k^2 + l^2)$.

Example: with $\beta = 1.6 \times 10^{-11}$ m$^{-1}$s$^{-1}$ and a wavelength of $6000$ km in $x$ with $l = 0$, $k \approx 1.05 \times 10^{-6}$ m$^{-1}$, and the phase speed is about $-15$ m/s.

Non-example: on an $f$-plane, where $\beta = 0$, the relation gives $\omega = 0$; there is no propagating Rossby wave.
