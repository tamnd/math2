---
tag: M36SD56MWQ
kind: concept
name: Green's function for the Laplacian
msc: [31A15, 31B10, 35J05]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_function_for_the_three-variable_Laplace_equation
---

## Summary

The Green's function of a domain for the [[Laplacian|0E0B6RA8K0]] is the potential of a unit point charge in the domain.
The boundary of the domain is held at potential zero.
In a plane domain $\Omega$ with pole $w$, it is a function $g_\Omega(z, w)$ that behaves like $\log(1/\abs{z - w})$ near $w$.
It is [[harmonic|0DEB0JMN0W]] elsewhere and vanishes on the boundary.
It solves the Poisson equation with zero boundary values: $\Delta_z g_\Omega(z, w) = -2\pi \delta_w$.
In free space $\R^3$ the corresponding function is $1/(4\pi\abs{x - y})$, the fundamental solution of the three-variable Laplace equation.
Green's functions give integral formulas for the [[Dirichlet problem|8D56GQ4AG8]] and are invariant under [[conformal maps|0YYT36R4YD]] in the plane.

## Explanations

### L1 human

Place a single point charge inside a grounded metal box.
The electric potential it creates inside the box is the Green's function, with the charge's position as the pole.
Near the charge the potential is huge, and on the walls of the box it is zero.
For the unit disc with the pole at the centre, the Green's function is $\log(1/\abs{z})$, which is $0$ on the unit circle.
