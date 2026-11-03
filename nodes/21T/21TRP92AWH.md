---
tag: 21TRP92AWH
kind: concept
name: Beam propagation method
msc: [78A40, 78M20, 65M06]
sources:
  - url: https://en.wikipedia.org/wiki/Beam_propagation_method
same_as:
  wikidata: Q4876189
  wikipedia: Beam propagation method
---

## Summary

The beam propagation method computes how a light beam evolves along a waveguide or another slowly varying structure.
It replaces the [[Helmholtz equation|MNXKTXJ35G]] by the [[paraxial wave equation|53DCTAEM5M]] for a slowly varying envelope, which is first order in the direction of propagation.
The field is then marched step by step along that direction, for example by the split-step Fourier method or by finite differences.
It is a standard tool for optical fibres and integrated optics.

## Explanations

### L1 human

A laser beam in a fibre moves mostly forward, with slow changes in its shape.
The method follows the cross-section of the beam slice by slice along the fibre, like the frames of a film.
Each step lets the beam spread a little, as it does in free space, and then bends it according to the refractive index of the slice.
Waves going backwards are ignored, which is what makes the method fast.
