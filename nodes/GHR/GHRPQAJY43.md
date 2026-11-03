---
tag: GHRPQAJY43
kind: concept
name: Vertex operator algebra
msc: [17B69, 81T40]
sources:
  - url: https://en.wikipedia.org/wiki/Vertex_operator_algebra
same_as:
  wikidata: Q28509
  wikipedia: Vertex operator algebra
---

## Summary

A vertex operator algebra is a graded vector space $V$ in which every vector $v$ gives a formal series $Y(v, z)$ of operators on $V$.
These series satisfy a Jacobi identity, and $V$ carries an action of the [[Virasoro algebra|R9WFXME6GC]].
It is the algebraic form of the chiral part of a two-dimensional conformal field theory.
Examples come from affine Lie algebras, from the Virasoro algebra itself and from even lattices.
The moonshine module, a vertex operator algebra with the Monster group as automorphism group, was the key to the proof of monstrous moonshine.

## Explanations

### L1 human

In an ordinary algebra, two elements multiply to give one element.
In a vertex operator algebra, two elements $u, v$ multiply to give a whole formal series $Y(u, z) v = \sum_n u_n v\, z^{-n-1}$, one product $u_n v$ for each integer $n$.
One can think of $z$ as the position of $u$ on a punctured plane, with $v$ at the origin, and of the series as the result of bringing them together.
These infinitely many products obey a single rule, the Jacobi identity, which generalizes both commutativity and associativity.
A conformal vector $\omega$ adds an action of the Virasoro algebra, which encodes the symmetries of the plane under conformal maps.
