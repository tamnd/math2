---
tag: F8RSNQBMBE
kind: concept
name: Fractional Laplacian
msc: [35R11, 26A33, 47G30]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_Laplacian
same_as:
  wikidata: Q30694381
  wikipedia: Fractional Laplacian
---

## Summary

The fractional Laplacian $(-\Delta)^s$, for $0 < s < 1$, is a power of the operator $-\Delta$ built from the [[Laplacian|0E0B6RA8K0]].
It acts on the [[Fourier transform|DPVM34ADZV]] side as multiplication by $\abs{\xi}^{2s}$.
Unlike the Laplacian, it is nonlocal: $(-\Delta)^s u(x)$ depends on the values of $u$ everywhere.
Its negative $-(-\Delta)^s$ is the generator of the rotationally symmetric $2s$-stable Lévy processes.
It appears in models of anomalous diffusion, in the thin obstacle problem and in [[fractional calculus|4V4AGE7XP4]].

## Explanations

### L1 human

The Laplacian compares the value of a function at a point with its average over tiny spheres around the point.
The fractional Laplacian compares it with values at all other points, with weights that decay like a power of the distance.
So a change far away still has a small effect here, which models particles that sometimes make long jumps.
For a wave $\cos(k x)$ on the line, $-\Delta$ multiplies it by $k^2$, and $(-\Delta)^s$ multiplies it by $\abs{k}^{2s}$.
For $s = \tfrac12$ one gets a "square root" of $-\Delta$, which on $\R^n$ is the [[Dirichlet-to-Neumann operator|W783KDGT8E]] of the upper half-space $\R^n \times (0, \infty)$.
