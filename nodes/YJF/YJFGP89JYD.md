---
tag: YJFGP89JYD
kind: concept
name: Loop algebra
msc: [17B65, 17B67]
specializes: [Z3VCZYHPKY]
sources:
  - url: https://en.wikipedia.org/wiki/Loop_algebra
same_as:
  wikidata: Q17098626
  wikipedia: Loop algebra
---

## Summary

The loop algebra of a [[Lie algebra|5JJYBJ6A8K]] $\mathfrak{g}$ is the Lie algebra $\mathfrak{g} \otimes k[t, t^{-1}]$ of Laurent polynomial maps into $\mathfrak{g}$, with the pointwise bracket.
Over $\C$, its elements can be seen as maps from the circle $\abs{t} = 1$ to $\mathfrak{g}$ with finite Fourier series.
It is the infinitesimal version of a loop group.
Adding a one-dimensional center and a derivation to it gives the untwisted [[affine Lie algebras|9A6RGRV056]].

## Explanations

### L1 human

A loop in $\mathfrak{g}$ is a closed path in $\mathfrak{g}$, parametrized by a point $t$ on the unit circle.
The loop algebra keeps those loops that are finite sums $\sum_m x_m t^m$ with $x_m \in \mathfrak{g}$ and $m \in \Z$.
Two loops are bracketed point by point, which on these sums means $[x t^m, y t^n] = [x, y] t^{m+n}$.
For example, if $\mathfrak{g}$ is abelian, then all brackets vanish and the loop algebra is abelian too.
