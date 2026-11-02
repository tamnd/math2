---
tag: PRJCH788AM
kind: concept
name: Eta invariant
msc: [58J28, 58J50]
sources:
  - url: https://en.wikipedia.org/wiki/Eta_invariant
same_as:
  wikidata: Q5402374
  wikipedia: Eta invariant
---

## Summary

The eta invariant of a self-adjoint elliptic operator on a closed manifold measures the asymmetry of its spectrum between positive and negative eigenvalues.
It is the value at $s = 0$ of the eta function $\sum \operatorname{sign}(\lambda) \abs{\lambda}^{-s}$, defined by analytic continuation.
Atiyah, Patodi and Singer introduced it as the boundary correction in their [[index theorem for manifolds with boundary|GGFAH1M80J]].

## Explanations

### L1 human

A self-adjoint operator has real eigenvalues, some positive and some negative, usually infinitely many of each.
One would like to count the positive ones minus the negative ones, but both counts are infinite.
The eta invariant is a regularized value of this difference, obtained by weighting each eigenvalue by $\abs{\lambda}^{-s}$ and continuing to $s = 0$.
If the spectrum is symmetric about $0$, the eta invariant is $0$.
