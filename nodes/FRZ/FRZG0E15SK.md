---
tag: FRZG0E15SK
kind: concept
name: Essential spectrum
msc: [47A53, 47A10]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_spectrum
same_as:
  wikidata: Q917390
  wikipedia: Essential spectrum
---

## Summary

The essential spectrum of a bounded operator is the part of its spectrum that does not change under compact perturbations.
It consists of the $\lambda$ for which $T - \lambda I$ is not a Fredholm operator.
For a self-adjoint operator on a Hilbert space, it is what remains of the spectrum after removing the isolated eigenvalues of finite multiplicity.

## Explanations

### L1 human

Some points of the spectrum are fragile: an isolated eigenvalue with a finite-dimensional eigenspace can be moved or removed by adding an operator of finite rank.
Other points are robust, because they involve infinitely many directions at once.
The essential spectrum collects the robust points.
For example, every compact operator on an infinite-dimensional space has essential spectrum $\set{0}$, and the identity has essential spectrum $\set{1}$.
