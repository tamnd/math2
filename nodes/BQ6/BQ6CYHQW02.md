---
tag: BQ6CYHQW02
kind: concept
name: Regularity structures
msc: [60L30, 60H17, 35R60]
sources:
  - url: https://en.wikipedia.org/wiki/Regularity_structure
same_as:
  wikidata: Q28401890
  wikipedia: Regularity structure
---

## Summary

A regularity structure is an algebraic framework, introduced by Martin Hairer, for describing functions and distributions locally by generalized Taylor expansions.
The building blocks are abstract symbols with assigned degrees of regularity, together with a group that says how to re-expand them around another point.
The theory gives a solution theory for singular [[stochastic partial differential equations|PRCQG82QTK]], whose nonlinear terms are not defined classically.
Examples include the [[Kardar–Parisi–Zhang equation|RQ196EHXKC]] and the dynamical $\Phi^4_3$ model.

## Explanations

### L1 human

A smooth function is described near a point by its Taylor polynomial, built from the monomials $1, x, x^2, \ldots$.
Solutions of rough random equations have no Taylor polynomial, because they are not differentiable.
The idea is to add new building blocks, made from the noise itself, and to expand the solution in terms of them.
Each block gets a degree, which may be negative or fractional, saying how it behaves at small scales.
A rule for moving the base point, like re-expanding $(x - a)^2$ around another point $b$, completes the structure.
