---
tag: VXDEQB46GV
kind: concept
name: Hamiltonian operator
msc: ["81Q10", "47B25", "81Q05"]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics)
same_as:
  wikidata: Q660488
  wikipedia: Hamiltonian (quantum mechanics)
---

## Summary

The Hamiltonian of a quantum system is the [[observable|DF5RN297GE]] of its total energy.
It is a self-adjoint operator $H$ that also drives the time evolution.
By [[Stone's theorem|DVGQB92HPJ]], $U(t) = e^{-itH/\hbar}$ is a group of [[unitary operators|MM0EJ2GDE4]], and state vectors evolve by $\psi(t) = U(t)\psi(0)$.
For a particle of mass $m$ in a potential $V$, it is the [[Schrödinger operator|89AA6XJY5K]] $-\frac{\hbar^2}{2m}\Delta + V$, the sum of kinetic and potential energy.
Its spectrum gives the possible energies, and its eigenvectors are the stationary states.
It is the quantum counterpart of the Hamiltonian function of [[Hamiltonian mechanics|MPM0RHWCN6]].

## Explanations

### L1 human

The Hamiltonian is the energy of a quantum system, written as an operator.
It has a second job: it says how the state changes in time, through the [[Schrödinger equation|EPZR6H2WJN]].
For a particle, it adds a kinetic part, which depends on how fast the wave function wiggles, and a potential part, which depends on where it is.
For a harmonic oscillator with $\hbar = m = \omega = 1$, it is $-\frac12 \frac{d^2}{dx^2} + \frac12 x^2$, and its eigenvalues are the energy levels $\frac12, \frac32, \frac52, \dots$.
