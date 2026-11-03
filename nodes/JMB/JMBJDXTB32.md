---
tag: JMBJDXTB32
kind: definition
name: Flexibility method
msc: [74K10, 74S99]
defines: 8CS7BCP7XS
uses: [SKVPKD5VZN]
sources:
  - url: https://en.wikipedia.org/wiki/Flexibility_method
---

## Definition

Consider a linear elastic [[statically indeterminate structure|SKVPKD5VZN]] of degree $n$ under given loads.
The *flexibility method* consists of the following steps.

1. Release: choose $n$ redundant forces $X_1, \ldots, X_n$ (support reactions or internal forces) such that removing the corresponding constraints leaves a statically determinate and stable primary structure.
2. Load displacements: compute, on the primary structure under the given loads, the displacement $\Delta_{i0}$ at each released constraint $i$, measured in the direction of $X_i$.
3. Flexibility coefficients: compute $f_{ij}$, the displacement at constraint $i$ of the primary structure due to a unit force $X_j = 1$ alone.
   The matrix $f = (f_{ij})$ is the flexibility matrix.
4. Compatibility: solve
$$\Delta_{i0} + \sum_{j=1}^{n} f_{ij} X_j = \Delta_i, \qquad i = 1, \ldots, n,$$
where $\Delta_i$ is the prescribed displacement at constraint $i$, usually $0$.

All other forces and displacements then follow by superposition on the primary structure.

## Remarks

Example: a beam of length $L$ and bending stiffness $EI$, clamped at $A$, propped at $B$, with uniform load $w$ per unit length.
Take the prop reaction $R$ at $B$ as the redundant, so the primary structure is a cantilever.
The load gives downward tip deflection $wL^4/(8EI)$.
A unit upward force at $B$ gives upward tip deflection $L^3/(3EI)$.
Compatibility $-wL^4/(8EI) + R L^3/(3EI) = 0$ gives $R = 3wL/8$.

Non-example: a straight beam on three supports, a pin at one end and two rollers, is indeterminate of degree $1$.
Taking the horizontal reaction of the pin as the redundant is not an allowed release.
The primary structure could then slide horizontally, and clause 1 requires a stable primary structure.

By Maxwell's reciprocal theorem the flexibility matrix is symmetric, $f_{ij} = f_{ji}$, and it is positive definite.
