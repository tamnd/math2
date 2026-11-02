---
tag: JJQEGRK2DG
kind: concept
name: Scorer's function
msc: [33C10, 34B30]
sources:
  - url: https://en.wikipedia.org/wiki/Scorer%27s_function
same_as:
  wikidata: Q1092942
  wikipedia: Scorer's function
---

## Summary

Scorer's functions $\operatorname{Gi}$ and $\operatorname{Hi}$ are particular solutions of the inhomogeneous Airy equations $y'' - x y = \mp\frac{1}{\pi}$.
They are built from the same integrals as the [[Airy functions|1N5D4PN92W]], split into two pieces.
Their sum is the Airy function $\operatorname{Bi}$.
They appear when a turning-point problem has a constant forcing term.

## Explanations

### L1 human

The Airy function $\operatorname{Bi}$ is an integral of a sum of two terms, one exponential and one oscillating.
Taking each term alone gives Scorer's two functions, $\operatorname{Hi}$ and $\operatorname{Gi}$.
Each piece alone no longer solves the Airy equation, but it solves it up to a constant.
For example, $\operatorname{Hi}(0) = \frac{1}{\pi} \int_0^\infty e^{-t^3/3}\, dt$, a positive number.
