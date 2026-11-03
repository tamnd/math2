---
tag: CKSHWY5BKY
kind: concept
name: T-matrix method
msc: [78A45, 78M16, 35P25]
sources:
  - url: https://en.wikipedia.org/wiki/T-matrix_method
same_as:
  wikidata: Q4291851
  wikipedia: T-matrix method
---

## Summary

The T-matrix method describes [[scattering|8BQYB8H5CT]] by a particle through a single linear map, the transition matrix.
Incident and scattered waves are expanded in spherical wave functions.
The T-matrix sends the coefficients of the incident wave to those of the scattered wave.
It depends only on the particle and the frequency, not on the incident wave.
This makes it efficient for averages over orientations and for clusters of particles.
See the [[definition|A0XKB446P9]].

## Explanations

### L1 human

Think of the particle as a black box with an input and an output.
The input is the incoming wave written as a sum of standard spherical pieces, and the output is the scattered wave written the same way.
The T-matrix is the table that turns input numbers into output numbers.
Once the table is known, any incoming wave, from any direction, can be handled by a matrix product.
For a sphere the table is diagonal, and its entries are the classical Mie coefficients.
