---
tag: PX7SS1X16K
kind: problem
name: Happy ending problem
msc: [52C10, 05D10]
uses: [02AS45T3H9, 00TQV3F5S4]
about: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Happy_ending_problem
same_as:
  wikidata: Q1033772
  wikipedia: Happy ending problem
history:
  posed_by: "Esther Klein"
  first_stated: "1933"
---

## Problem

A finite set of points in the plane is in general position if no three of its points lie on a line.
For an integer $n \ge 3$, let $N(n)$ be the least integer $N$ with the following property.
Every set of $N$ points in the plane in general position contains $n$ points that are the vertices of a [[convex|02AS45T3H9]] polygon.
The problem asks for the value of $N(n)$.
Erdős and Szekeres conjectured that $N(n) = 2^{n-2} + 1$ for every $n \ge 3$.

## Remarks

Erdős and Szekeres proved that $N(n)$ exists, using [[Ramsey's theorem|00TQV3F5S4]] in one of their proofs.
They also proved the lower bound $N(n) \ge 2^{n-2} + 1$ by a construction.
The known values are $N(3) = 3$, $N(4) = 5$, $N(5) = 9$ and $N(6) = 17$, all equal to $2^{n-2} + 1$.
The value $N(6) = 17$ was established with a computer search by Szekeres and Peters.
Suk proved in 2017 that $N(n) \le 2^{n + o(n)}$.
The conjecture $N(n) = 2^{n-2} + 1$ is open for $n \ge 7$.

## History

The case $n = 4$ was posed by Esther Klein.
The name comes from the marriage of Klein and George Szekeres, who met through this problem.

## Explanations

### L1 human

Put five points on a sheet of paper so that no three are on one straight line.
Then four of them always form a convex quadrilateral, a shape with no dent.
The problem asks how many points you need to be sure of finding a convex shape with $n$ corners.
The guess is $2^{n-2} + 1$ points, and it is proved only for small $n$.
