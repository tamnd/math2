---
tag: Z94NBKVCRY
kind: problem
name: Riemann problem for gas dynamics
msc: [76N15, 35L65, 76L05]
uses: [GJWKX22VVE, RW0JK9VDZE, FRVV0NHBXT, MFN4Q5SH8H, 1A01A3EJRX]
about: [RW0JK9VDZE, FRVV0NHBXT]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_problem
history:
  posed_by: "Bernhard Riemann"
  first_stated: "1860"
---

## Problem

Let $\gamma > 1$ be the adiabatic exponent of a polytropic gas.
Consider the one-dimensional [[Euler equations|RW0JK9VDZE]]
$$\rho_t + (\rho u)_x = 0, \qquad (\rho u)_t + (\rho u^2 + p)_x = 0, \qquad E_t + \big( u (E + p) \big)_x = 0,$$
where $\rho$ is the density, $u$ the velocity, $p$ the pressure and $E = \dfrac{p}{\gamma - 1} + \dfrac12 \rho u^2$ the total energy per unit volume.
Let $(\rho_l, u_l, p_l)$ and $(\rho_r, u_r, p_r)$ be two constant states with $\rho_l, p_l, \rho_r, p_r > 0$.
Find an [[entropy solution|1A01A3EJRX]] for $t > 0$ with the initial values $(\rho_l, u_l, p_l)$ for $x < 0$ and $(\rho_r, u_r, p_r)$ for $x > 0$.

## Remarks

This is the [[Riemann problem|GJWKX22VVE]] for the Euler equations; Riemann studied it in 1860 for an isentropic gas.
It is solved.
The solution is self-similar, a function of $x/t$, and consists of three waves separated by constant states.
The left wave is a [[shock|FRVV0NHBXT]] or a [[rarefaction wave|MFN4Q5SH8H]], the middle wave is a contact discontinuity, and the right wave is a shock or a rarefaction wave.
Across the contact discontinuity the pressure $p_*$ and the velocity $u_*$ are continuous, and only the density jumps.
The value $p_*$ is the root of one scalar equation $\phi_l(p_*) + \phi_r(p_*) + u_r - u_l = 0$, where $\phi_l$ and $\phi_r$ are explicit increasing functions built from the shock and rarefaction curves.
If $u_r - u_l \ge \dfrac{2(c_l + c_r)}{\gamma - 1}$, where $c_l$ and $c_r$ are the sound speeds of the two states, there is no root, and a vacuum forms between two rarefaction waves.
In the class of such wave patterns the solution exists and is unique for all data.
Exact and approximate Riemann solvers are the core of Godunov-type numerical methods for compressible flow.

## Explanations

### L1 human

A tube holds gas in two different states on the two sides of a thin wall, and the wall is removed at time zero.
Typically a shock runs into the low-pressure side, a rarefaction fan runs into the high-pressure side, and between them the interface of the two gases moves with the flow.
All three can be computed exactly, up to solving one equation in one unknown.
If the two gases rush apart fast enough, a region of empty space opens between them.
