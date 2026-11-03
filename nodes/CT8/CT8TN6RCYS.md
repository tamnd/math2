---
tag: CT8TN6RCYS
kind: definition
name: Babcock–Leighton model
msc: [85A30, 76W05]
defines: CFAQFR06CT
uses: [NPVYXT6WHA, AFVDBT0K5C]
sources:
  - url: https://en.wikipedia.org/wiki/Solar_dynamo
---

## Definition

A *Babcock–Leighton model* is a model of the [[solar dynamo|NPVYXT6WHA]] for the axisymmetric mean field of the Sun in which these three mechanisms act.

1. The differential rotation of the Sun stretches the poloidal field into a toroidal field (the $\Omega$-effect).
2. The toroidal field near the base of the convection zone rises and emerges at the surface as bipolar active regions.
   Their axes are tilted with respect to the east–west direction, with the leading polarity nearer the equator.
   The surface decay of these regions is the only source of new poloidal field, so this source is concentrated near the surface.
3. Field is transported between the surface source and the deep toroidal field by turbulent diffusion, and in flux-transport versions also by the meridional circulation.

## Remarks

In the mean-field language of [[dynamo theory|AFVDBT0K5C]], clause 2 is a source term for the poloidal field, localized at the surface.
It is proportional to the toroidal field at the base of the convection zone, instead of being a local $\alpha$-effect in the bulk.

Example: take a flux-transport model with solar differential rotation, a poleward surface meridional flow and a surface poloidal source.
It satisfies the three clauses.
It produces a cycle in which the toroidal field migrates toward the equator, as the sunspot belts do.

Non-example: in a classical $\alpha\Omega$ model, helical turbulence produces the poloidal field throughout the convection zone.
This fails clause 2, since the poloidal source is not tied to the emergence and decay of active regions.

The tilt of the bipolar regions grows with latitude, an observed regularity known as Joy's law.
