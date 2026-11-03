---
tag: FNZBEP8JN4
kind: definition
name: Fluid–structure interaction
msc: [74F10, 76D05]
defines: 7QE6ZASKWH
uses: [18KXZHVF4M, T1PYEBKBAJ, KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Fluid%E2%80%93structure_interaction
---

## Definition

Let $\Omega_f(t)$ and $\Omega_s(t)$ be the regions filled at time $t$ by a fluid and by a deformable solid.
Let $\Gamma(t)$ be their common interface, with unit normal $n$.
Let $v$ be the fluid velocity and $\sigma_f$ the fluid [[Cauchy stress|KG2XWEMJ30]], and let $d$ be the solid displacement and $\sigma_s$ the solid Cauchy stress.
A *fluid–structure interaction problem* asks for $v$, the fluid pressure and $d$ such that:

1. $v$ and the pressure solve the fluid equations, for example the [[Navier–Stokes equations|18KXZHVF4M]], in $\Omega_f(t)$.
2. $d$ solves the equations of [[elastodynamics|T1PYEBKBAJ]] (or of a nonlinear elastic model) in $\Omega_s(t)$.
3. The velocities agree on the interface: $v = \partial_t d$ on $\Gamma(t)$.
4. The tractions balance on the interface: $\sigma_f n = \sigma_s n$ on $\Gamma(t)$.
5. The fluid region moves with the solid: $\Gamma(t)$ is the image of the reference interface under the solid motion.

## Remarks

Example: blood in an elastic artery.
The blood solves the Navier–Stokes equations inside the vessel and the wall solves an elastic model.
The blood sticks to the moving wall and its pressure loads the wall, so all five clauses hold.

Non-example: flow past a rigid cylinder held fixed.
The solid does not deform, so clauses 2, 3 and 5 reduce to a fixed no-slip boundary and the problem is a pure fluid problem.

Clauses 3 and 4 are called the kinematic and the dynamic coupling conditions.
When the fluid loads the solid but the deformation is too small to change the flow, one speaks of one-way coupling.
