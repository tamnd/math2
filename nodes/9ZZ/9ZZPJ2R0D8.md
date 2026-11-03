---
tag: 9ZZPJ2R0D8
kind: concept
name: Rigorous coupled-wave analysis
msc: [78A45, 78M22]
sources:
  - url: https://en.wikipedia.org/wiki/Rigorous_coupled-wave_analysis
same_as:
  wikidata: Q7333866
  wikipedia: Rigorous coupled-wave analysis
---

## Summary

Rigorous coupled-wave analysis (RCWA) computes the diffraction of light by periodic structures such as gratings and [[photonic crystal|2PBQKKP2N5]] slabs.
It expands the fields and the permittivity in [[Fourier series|G12KXDHPPS]] along the periods.
Then [[Maxwell's equations|9BWWD4QK8Y]] become a system of ordinary differential equations in the depth.
The structure is cut into layers that are uniform in depth, and the system is solved in each layer by eigenvectors.
The layers are joined as in the [[transfer-matrix method|G5Q62JS3JM]].
It is also called the Fourier modal method, and it is due to Moharam and Gaylord.

## Explanations

### L1 human

A grating splits an incoming beam into several beams, its diffraction orders, at angles given by the [[grating equation|TWYY4JN7K1]].
RCWA computes how much light goes into each order.
It writes the field as a sum of the waves of all orders and lets the grating mix them.
Keeping more orders makes the answer more accurate, at the cost of larger matrices.
