---
tag: NYHNTP9AND
kind: concept
name: de Branges space
msc: ["46E22", 30D20]
sources:
  - url: https://en.wikipedia.org/wiki/De_Branges_space
same_as:
  wikidata: Q5244279
  wikipedia: De Branges space
---

## Summary

A de Branges space is a Hilbert space of [[entire functions|0419794R0T]] built from one entire function $E$.
The function $E$ must be larger at each point of the upper half-plane than at the mirror point in the lower half-plane.
Its elements are the entire functions $F$ such that $F/E$ and $F^\#/E$ lie in the Hardy space of the [[upper half-plane|X6XGGH5FPW]].
The norm of $F$ is the $L^2$ norm of $F/E$ on the real line.
It is a reproducing kernel Hilbert space with an explicit kernel, and it generalises the Paley–Wiener spaces.
De Branges used these spaces in the spectral theory of canonical systems.

## Explanations

### L1 human

Choose an entire function $E$ with $\abs{E(\bar z)} < \abs{E(z)}$ whenever $z$ is in the upper half-plane.
The space $\mathcal{H}(E)$ collects entire functions that are "no larger than $E$" in a precise square-integrable sense.
For $E(z) = e^{-iaz}$ with $a > 0$, one gets the Paley–Wiener space of square-integrable band-limited functions, whose Fourier transforms live on $[-a, a]$.
Each point evaluation $F \mapsto F(w)$ is a bounded functional, given by an inner product with an explicit kernel.
