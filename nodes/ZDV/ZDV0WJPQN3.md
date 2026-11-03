---
tag: ZDV0WJPQN3
kind: definition
name: Fluid dynamics
msc: [76A02, 35Q35]
defines: F2JRWJNYN4
uses: [H27M44BV4M, 0299VCW1TH, 18KXZHVF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Fluid_dynamics
---

## Definition

*Fluid dynamics* is the part of [[fluid mechanics|H27M44BV4M]] that studies fluids in motion.
A flow in a region $\Omega \subseteq \R^3$ over a time interval $I$ is given by three fields.
They are a density $\rho \colon \Omega \times I \to (0, \infty)$, a velocity [[vector field|0299VCW1TH]] $\mathbf{u} \colon \Omega \times I \to \R^3$ and a pressure $p \colon \Omega \times I \to \R$.
Fluid dynamics determines these fields from the following laws, written as partial differential equations:

1. conservation of mass;
2. conservation of momentum (Newton's second law for each fluid parcel);
3. conservation of energy, together with an equation of state that links $p$, $\rho$ and the temperature.

## Remarks

Example: for an incompressible viscous fluid of constant density, laws 1 and 2 become the [[Navier–Stokes equations|18KXZHVF4M]], and these determine $\mathbf{u}$ and $p$.
Non-example: a fluid at rest, with $\mathbf{u} = 0$ for all time, belongs to fluid statics rather than fluid dynamics.
A flow is *steady* when the fields do not depend on $t$.
Hydrodynamics usually refers to liquids and aerodynamics to gases.
