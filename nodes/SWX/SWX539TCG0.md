---
tag: SWX539TCG0
kind: concept
name: Tjurina number
msc: [32S05, 14B07, 32S30]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_number
---

## Summary

The Tjurina number of an isolated hypersurface singularity is the dimension of the space of its first-order deformations up to coordinate changes.
It is the number of parameters of a miniversal deformation of the hypersurface germ.
It is computed from the defining function and its partial derivatives, and it is at most the Milnor number.
K. Saito proved that the two numbers are equal exactly when the function is quasi-homogeneous in suitable coordinates.

## Explanations

### L1 human

The Tjurina number counts the essentially different ways to perturb a singular point of a hypersurface, such as the tip of a cone or the cusp of a curve.
For the cusp curve $x^2 + y^3 = 0$ it is $2$: the perturbations $x^2 + y^3 + a y + b$ already capture every nearby curve up to a change of coordinates.
It differs from the Milnor number because it allows multiplying the equation by a nonvanishing function, which changes the function but not the hypersurface.
