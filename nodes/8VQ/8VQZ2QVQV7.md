---
tag: 8VQZ2QVQV7
kind: definition
name: Multiphase flow
msc: [76T10, 76T06, 76T20]
defines: A3Q9SNF86Q
uses: [F2JRWJNYN4, 18KXZHVF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Multiphase_flow
---

## Definition

Consider a flow of matter in a region $\Omega \subseteq \R^3$.
It is a *multiphase flow* if $m \ge 2$ distinct phases are present.
At each time $t$, the region $\Omega$ is then divided into disjoint open sets $\Omega_1(t), \dots, \Omega_m(t)$ and the interfaces between them.
The set $\Omega_k(t)$ is the part occupied by the $k$-th phase, and it need not be connected.
A phase is a gas, a liquid, a solid, or one of several immiscible liquids.
The interfaces move with the flow.
In each $\Omega_k(t)$ the phase obeys its own equations of motion, for example the [[Navier–Stokes equations|18KXZHVF4M]] with its own density and viscosity.
On the interfaces, conditions couple the phases: conservation of mass and momentum across the interface, and a jump of normal stress given by surface tension.
A *two-phase flow* is the case $m = 2$.

## Remarks

Example: air bubbles rising in water form a two-phase flow, and the set occupied by the gas is the union of the bubbles.
The pressure inside each bubble exceeds the pressure outside by the surface tension jump.

Non-example: salt dissolved in water is not a multiphase flow; the solution is a single phase with no interface, and it is described as a multicomponent mixture.

When the interfaces are too many to track, as in dense sprays, averaged models treat each phase as a continuum with a volume fraction $\alpha_k$, with $\sum_k \alpha_k = 1$.
