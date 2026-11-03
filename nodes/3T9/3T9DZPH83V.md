---
tag: 3T9DZPH83V
kind: definition
name: Acoustic wave equation
msc: [76Q05, 35L05]
defines: 85WZYYHZYS
uses: [5EHD2XBQDG, SN4J6KP03C, FJC2GMVARF, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Acoustic_wave_equation
---

## Definition

Consider an inviscid [[compressible fluid|FJC2GMVARF]] in a uniform state of rest with density $\rho_0$ and pressure $p_0$.
Let $c_0 > 0$ be its [[speed of sound|SN4J6KP03C]], given by $c_0^2 = (\partial p / \partial \rho)_s$, the derivative at constant entropy $s$ at the state $(\rho_0, p_0)$.
Write the pressure as $p_0 + p'(x, t)$ for $x \in \R^3$ and time $t$, where $p'$ is the acoustic pressure.
The *acoustic wave equation* is
$$\frac{\partial^2 p'}{\partial t^2} = c_0^2 \, \Delta p',$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in $x$.

## Remarks

It is obtained from the mass and momentum equations of an inviscid fluid and an isentropic equation of state.
One keeps only the terms that are linear in the perturbations $p'$, $\rho' = \rho - \rho_0$ and the velocity $u$.
The density perturbation $\rho' = p' / c_0^2$ and the velocity potential $\phi$, with $u = \nabla \phi$ and $p' = -\rho_0 \, \partial \phi / \partial t$, satisfy the same equation.

Example: the plane wave $p'(x, t) = A \cos(k \cdot x - \omega t)$ with $k \in \R^3$ is a solution exactly when $\omega^2 = c_0^2 \abs{k}^2$.
Indeed $\partial_t^2 p' = -\omega^2 p'$ and $\Delta p' = -\abs{k}^2 p'$.

Non-example: $p'(x, t) = \cos(x_1) e^{-t}$ is not a solution, since $\partial_t^2 p' = p'$ while $c_0^2 \Delta p' = -c_0^2 p'$.

In one space dimension every solution has the form $p'(x, t) = F(x - c_0 t) + G(x + c_0 t)$, two waves that move in opposite directions at speed $c_0$.
