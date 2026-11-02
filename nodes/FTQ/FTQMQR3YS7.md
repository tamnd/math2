---
tag: FTQMQR3YS7
kind: concept
name: Spectral triple
msc: [58B34, 46L87]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_triple
same_as:
  wikidata: Q17103517
  wikipedia: Spectral triple
---

## Summary

A spectral triple $(A, H, D)$ consists of an algebra $A$ of operators on a Hilbert space $H$ and an unbounded self-adjoint operator $D$ on $H$.
The operator $D$ has compact resolvent, and its commutators with elements of $A$ are bounded.
It is the noncommutative version of a compact Riemannian spin manifold together with its [[Dirac operator|3DXGJTEQZH]].
From a spectral triple one recovers a distance, a dimension and an integral, so it encodes metric geometry in operator language.

## Explanations

### L1 human

On a compact manifold, the Dirac operator is a first-order differential operator that knows the shape of the manifold.
Its eigenvalues grow at a rate fixed by the dimension, and the size of the commutator $[D, f]$ measures how fast a function $f$ changes.
A spectral triple keeps only these features: an algebra standing for the functions, a Hilbert space on which they act, and an operator $D$ standing for the Dirac operator.
The simplest example is the circle: functions on the circle act on $L^2(S^1)$, and $D = -i \, d/d\theta$ has eigenvalues the integers.
The algebra need not be commutative, which allows "spaces" with no points in the usual sense.
