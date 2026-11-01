---
tag: AQ75M2JTB2
kind: concept
name: Schramm–Loewner evolution
msc: [60J67, 30C35, 82B27]
sources:
  - url: https://en.wikipedia.org/wiki/Schramm%E2%80%93Loewner_evolution
same_as:
  wikidata: Q7432797
  wikipedia: Schramm–Loewner evolution
---

## Summary

The Schramm–Loewner evolution with parameter $\kappa > 0$, written $\mathrm{SLE}_\kappa$, is a random curve in a planar domain.
It is obtained from the [[Loewner differential equation|51G4QJZ345]] driven by a multiple of a Brownian motion.
Oded Schramm introduced it in 2000 as the candidate scaling limit of interfaces in planar models of statistical physics that are conformally invariant.
It is characterised by conformal invariance together with a domain Markov property, and the single parameter $\kappa$ governs the shape of the curve.

## Explanations

### L1 human

Many random paths on a fine lattice, such as the boundary of a cluster in critical percolation, look the same at every scale.
In the limit, they are unchanged by conformal maps.
Schramm found that any such limiting random curve must be described by the Loewner equation with a driving function $\sqrt{\kappa}\, B_t$, where $B_t$ is a Brownian motion.
Small $\kappa$ gives curves that are nearly straight, and larger $\kappa$ gives curves that wiggle more, touch themselves, and for $\kappa \ge 8$ fill the whole domain.
For example $\kappa = 6$ describes the limit of percolation interfaces on the triangular lattice.
