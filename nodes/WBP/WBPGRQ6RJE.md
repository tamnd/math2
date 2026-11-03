---
tag: WBPGRQ6RJE
kind: concept
name: Angular spectrum method
msc: [78A45, 42B10, 35J05]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_spectrum_method
same_as:
  wikidata: Q3492872
  wikipedia: Angular spectrum method
---

## Summary

The angular spectrum method computes how a monochromatic wave field propagates from one plane to a parallel plane.
It writes the field in the first plane as a superposition of [[plane waves|NM024G378A]] by a two-dimensional [[Fourier transform|DPVM34ADZV]].
Then it moves each plane wave by multiplying it by a phase factor, and transforms back.
Components with high spatial frequency become [[evanescent waves|VT8YK4WC0H]] that decay away from the plane.
The method is exact for the [[Helmholtz equation|MNXKTXJ35G]] in a homogeneous medium and is equivalent to the [[Rayleigh–Sommerfeld formula|3B5D567BEK]].

## Explanations

### L1 human

Any light pattern on a plane can be built by adding plane waves travelling in different directions.
Each plane wave travels in a very simple way: it just picks up a phase as it moves.
So to know the pattern on a later plane, split the pattern into plane waves, let each one travel, and add them up again.
Fine details of the pattern correspond to waves that would have to travel at impossible angles, and these die out within a wavelength or so.
