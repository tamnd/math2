---
tag: 6T7S8QEBKY
kind: concept
name: Phonon dispersion in lattices
msc: [74J05, "74E15", 74A25]
sources:
  - url: https://en.wikipedia.org/wiki/Phonon
---

## Summary

Phonon dispersion is the relation between wave vector and frequency for small vibrations of a crystal.
The crystal is modelled as a lattice of atoms joined by elastic forces.
For each wave vector the possible frequencies are the square roots of the eigenvalues of a Hermitian matrix, the dynamical matrix.
As the wave vector varies, they form several branches.
At long wavelengths the lowest branches are linear in the wave vector and give the elastic sound waves of continuum [[elastodynamics|T1PYEBKBAJ]].
At short wavelengths the discreteness of the lattice shows, and the waves become dispersive.

## Explanations

### L1 human

Picture a long row of equal balls joined by equal springs.
A wave can run along the row, and its frequency depends on its wavelength.
For long waves the row behaves like a continuous elastic rod and the frequency is proportional to the wave number.
For waves only a few balls long the frequency grows more slowly and stops at a maximum, because no wave can be shorter than two spacings.
For a row with spring constant $K$, ball mass $m$ and spacing $a$, the frequency of the wave with wave number $k$ is $2\sqrt{K/m}\,\abs{\sin(ka/2)}$.
