---
tag: 89AA6XJY5K
kind: concept
name: Schrödinger operator
msc: [34L40, 35J10, 81Q10]
sources:
  - url: https://en.wikipedia.org/wiki/Schrödinger_equation
---

## Summary

A Schrödinger operator is a differential operator of the form $-\Delta + V$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] and $V$ is a real function called the potential.
In one dimension it is the operator $-\frac{d^2}{dx^2} + V(x)$.
Its eigenvalue equation is the time-independent Schrödinger equation of quantum mechanics, and its eigenvalues are the allowed energies of a particle in the potential $V$.
In the theory of ordinary differential equations it is the main example of a Sturm–Liouville operator.

## Explanations

### L1 human

The operator takes a function, measures how much it bends with the second derivative, and adds the function times the potential.
In physics the bending term is the kinetic energy and $V$ is the potential energy.
For $V(x) = x^2$ the operator $-y'' + x^2 y$ is the quantum harmonic oscillator.
Its eigenvalues are $1, 3, 5, \ldots$, and the first eigenfunction is $e^{-x^2/2}$.
