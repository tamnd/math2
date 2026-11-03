---
tag: P1JHAF1AQY
kind: definition
name: Lubrication theory
msc: [76D08]
defines: 90FD7XNX72
uses: [18KXZHVF4M, DF0M8YNQ3D, JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Lubrication_theory
---

## Definition

Let a viscous fluid of dynamic viscosity $\mu > 0$ fill a thin gap $\set{(x, y, z) : 0 < z < h(x, y)}$ between two surfaces.
Let $H$ be a typical gap height and $L$ a typical length along the gap, with $\varepsilon = H / L \ll 1$.
Assume also that the reduced [[Reynolds number|JH9EJ0HA0R]] $\varepsilon^2 \mathrm{Re}$ is small.
The *lubrication approximation* replaces the [[Navier–Stokes equations|18KXZHVF4M]] for the velocity $(u, v, w)$ and pressure $p$ by the leading-order equations

1. $\partial_z p = 0$,
2. $\mu \, \partial_z^2 u = \partial_x p$ and $\mu \, \partial_z^2 v = \partial_y p$,
3. $\partial_x u + \partial_y v + \partial_z w = 0$,

with the [[no-slip condition|DF0M8YNQ3D]] on both surfaces.
*Lubrication theory* is the study of flows by means of these equations.

## Remarks

Example: plane Poiseuille flow $u = \frac{G}{2 \mu} z (h - z)$, $v = w = 0$, $p = -G x$ in a gap of constant height $h$ solves all three equations, since $\mu \, \partial_z^2 u = -G = \partial_x p$.

Non-example: in a cavity whose height equals its length, $\varepsilon$ is not small.
The pressure then varies across the gap, so clause 1 is not a valid approximation.

Integrating clause 2 twice in $z$ with the no-slip conditions gives $u$ and $v$ as parabolas in $z$, with coefficients depending on $\nabla p$.
Integrating clause 3 across the gap then gives the [[Reynolds equation|K2W9427PJ2]] for $p$ alone.
