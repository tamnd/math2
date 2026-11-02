---
tag: N8X7XJBKT0
kind: concept
name: Hopf module
msc: [16T05]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Summary

A Hopf module over a [[Hopf algebra|7XFYP0N84H]] $H$ is a vector space that is both an $H$-[[module|0NZ8JA25WK]] and an $H$-[[comodule|7WEM2E6RTV]].
The coaction must be compatible with the action.
The fundamental theorem of Hopf modules, due to Larson and Sweedler, says that every Hopf module is free.
It has the form $V \otimes H$, where $V$ is its space of coinvariants.
This theorem is the main tool behind the uniqueness of [[integrals|RJA5026RGX]] and the Frobenius property of finite-dimensional Hopf algebras.

## Explanations

### L1 human

The Hopf algebra $H$ itself can be multiplied by elements of $H$ and also split by its comultiplication, and the two operations fit together.
A Hopf module is any vector space with these two structures fitting together in the same way.
The simplest examples are copies of $H$ with a multiplicity space attached, $V \otimes H$.
The surprising theorem is that there are no others: every Hopf module looks like $V \otimes H$.
