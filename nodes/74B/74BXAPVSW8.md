---
tag: 74BXAPVSW8
kind: concept
name: Linear canonical transformation
msc: [44A15, 42A38, 81S30]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_canonical_transformation
same_as:
  wikidata: Q6553419
  wikipedia: Linear canonical transformation
---

## Summary

A linear canonical transformation is an integral transform of functions on $\R$ attached to a real $2 \times 2$ matrix of determinant $1$.
It includes the [[Fourier transform|DPVM34ADZV]], the [[fractional Fourier transform|28VV812XWQ]], the Fresnel transform, scalings and multiplication by chirps as special cases.
Composing two such transforms gives, up to a sign, the transform of the product matrix.
So they form a projective unitary representation of $SL(2, \R)$, which is a genuine representation of the [[metaplectic group|8B0JM2YDE2]].
In optics it describes the propagation of light through lenses and free space in the paraxial approximation.

## Explanations

### L1 human

A signal can be pictured in a plane with time along one axis and frequency along the other.
Linear maps of this plane that keep areas and orientation are given by matrices $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $ad - bc = 1$.
For each such map there is a transform of signals that moves their picture in the plane accordingly.
The Fourier transform is the quarter-turn rotation, a scaling of time is a squeeze of the plane, and multiplying by $e^{i\pi c t^2}$ is a shear.
