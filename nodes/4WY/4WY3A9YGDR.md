---
tag: 4WY3A9YGDR
kind: concept
name: Kuranishi structure
msc: [53D45, 58D27, 57R18]
sources:
  - url: https://en.wikipedia.org/wiki/Kuranishi_structure
same_as:
  wikidata: Q25304228
  wikipedia: Kuranishi structure
---

## Summary

A Kuranishi structure on a compact space describes it locally as a quotient by a finite group.
The thing divided is the zero set of a smooth section of a vector bundle.
The bundle has finite rank and lives over a finite-dimensional manifold.

The local descriptions, called Kuranishi charts, are glued by coordinate changes that embed one chart into another.
The notion was introduced by Fukaya and Ono to handle moduli spaces of pseudoholomorphic curves, which are usually singular and of the wrong dimension.
A Kuranishi structure with an orientation has a [[virtual fundamental class|5VXYQ4BXRB]], which is used to define [[Gromov–Witten invariants|XVJA0JD79P]] and Floer homology in general symplectic manifolds.

## Explanations

### L1 human

Many moduli spaces are cut out by equations that, near each solution, reduce to finitely many equations in finitely many unknowns.
A Kuranishi chart records exactly this: a smooth space of unknowns, a finite list of equations, and a finite symmetry group.
The solutions may form a singular set, but the chart still knows the expected dimension, the number of unknowns minus the number of equations.
For example, the zero set of $s(x, y) = x y$ on $\R^2$, a pair of crossing lines, is described by one chart with $V = \R^2$, $E = \R$ and expected dimension $1$.
