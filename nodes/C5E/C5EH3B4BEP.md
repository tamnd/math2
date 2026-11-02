---
tag: C5EH3B4BEP
kind: concept
name: Hamiltonian vector field
msc: [53D05, 37J39, 70H05]
specializes: [0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_vector_field
same_as:
  wikidata: Q2256693
  wikipedia: Hamiltonian vector field
---

## Summary

On a [[symplectic manifold|CAN490EPRT]], every smooth function $H$ determines a [[vector field|0299VCW1TH]] $X_H$, its Hamiltonian vector field.
The symplectic form turns the differential $dH$ into a tangent vector at each point.
The flow of $X_H$ is the motion of a [[Hamiltonian system|0EDKGA2FAK]] with energy $H$, so this notion carries classical mechanics onto curved phase spaces.

## Explanations

### L1 human

Think of $H$ as the energy of a mechanical system, written as a function of position and momentum.
The gradient of $H$ points to where the energy grows fastest.
The Hamiltonian vector field is the gradient turned by a quarter turn, so it points along the level sets of $H$ instead of across them.
For $H(q, p) = \frac{1}{2}(q^2 + p^2)$ on the plane, the field is $X_H = p\,\partial_q - q\,\partial_p$.
Its flow turns the plane around the origin and keeps the energy constant, which is the motion of a harmonic oscillator.
