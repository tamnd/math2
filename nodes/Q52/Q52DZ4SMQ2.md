---
tag: Q52DZ4SMQ2
kind: concept
name: Wannier function
msc: [82D20, 81Q10]
sources:
  - url: https://en.wikipedia.org/wiki/Wannier_function
same_as:
  wikidata: Q1152058
  wikipedia: Wannier function
---

## Summary

Wannier functions are orthonormal functions attached to the sites of a crystal lattice.
They are obtained from the Bloch functions of a band by a Fourier transform over the [[Brillouin zone|EKTERAYFJ2]].
Each one is a translate of a single function, and together they span the same space as the Bloch functions of the band.
Unlike Bloch functions, which spread over the whole crystal, a good choice of Wannier functions is localised near one site.
They were introduced by Gregory Wannier in 1937, and they are the basis behind tight-binding models.

## Explanations

### L1 human

Bloch waves describe an electron spread over all of a crystal, like a wave on the sea.
Adding up all the Bloch waves of one band with suitable phases makes them cancel everywhere except near one atom.
The result is a Wannier function: a wave packet sitting on one site.
Shifting it by a lattice vector gives the Wannier function of the next site, and all of them are orthogonal.
There is freedom in the phases, and choosing them smoothly makes the Wannier function decay fast away from its site.
