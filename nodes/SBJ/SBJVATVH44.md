---
tag: SBJVATVH44
kind: concept
name: Marsden–Weinstein reduction
msc: [53D20, 37J39]
sources:
  - url: https://en.wikipedia.org/wiki/Momentum_map
---

## Summary

Marsden–Weinstein reduction, also called symplectic reduction, builds a smaller [[symplectic manifold|CAN490EPRT]] from one with a Hamiltonian symmetry.
One takes a level set of the [[moment map|ZARM34FZ6Z]] and divides it by the symmetry group.
It is the geometric form of removing conserved quantities from a mechanical system.
It produces many important spaces, such as complex projective spaces and moduli spaces.

## Explanations

### L1 human

A symmetry of a mechanical system gives conserved quantities, and fixing their values cuts down the phase space.
The symmetry still moves points inside this smaller set, so one also identifies points that differ by a symmetry.
What is left is again a phase space, with two dimensions less for each dimension of the symmetry group.
For example, fixing the energy of $n + 1$ uncoupled harmonic oscillators with equal frequency gives a sphere $S^{2n+1}$, and dividing by the common phase rotation gives the complex projective space $\mathbb{CP}^n$.
