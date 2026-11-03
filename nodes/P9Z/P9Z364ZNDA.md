---
tag: P9Z364ZNDA
kind: concept
name: Uniform theory of diffraction
msc: [78A45, 78M35]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_theory_of_diffraction
same_as:
  wikidata: Q7885118
  wikipedia: Uniform theory of diffraction
---

## Summary

The uniform theory of diffraction (UTD) is a high-frequency method for computing waves scattered by objects with edges, corners and curved surfaces.
It adds diffracted rays to the rays of geometrical optics, as in [[Keller's geometrical theory of diffraction|ES9KPGJAGS]].
Keller's diffraction coefficients become infinite at the shadow and reflection boundaries, where the geometrical-optics field jumps.
UTD multiplies them by a transition function built from a [[Fresnel integral|D0TQ9F2ZDW]], so that the total field is finite and continuous there.
It was developed by Kouyoumjian and Pathak, and it is widely used for antennas on vehicles and for radio propagation in cities.

## Explanations

### L1 human

Light or radio waves behind a sharp edge do not stop abruptly: some energy bends into the shadow.
UTD describes this as new rays that start at the edge and spread out in all directions.
Simple formulas for these rays fail right at the border of the shadow, where they blow up.
UTD repairs them with a correction factor that smoothly joins the lit side and the shadow side.
