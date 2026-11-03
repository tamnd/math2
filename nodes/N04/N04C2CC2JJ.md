---
tag: N04C2CC2JJ
kind: statement
role: theorem
name: Ewald–Oseen extinction theorem
msc: [78A45, 78A40, 78A10]
uses: [ASQAH710WN, BANHMXD2TD, NM024G378A, 9VGK0SP6EQ, QDV9SBK6W0]
about: [9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Ewald%E2%80%93Oseen_extinction_theorem
same_as:
  wikidata: Q18354377
  wikipedia: Ewald–Oseen extinction theorem
---

## Statement

Let a homogeneous, isotropic, linear, non-magnetic dielectric fill a half-space, with vacuum in the other half-space.
Let a monochromatic [[plane wave|NM024G378A]] of angular frequency $\omega$ come from the vacuum side.
Regard the medium as vacuum filled with oscillating [[electric dipoles|BANHMXD2TD]] with [[polarization density|ASQAH710WN]] $P$.
Let each dipole be driven by the total field at its location.
Then, inside the medium, the field radiated by all the dipoles is the sum of two waves:

1. a wave that travels with speed $c$ and exactly cancels the incident wave;
2. a wave that travels with speed $c / n$, where $n$ is the [[refractive index|9VGK0SP6EQ]] of the medium.

So the total field inside the medium is a single wave of speed $c / n$.

## Remarks

The proof writes the field at a point as the incident field plus the integral of the dipole fields over the half-space.
One looks for a polarization of the form of a plane wave with unknown wave vector inside the medium.
The integral over the half-space then splits into a contribution from the bulk and a contribution from the boundary surface.
The bulk part must reproduce the assumed wave, which fixes its speed $c / n$; the surface part has the vacuum wave vector and must cancel the incident wave.
The cancellation condition gives the amplitude of the transmitted wave, and the field radiated backward by the dipoles gives the reflected wave.

In this way the theorem derives [[Snell's law|QDV9SBK6W0]] and the Fresnel equations from a microscopic picture.

## Explanations

### L1 human

Light slows down in glass, yet the atoms of glass sit in empty space where light travels at its usual speed.
The extinction theorem explains this puzzle.
Each atom is shaken by the light and sends out its own wavelets, all at the usual speed.
Added up, these wavelets wipe out the original wave inside the glass and build a new wave that moves more slowly.

### L2 human

The theorem justifies the macroscopic description of a dielectric by a refractive index.
It shows how the boundary conditions of macroscopic electromagnetism arise from the radiation of the dipoles near the surface.
Together with a local-field model such as the Clausius–Mossotti relation, it links the index $n$ to the polarizability of the molecules.
