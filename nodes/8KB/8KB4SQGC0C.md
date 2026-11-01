---
tag: 8KB4SQGC0C
kind: concept
name: Graded ring
msc: [13A02]
specializes: [0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_ring
same_as:
  wikidata: Q15534632
  wikipedia: Graded ring
---

## Summary

A graded ring is a [[ring|0B1261B5ED]] that splits as a direct sum of pieces $R_0, R_1, R_2, \dots$.
The product of an element of $R_m$ and an element of $R_n$ must lie in $R_{m+n}$.
The main example is a polynomial ring, split by degree.
Graded rings are the algebraic side of projective geometry, and they appear in commutative algebra through [[associated graded rings|8HFAEGFQT1]] and [[Rees algebras|W8ZAH8TTHS]].

## Explanations

### L1 human

In a polynomial ring every polynomial is a sum of homogeneous parts, one for each degree.
Multiplying two homogeneous parts adds their degrees.
A graded ring is any ring with this kind of bookkeeping by degree.
For example, $x^2 + 3xy + 5$ in $k[x, y]$ has a part $x^2 + 3xy$ of degree $2$ and a part $5$ of degree $0$.
The [[definition|CAPQBQDRA7]] makes this precise.
