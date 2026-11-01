---
tag: S4SV3QZ8B1
kind: concept
name: Hecke operator
msc: [11F25, 11F11]
sources:
  - url: https://en.wikipedia.org/wiki/Hecke_operator
same_as:
  wikidata: Q1592959
  wikipedia: Hecke operator
---

## Summary

The Hecke operators $T_n$, for $n \ge 1$, are linear maps on the space $M_k$ of [[modular forms|GWKN5VG78A]] of weight $k$.
They average a modular form over the sublattices of index $n$ of a lattice.
They commute with each other and preserve the [[cusp forms|A50Y012RBP]].
A common eigenform of all $T_n$, suitably normalized, has multiplicative Fourier coefficients and an L-function with an Euler product.

## Explanations

### L1 human

A modular form can be seen as a function of lattices in the plane.
The operator $T_n$ replaces the value at a lattice by the sum of the values at all its sublattices of index $n$.
This produces a new modular form of the same weight.
Since the space of forms is small, a form is often sent to a multiple of itself.
For $\Delta$ of weight $12$, $T_n \Delta = \tau(n) \Delta$, which explains why the [[Ramanujan tau function|6DNZAGCSQS]] is multiplicative.
