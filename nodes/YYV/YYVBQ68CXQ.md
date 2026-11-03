---
tag: YYVBQ68CXQ
kind: concept
name: Rayleigh dissipation function
msc: [70H03, 70F40]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_dissipation_function
same_as:
  wikidata: Q4162366
  wikipedia: Rayleigh dissipation function
---

## Summary

The Rayleigh dissipation function is a quadratic function of the generalized velocities that describes friction forces proportional to velocity.
Its derivatives give the friction forces, so viscous [[damping|RJX78YZ6XD]] fits into the [[Lagrange equations|BEM454AYTT]] with one extra term.
Twice its value is the rate at which the system loses energy.
See the [[definition|X5ZH6CS7QF]].

## Explanations

### L1 human

The Lagrangian method handles forces that come from a potential energy, but friction does not come from a potential.
For friction that grows linearly with speed, such as a shock absorber or air drag at low speed, there is a simple fix.
One writes down a second function $F$, built from the velocities, and the friction force is minus its derivative.
For a mass on a spring with a damper of constant $c$, $F = \frac{1}{2} c \dot x^2$ and the friction force is $-c \dot x$.
The energy of the system then falls at the rate $2F$.
