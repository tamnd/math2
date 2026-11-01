---
tag: HE8F7KBF42
kind: concept
name: Abel–Jacobi map
msc: [14H40, 30F30]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%E2%80%93Jacobi_map
same_as:
  wikidata: Q4666729
  wikipedia: Abel–Jacobi map
---

## Summary

The Abel–Jacobi map sends a point of a compact [[Riemann surface|5K0N8QMV6Q]] of genus $g \ge 1$ to its Jacobian variety, a complex torus of dimension $g$.
It is defined by integrating a basis of holomorphic [[Abelian differentials|P014C13K5H]] from a fixed base point.
Abel's theorem says that it detects which divisors of degree $0$ are divisors of meromorphic functions.
It is the basic bridge between a curve and its Jacobian.

## Explanations

### L1 human

Pick a base point on the surface and a point $P$, and integrate the $g$ holomorphic differentials along a path from the base point to $P$.
This gives $g$ complex numbers, but they depend on the path.
Two paths differ by a loop, and the integrals over loops form a lattice, so the answer is well defined modulo that lattice.
For a torus $\C / \Lambda$ with the differential $dz$, the map is just $P \mapsto P - P_0$, so the torus is its own Jacobian.
