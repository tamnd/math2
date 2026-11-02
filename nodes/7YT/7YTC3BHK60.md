---
tag: 7YTC3BHK60
kind: concept
name: Tropical geometry
msc: [14T10, 14T15, 14T20]
sources:
  - url: https://en.wikipedia.org/wiki/Tropical_geometry
same_as:
  wikidata: Q2982669
  wikipedia: Tropical geometry
---

## Summary

Tropical geometry studies polynomials over the tropical semiring, where addition is replaced by minimum (or maximum) and multiplication by ordinary addition, see [[max-plus algebra|64G0VSC5F4]].
Tropical polynomials are piecewise linear functions, and their zero sets, the [[tropical varieties|FT2GJEHWY5]], are polyhedral complexes.
Through a [[valuation|B85T5VKR3M]], an algebraic variety degenerates to a tropical variety that keeps much of its combinatorial information, such as degrees and intersection numbers.
This makes problems of [[enumerative geometry|ZPZA1FKZZC]] and of [[toric varieties|YWB981MEF2]] accessible to combinatorics.

## Explanations

### L1 human

In tropical arithmetic, $3 \oplus 5 = \min(3, 5) = 3$ and $3 \odot 5 = 3 + 5 = 8$.
A polynomial in this arithmetic becomes a minimum of finitely many linear functions, whose graph is made of flat pieces.
The tropical curve of such a polynomial is the set of corners, where the minimum is attained twice.
A tropical line in the plane, for example, is a point with three rays coming out of it.
These piecewise linear pictures are shadows of ordinary curves, and counting them can answer classical questions such as how many curves pass through given points.
