---
tag: G5Q62JS3JM
kind: concept
name: Transfer-matrix method in optics
msc: [78A40, 78A10]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer-matrix_method_(optics)
same_as:
  wikidata: Q7833984
  wikipedia: Transfer-matrix method (optics)
---

## Summary

The transfer-matrix method computes the reflection and transmission of a [[plane wave|NM024G378A]] by a stack of flat homogeneous layers.
Each layer is described by a $2 \times 2$ matrix that maps the tangential fields at one face to those at the other.
The matrix of the whole stack is the product of the layer matrices, and the reflection and transmission coefficients follow from it.
It is the standard tool for anti-reflection coatings, dielectric mirrors and [[thin-film interference|K8VR0H7M9X]], and it extends the [[Fresnel equations|ARTBZGVY72]] from one interface to many.
It should not be confused with [[ray transfer matrix analysis|9WFT4VY2R7]], which uses $2 \times 2$ matrices for rays in geometrical optics.

## Explanations

### L1 human

Light hitting a coated lens is partly reflected at every boundary between layers, and the reflected waves interfere.
Tracking all these echoes one by one is tedious.
The transfer-matrix method packs the effect of each layer into a small matrix, and multiplying the matrices accounts for all the echoes at once.
For example, a single layer whose thickness is a quarter of the wavelength inside it, with the right refractive index, cancels the reflection of a glass surface.
