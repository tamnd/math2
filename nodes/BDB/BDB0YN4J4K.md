---
tag: BDB0YN4J4K
kind: definition
name: Metamaterial
msc: [78A48, 78A10]
defines: CQ9A45JF68
uses: [F768YN0P2V, 5MJQ5J5H8Z, 604T74VWDK]
sources:
  - url: https://en.wikipedia.org/wiki/Metamaterial
---

## Definition

A *metamaterial* for waves of wavelength $\lambda$ is an artificial medium with these properties.
1. It is built from a periodic or random arrangement of structured elements, its *unit cells*, whose size and spacing are much smaller than $\lambda$.
2. For waves of wavelength $\lambda$ it behaves as a homogeneous medium with effective [[constitutive relations|604T74VWDK]].
They have an effective [[permittivity|F768YN0P2V]] $\varepsilon_{\mathrm{eff}}$ and an effective [[permeability|5MJQ5J5H8Z]] $\mu_{\mathrm{eff}}$.
3. These effective parameters are determined mainly by the geometry of the unit cells, and they take values not found in the constituent materials.

## Remarks

Example: take a lattice of small split metal rings, with spacing much less than the wavelength.
Near the resonance of the rings, its effective permeability is negative over a band of frequencies.
A lattice of thin metal wires has a negative effective permittivity below an effective plasma frequency.
Combining the two gives a medium with $\varepsilon_{\mathrm{eff}} < 0$ and $\mu_{\mathrm{eff}} < 0$, and thus a negative refractive index.

Non-example: a photonic crystal with period comparable to $\lambda$ fails clause 1 and clause 2.
Waves resolve its structure, and its behaviour comes from Bragg scattering rather than from effective parameters.

The effective parameters are frequency dependent, and passive metamaterials with negative parameters are necessarily dispersive; in practice they are also lossy.
