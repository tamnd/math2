---
tag: VZPCZT8ZAN
kind: object
name: Abrikosov vortex lattice
msc: [82D55]
sources:
  - url: https://en.wikipedia.org/wiki/Abrikosov_vortex
---

## Description

Consider a type-II superconductor described by Ginzburg–Landau theory, with Ginzburg–Landau parameter $\kappa > 1/\sqrt{2}$.
Let the applied magnetic field $H$ lie between the lower critical field $H_{c1}$ and the upper critical field $H_{c2}$.
In this range the field enters the sample as a set of parallel flux lines, called Abrikosov vortices.
Around each vortex the complex order parameter $\psi$ vanishes at the core, and its phase winds once by $2\pi$.
Each vortex then carries exactly one flux quantum $\Phi_0 = h/(2e)$, where $h$ is Planck's constant and $e$ is the elementary charge.
The vortices repel each other and settle into a periodic two-dimensional lattice, the *Abrikosov vortex lattice*.
Check of the density: let $B$ be the mean magnetic induction.
Each lattice cell carries flux $\Phi_0$, so the cell area is $\Phi_0 / B$ and the vortex density is $B / \Phi_0$.

## Remarks

Near $H_{c2}$ the order parameter is small, and Abrikosov found lattice solutions of the linearized Ginzburg–Landau equations built from lowest Landau level functions.
Which lattice wins is decided by the Abrikosov parameter $\beta_A = \langle \abs{\psi}^4 \rangle / \langle \abs{\psi}^2 \rangle^2$, where $\langle \cdot \rangle$ is the spatial average; a smaller value means a lower free energy.
The square lattice gives $\beta_A \approx 1.18$ and the triangular lattice gives $\beta_A \approx 1.16$.
So the triangular lattice is the stable one, and it is the lattice seen in experiments on clean samples.

## Explanations

### L1 human

A superconductor normally pushes magnetic field out of itself.
In some superconductors a strong enough field can still get in, but only in thin tubes, each carrying the same tiny amount of magnetic flux.
Inside each tube the superconductivity is destroyed, and around it a current swirls like a whirlpool.
The tubes push each other apart and line up in a regular pattern, like oranges packed in a crate seen from above.
The pattern is a triangular lattice, and doubling the field roughly doubles the number of tubes per unit area.
