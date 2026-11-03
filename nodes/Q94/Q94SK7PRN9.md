---
tag: Q94SK7PRN9
kind: concept
name: Eshelby energy-momentum tensor
msc: [74A45, 74B20, 74R10]
sources:
  - url: https://en.wikipedia.org/wiki/Configurational_mechanics
---

## Summary

The Eshelby energy-momentum tensor is a second-order tensor built from the strain energy density and the stress of an elastic body.
Its divergence vanishes at equilibrium in a homogeneous [[hyperelastic material|ZHK2EVRD90]] without body forces.
So its flux through a closed surface is zero unless the surface encloses a defect.
The flux around a defect, such as a crack tip, a dislocation or an inclusion, is the configurational force on it.
This force is the rate of decrease of energy when the defect moves.
The [[J-integral|BZ2WFST50T]] of fracture mechanics is the flux of its first row around a crack tip.

## Explanations

### L1 human

Ordinary forces push material points; configurational forces push defects through the material.
If a hole, a crack or an inclusion moves a little inside a stressed body, the stored energy changes, and the rate of change is a force on the defect.
The Eshelby tensor is the bookkeeping device that gives this force as an integral over any surface around the defect.
Because the tensor is divergence-free away from defects, the surface can be chosen far away, where the fields are easy to compute.
