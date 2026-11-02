---
tag: DCCA2T9GKH
kind: concept
name: Fejér kernel
msc: ["42A24", "40G05"]
sources:
  - url: https://en.wikipedia.org/wiki/Fejér_kernel
same_as:
  wikidata: Q1402176
  wikipedia: Fejér kernel
---

## Summary

The Fejér kernel $F_N$ is the average of the first $N$ Dirichlet kernels, the trigonometric polynomials that produce the partial sums of a [[Fourier series|G12KXDHPPS]].
Convolving a periodic function with $F_N$ gives the $N$-th [[Cesàro mean|08R2V9GZF7]] of its Fourier partial sums.
Unlike the Dirichlet kernel, the Fejér kernel is nonnegative, has total mass $1$ and concentrates near $0$.
These three properties are the heart of [[Fejér's theorem|TPJZCSXSVN]].

## Explanations

### L1 human

A Fourier partial sum is an average of the function against a weight, the Dirichlet kernel, which takes negative values and oscillates strongly.
Averaging these weights over the first $N$ steps gives the Fejér kernel, which is never negative.
Its graph is a tall narrow bump at $0$ with small ripples elsewhere, and the bump gets narrower as $N$ grows.
So convolving with it computes a local average of the function, which approaches the value of the function at each point of continuity.
