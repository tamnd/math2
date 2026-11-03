---
tag: P6HAX0MH0B
kind: concept
name: Molecular dynamics
msc: [82M37, 65P10]
sources:
  - url: https://en.wikipedia.org/wiki/Molecular_dynamics
same_as:
  wikidata: Q901663
  wikipedia: Molecular dynamics
---

## Summary

Molecular dynamics is the computer simulation of a system of many particles by numerical integration of [[Newton's laws of motion|KNBP19FG6K]].
The forces come from a model potential, such as the [[Lennard-Jones potential|349MN3ER54]].
The equations are solved step by step, usually with the [[Verlet integration|ESWE8Y3JD4]] scheme.
Under the [[ergodic hypothesis|3MY6RYD0PD]], averages over the computed trajectory estimate equilibrium averages.
The trajectory itself gives dynamical quantities such as diffusion coefficients.
It is a basic tool of statistical physics, chemistry, materials science and biophysics.

## Explanations

### L1 human

Molecular dynamics is a movie of atoms made by a computer.
At each tiny time step the computer works out the force on each atom from the positions of the others, then moves all atoms a little.
Repeating this millions of times shows how a liquid flows, a crystal melts or a protein folds.
For example, a box of a few thousand argon atoms with a Lennard-Jones potential already behaves like real liquid argon.
The time step must be much shorter than the fastest vibration, typically about a femtosecond.
