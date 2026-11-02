---
tag: 1GHF4EKBXS
kind: concept
name: Spectrum
msc: [55P42]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(topology)
same_as:
  wikidata: Q7575269
  wikipedia: Spectrum (topology)
---

## Summary

A spectrum, in algebraic topology, is a sequence of pointed spaces $E_n$ with maps from the suspension of each space to the next one.
Spectra are the objects of stable homotopy theory, much as spaces are the objects of unstable homotopy theory.
Every [[generalized cohomology theory|H28PSZR7XG]] is represented by a spectrum, and spectra have homotopy groups in all integer degrees, including negative ones.

## Explanations

### L1 human

A space can be suspended again and again, and a spectrum is what one gets by allowing the process to run in both directions.
It is a list of spaces $E_0, E_1, E_2, \ldots$ in which each space is glued to the next by a map from its suspension.
The simplest example takes $E_n = S^n$, the $n$-sphere, with the identity maps $\Sigma S^n = S^{n+1}$; this is the sphere spectrum.
Another example uses Eilenberg–MacLane spaces $K(G, n)$, and it gives ordinary cohomology with coefficients in $G$.
