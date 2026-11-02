---
tag: 1A01A3EJRX
kind: concept
name: Entropy solution
msc: [35L65, 35D30]
sources:
  - url: https://en.wikipedia.org/wiki/Conservation_law
---

## Summary

An entropy solution of a scalar conservation law $u_t + \operatorname{div} f(u) = 0$ is a [[weak solution|SJZX81A783]] that also satisfies a family of inequalities, the entropy conditions.
Weak solutions of conservation laws are in general not unique, because shocks can be drawn in many ways.
The entropy conditions select the physically relevant solution, the one obtained as the limit of solutions with small added viscosity.
In Kruzhkov's formulation, the entropy solution of the initial value problem exists and is unique for every bounded initial datum.

## Explanations

### L1 human

Solutions of conservation laws, such as models of traffic or gas flow, develop jumps called shocks even from smooth initial data.
Once jumps are allowed, the equation alone permits several solutions, some of them unphysical, like a shock that spontaneously forms from a smooth spreading wave.
The entropy condition is an extra rule saying that information may only flow into a shock, never out of it.
For Burgers' equation $u_t + (u^2/2)_x = 0$, a jump from $1$ down to $0$ is allowed, while a jump from $0$ up to $1$ must instead spread out into a fan.
