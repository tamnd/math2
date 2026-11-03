---
tag: SB4N1BTRAQ
kind: concept
name: Vlasov–Poisson system
msc: [35Q83, 82C40, 82D10]
specializes: [SJH7M2VCTE]
sources:
  - url: https://en.wikipedia.org/wiki/Vlasov_equation
---

## Summary

The Vlasov–Poisson system is the [[Vlasov equation|SJH7M2VCTE]] in which the force is the gradient of a potential.
The potential solves [[Poisson's equation|DWK5N5SKTK]] with the particle density as source.
It describes a large collection of particles that interact only through their common electric or gravitational field, with collisions neglected.
With a repulsive force it models a plasma of electrons, and with an attractive force it models stars in a galaxy.
It is a basic nonlinear kinetic equation, with conserved mass and energy, and with phenomena such as Landau damping.

## Explanations

### L1 human

Imagine a cloud of charged particles flying around.
Each particle feels the electric field made by all the others, and the particles move according to that field.
As they move, the field changes, which changes their motion again.
The Vlasov–Poisson system follows this loop for the density of particles in positions and velocities.
For stars the same loop holds with gravity, which pulls instead of pushes.
