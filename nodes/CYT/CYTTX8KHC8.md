---
tag: CYTTX8KHC8
kind: concept
name: Newton polytope
msc: [14M25, 52B20, 14T10]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_polytope
same_as:
  wikidata: Q99705926
  wikipedia: Newton polytope
---

## Summary

The Newton polytope of a polynomial in several variables is the [[convex hull|0FQSDC2EQ2]] of the exponent vectors of its monomials with nonzero coefficient.
It records which monomials can dominate, much as the [[Newton polygon|H7QNCE2QZJ]] of a polynomial over a valued field does in one variable.
The Newton polytope of a product is the Minkowski sum of the Newton polytopes of the factors.
Mixed volumes of Newton polytopes count the solutions of generic polynomial systems by the [[Bernstein–Kushnirenko theorem|VP32769PVR]].
Newton polytopes link polynomials with [[toric varieties|YWB981MEF2]] and [[tropical geometry|7YTC3BHK60]].

## Explanations

### L1 human

Write a polynomial in $x$ and $y$ and mark, for each term $c\,x^a y^b$ with $c \ne 0$, the point $(a, b)$ in the plane.
The smallest convex region containing all the marked points is the Newton polytope.
For $1 + x + y + xy$ it is the unit square, and for $1 + x^2 + y^3$ it is a triangle.
Its shape predicts much about the polynomial, for example how many common zeros two generic polynomials with these shapes have.
