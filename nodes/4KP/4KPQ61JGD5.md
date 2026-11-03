---
tag: 4KPQ61JGD5
kind: concept
name: Boundary element method
msc: [65N38, 74S15]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_element_method
same_as:
  wikidata: Q1935004
  wikipedia: Boundary element method
---

## Summary

The boundary element method solves a linear partial differential equation by discretising an integral equation posed only on the boundary of the domain.
It uses a [[fundamental solution|K2NK9A8M5F]] of the equation to express the solution inside through its values and normal derivatives on the boundary.
Only the boundary is meshed, which lowers the dimension of the problem by one and suits unbounded domains, but the resulting matrices are dense.
In elasticity its starting point is the [[Somigliana identity|Q8YMDSV27Y]].

## Explanations

### L1 human

For many equations, knowing what happens on the boundary of a region is enough to know everything inside.
The boundary element method uses this: it computes only the unknown boundary values, and then gets inside values by a formula.
So a three-dimensional body needs only a mesh of its two-dimensional surface.
For example, the field around a cavity in an infinite elastic solid needs a mesh of the cavity surface only, not of the infinite solid around it.
