---
tag: 9WFT4VY2R7
kind: concept
name: Ray transfer matrix analysis
msc: [78A05]
sources:
  - url: https://en.wikipedia.org/wiki/Ray_transfer_matrix_analysis
same_as:
  wikidata: Q1760601
  wikipedia: Ray transfer matrix analysis
---

## Summary

Ray transfer matrix analysis describes a paraxial optical system by a $2 \times 2$ matrix, the ABCD matrix.
The matrix sends the height and angle of a ray at the input plane to its height and angle at the output plane.
Each element, such as a stretch of free space, a lens or a curved interface, has its own matrix.
The matrix of a system is the product of these.
It gives focal lengths, image positions and stability of laser resonators by simple matrix algebra.
See the [[definition|EM1BMZ6P6D]].

## Explanations

### L1 human

Describe a ray by two numbers: how high above the axis it is, and how steeply it rises.
In the [[paraxial approximation|N111BHFQ2H]], each optical element changes these two numbers linearly, so it acts as a $2 \times 2$ matrix.
Free space of length $d$ keeps the angle and adds $d$ times the angle to the height.
A thin lens keeps the height and tilts the ray toward the axis in proportion to its height.
To follow a ray through a whole system, one multiplies the matrices of its parts.
