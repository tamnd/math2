---
tag: D5XH66A8RP
kind: concept
name: Differential graded Lie algebra
msc: [17B70, 17B55, 55P62]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_graded_Lie_algebra
same_as:
  wikidata: Q15241040
  wikipedia: Differential graded Lie algebra
---

## Summary

A differential graded Lie algebra is a [[chain complex|WQ82C0M3QB]] whose terms carry a graded Lie bracket.
The differential is a derivation of the bracket.
It is the Lie analogue of a [[differential graded algebra|GQVAXW5X09]].
In [[deformation theory|SWFR1GD6QT]] over a field of characteristic zero, many deformation problems are controlled by a differential graded Lie algebra, through its Maurer–Cartan equation $d a + \frac{1}{2}[a, a] = 0$.
Differential graded Lie algebras also model rational homotopy types, following Quillen.

## Explanations

### L1 human

Start with a [[Lie algebra|5JJYBJ6A8K]], and spread it over several degrees $\ldots, L^{-1}, L^0, L^1, \ldots$.
The bracket of an element of degree $i$ with one of degree $j$ has degree $i + j$, and its symmetry rules carry signs that depend on the degrees.
Add a map $d$ that raises the degree by one, satisfies $d \circ d = 0$, and obeys a product rule for the bracket.
A small example is the space of differential forms with values in a matrix Lie algebra, with the exterior derivative as $d$.
The cohomology of a differential graded Lie algebra is again a graded Lie algebra.
