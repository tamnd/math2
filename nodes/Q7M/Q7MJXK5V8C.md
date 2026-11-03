---
tag: Q7MJXK5V8C
kind: definition
name: Rayleigh–Plesset equation
msc: [76T10, 76B10]
defines: 7HAFBCXD5A
uses: [A3Q9SNF86Q, 2JZ0C15A9C, NM5Q4845Z4, Z9TBETJAP6]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Plesset_equation
---

## Definition

Consider a spherical bubble of radius $R(t) > 0$ centred at the origin in an unbounded [[incompressible|2JZ0C15A9C]] Newtonian liquid.
Let the liquid have constant density $\rho_L$, kinematic [[viscosity|NM5Q4845Z4]] $\nu_L$ and surface tension $\sigma$.
Assume the flow of the liquid is spherically symmetric.
Let $p_B(t)$ be the pressure inside the bubble, assumed uniform, and $p_\infty(t)$ the pressure of the liquid far from the bubble.
The *Rayleigh–Plesset equation* is
$$R \ddot R + \frac{3}{2} \dot R^2 + \frac{4 \nu_L \dot R}{R} + \frac{2 \sigma}{\rho_L R} = \frac{p_B(t) - p_\infty(t)}{\rho_L},$$
where dots denote derivatives in $t$.

## Remarks

Incompressibility forces the radial velocity of the liquid to be $u(r, t) = R^2 \dot R / r^2$.
The equation follows by integrating the radial momentum equation from $r = R$ to $r = \infty$.
The normal stress condition at the bubble wall then adds the [[Young–Laplace|Z9TBETJAP6]] term $2 \sigma / R$ and the viscous term $4 \mu_L \dot R / R$, with $\mu_L = \rho_L \nu_L$.

Example: an empty cavity ($p_B = 0$) with $\nu_L = 0$, $\sigma = 0$ and constant $p_\infty > 0$ is Rayleigh's collapse problem.
For a cavity at rest at radius $R_0$, the energy integral gives $\dot R^2 = \frac{2 p_\infty}{3 \rho_L} \big( R_0^3 / R^3 - 1 \big)$.
The collapse time is about $0.915 \, R_0 \sqrt{\rho_L / p_\infty}$.

Non-example: a bubble near a wall does not stay spherical, and its radius alone does not determine the flow, so the equation does not apply.

For a gas bubble one often takes $p_B = p_v + p_{g0} (R_0 / R)^{3 \kappa}$, with the vapour pressure $p_v$ and a polytropic exponent $\kappa$.
