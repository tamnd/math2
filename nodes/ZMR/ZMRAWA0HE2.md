---
tag: ZMRAWA0HE2
kind: concept
name: Laser rate equations
msc: [78A60, 34C60]
sources:
  - url: https://en.wikipedia.org/wiki/Rate_equation
---

## Summary

The laser rate equations are a system of ordinary differential equations for a laser.
The unknowns are the population inversion of the gain medium and the number of photons in the cavity.
They model pumping, spontaneous decay, stimulated emission and cavity losses as rates of gain and loss.
They predict the lasing threshold, the output power above threshold, and relaxation oscillations after the laser is switched on.
They are a simplification of the [[Maxwell–Bloch equations|H8Z49EWR5Q]] when the polarization of the medium decays fast.

## Explanations

### L1 human

Inside a laser there are two populations to keep track of: excited atoms and photons.
The pump makes excited atoms, and each excited atom can decay on its own or be stimulated by a photon to give a second photon.
Photons leak out of the cavity through the mirrors, and that is the laser beam.
Writing how fast each population goes up and down gives two coupled equations.
They show that the laser only turns on once the pump beats a threshold.
