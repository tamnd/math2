---
tag: BZ2MM3CTNA
kind: statement
role: theorem
name: Cayley–Bacharach theorem
msc: [14H50, 14C17]
uses: [EWS4WFTA7W, ZT9A6JK8QF, 2C3PAQ7H50, KWNVF194D8]
about: [EWS4WFTA7W]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Bacharach_theorem
same_as:
  wikidata: Q4455043
  wikipedia: Cayley–Bacharach theorem
---

## Statement

Let $k$ be an algebraically closed field, and let $\mathbb{P}^2$ be the [[projective plane|ZT9A6JK8QF]] over $k$.
Let $C_1$ and $C_2$ be [[plane curves|EWS4WFTA7W]] of degrees $d$ and $e$, defined by [[homogeneous polynomials|2C3PAQ7H50]] with no common factor.
Assume that $C_1$ and $C_2$ meet in exactly $de$ distinct points.
Then every plane curve of degree $d + e - 3$ that passes through all but one of these $de$ points also passes through the remaining point.

## Remarks

The most quoted case is $d = e = 3$: if two plane cubics meet in nine distinct points, then every cubic through eight of them passes through the ninth.
For this case, the cubics through the eight points form a vector space of dimension $10 - 8 = 2$, because the eight points impose independent conditions on cubics.
The defining polynomials $F_1, F_2$ of $C_1, C_2$ are independent and lie in this space, so every cubic through the eight points is $\lambda F_1 + \mu F_2$ and vanishes at the ninth point.
The general case is usually proved with duality on the zero-dimensional complete intersection $C_1 \cap C_2$.
By [[Bézout's theorem|KWNVF194D8]], two curves of degrees $d$ and $e$ without common component meet in $de$ points counted with multiplicity, so the hypothesis says that all intersections are transverse.
The cubic case gives a proof of the associativity of the group law on an elliptic curve, and of Pascal's theorem on six points of a conic.

## Explanations

### L1 human

Two curves in the plane cross in a predictable number of points, for two cubics nine.
The theorem says that these points are not independent of each other.
A curve of the right degree that goes through all of them but one is forced to go through the last one as well.
For cubics, eight of the nine points already decide the ninth.

### L2 human

The theorem says that the intersection points fail to impose independent conditions on curves of degree $d + e - 3$.
This is the degree that appears in the adjunction formula for the canonical divisor of a plane curve.
It is the source of many classical incidence theorems, such as Pappus's and Pascal's theorems, which come from degenerate cubics made of lines and conics.
In modern language it is a consequence of duality for the complete intersection $C_1 \cap C_2$.
