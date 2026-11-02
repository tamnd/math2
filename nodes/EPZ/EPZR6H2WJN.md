---
tag: EPZR6H2WJN
kind: concept
name: Schrödinger equation
msc: [35Q41, 81Q05, 35Q40]
sources:
  - url: https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation
same_as:
  wikidata: Q165498
  wikipedia: Schrödinger equation
---

## Summary

The Schrödinger equation $i\hbar\, \partial_t \psi = -\frac{\hbar^2}{2m} \Delta \psi + V \psi$ describes how the wave function $\psi$ of a quantum particle of mass $m$ in a potential $V$ evolves in time.
It is a linear dispersive partial differential equation with complex-valued solutions.
Its right-hand side is a [[Schrödinger operator|89AA6XJY5K]] applied to $\psi$.
The solutions are given by a unitary group of operators, so the total probability $\int \abs{\psi}^2 \, dx$ is conserved.
It is the basic equation of non-relativistic quantum mechanics and a model problem for dispersive equations.

## Explanations

### L1 human

In quantum mechanics a particle is described by a complex wave, and $\abs{\psi(x, t)}^2$ is the probability density of finding it at $x$ at time $t$.
The Schrödinger equation says how this wave moves: the kinetic energy term spreads it out, and the potential bends it.
A free particle is a superposition of plane waves $e^{i(k \cdot x - \abs{k}^2 t)}$, in units where $\hbar = 1$ and $2m = 1$.
Waves with larger $k$ move faster, so a localised wave packet spreads out in time, which is the typical behaviour of dispersive equations.
