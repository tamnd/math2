---
tag: M8F0SGSGQW
kind: concept
name: Mindlin–Reissner plate theory
msc: [74K20, 74B05]
specializes: [782XMC21FH]
sources:
  - url: https://en.wikipedia.org/wiki/Reissner–Mindlin_plate_theory
same_as:
  wikidata: Q3564249
  wikipedia: Reissner–Mindlin plate theory
---

## Summary

Mindlin–Reissner plate theory is a [[plate theory|782XMC21FH]] for moderately thick plates that takes transverse shear deformation into account.
Normals to the mid-plane stay straight but may tilt away from the normal of the deformed mid-plane.
So the rotations of the normals are unknowns besides the deflection.
It is the plate analogue of [[Timoshenko–Ehrenfest beam theory|K4W0JQ1K6Z]] and reduces to [[Kirchhoff–Love plate theory|9E6E0SCEYA]] when the shear stiffness becomes infinite.
It is widely used in finite element analysis, where it needs only continuous, not continuously differentiable, approximations.

## Explanations

### L1 human

In a thin plate, lines across the thickness stay at right angles to the bent surface.
In a thicker plate the layers also slide a little over each other, so these lines lean over.
Mindlin–Reissner theory lets each such line tilt by its own amount, and it adds a shear energy for the leaning.
This gives a better answer for thick plates and for the vibrations of plates at high frequency.
