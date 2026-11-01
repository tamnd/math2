---
tag: ZW2RBS9VTR
kind: concept
name: Langevin equation
msc: [60H10, 82C31]
sources:
  - url: https://en.wikipedia.org/wiki/Langevin_equation
same_as:
  wikidata: Q584537
  wikipedia: Langevin equation
---

## Summary

The Langevin equation is a stochastic differential equation for the motion of a particle in a fluid.
It combines a deterministic force, a friction force proportional to the velocity, and a random force from collisions with the molecules of the fluid.
The friction and the strength of the noise are tied by the temperature, so that the particle reaches thermal equilibrium.
Without an external force, the velocity is an [[Ornstein–Uhlenbeck process|HZM2ASCDY4]].

## Explanations

### L1 human

A pollen grain in water is pushed by countless water molecules.
On average these pushes slow the grain down, like friction, but they also shake it at random.
The Langevin equation is Newton's law with these two extra forces added.
The random kicks keep the grain moving, while the friction keeps its speed from growing without bound.
In the long run, the velocity of the grain has a normal law whose variance is the temperature divided by the mass, in suitable units.
