---
tag: 2PCVRG9NBN
kind: concept
name: Born series
msc: [81U05, 45B05]
sources:
  - url: https://en.wikipedia.org/wiki/Born_series
same_as:
  wikidata: Q18960800
  wikipedia: Born series
---

## Summary

The Born series is the expansion of a scattered wave in powers of the scattering potential.
It is obtained by iterating the [[Lippmann–Schwinger equation|MW5R19P2X4]] $\psi = \phi + G_0 V \psi$, which gives $\psi = \phi + G_0 V \phi + G_0 V G_0 V \phi + \cdots$.
It is the [[Liouville–Neumann series|H1HWSWME6B]] of this integral equation.
So it converges when the operator $G_0 V$ is small, for example for weak potentials or at high energy.
Its first term beyond $\phi$ is the Born approximation, the standard first estimate of scattering amplitudes.

## Explanations

### L1 human

A wave meets an obstacle and is scattered once, then the scattered wave is scattered again, and so on.
The Born series adds up these contributions: no scattering, one scattering event, two events, and so on.
When the obstacle is weak, each extra event is much smaller than the last, so the first one or two terms already give a good answer.
