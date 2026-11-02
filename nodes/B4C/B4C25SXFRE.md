---
tag: B4C25SXFRE
kind: concept
name: Symplectic integrator
msc: [65P10, 37J11]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_integrator
same_as:
  wikidata: Q7661847
  wikipedia: Symplectic integrator
---

## Summary

A symplectic integrator is a numerical method for [[Hamiltonian systems|0EDKGA2FAK]] whose one-step map is a symplectic map, like the exact flow.
Because it keeps this geometric structure, it avoids the slow drift of energy that ordinary methods show.
Its energy error stays small over very long times.
Examples are the symplectic Euler method, the [[Störmer–Verlet method|ESWE8Y3JD4]] or [[leapfrog method|3HGJCQBWVY]], and the Gauss–Legendre [[Runge–Kutta methods|7DBPJKYC6C]].
They are the standard tools in celestial mechanics and molecular dynamics.

## Explanations

### L1 human

Simulate a planet around the sun with the simple Euler method, and the planet slowly spirals outward, gaining energy it should not have.
A symplectic integrator is designed so that each step preserves areas in the space of positions and momenta, just as the true motion does.
The computed orbit then stays close to a true orbit of a slightly changed system, and the energy only wobbles.
For the harmonic oscillator, the Euler method multiplies $q^2 + p^2$ by $1 + h^2$ at each step, while the symplectic Euler method keeps a nearby quadratic quantity exactly.
