---
tag: G4C8V6K4VW
kind: statement
role: theorem
name: Erdős–Anning theorem
msc: [52C10, 51M04]
uses: [0XW7V9ZZ05, 0NPPGHQNXQ, 0AFNNTRTJE, 0WN5G117YC]
about: [0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Anning_theorem
same_as:
  wikidata: Q3526982
  wikipedia: Erdős–Anning theorem
---

## Statement

Let $S$ be an infinite set of points in the [[Euclidean plane|0XW7V9ZZ05]].
Assume that the [[Euclidean distance|0NPPGHQNXQ]] between any two points of $S$ is an integer.
Then all points of $S$ lie on one line.

## Remarks

Suppose that $S$ contains three points $A, B, C$ that are not [[collinear|0AFNNTRTJE]].
For any other point $X$ of $S$, the triangle inequality gives $\abs{\,\norm{X - A} - \norm{X - B}\,} \le \norm{A - B}$, and this difference is an integer.
So $X$ lies on one of finitely many [[hyperbolas|0WN5G117YC]] with foci $A$ and $B$, counting degenerate ones such as the perpendicular bisector and parts of the line $AB$.
In the same way $X$ lies on one of finitely many hyperbolas with foci $A$ and $C$, and two such curves with different foci meet in at most $4$ points.
So $S$ is finite, a contradiction.
The hypothesis that $S$ is infinite is needed: the vertices of a $3$-$4$-$5$ right triangle are three non-collinear points with integer distances.
Integer distances cannot be weakened to rational ones: there are infinite non-collinear sets with all distances rational, for example dense subsets of a circle.

## Explanations

### L1 human

If infinitely many points in the plane have whole-number distances between every two of them, then they all sit on one straight line.
Off a line, integer distances are so restrictive that only finitely many points can fit.

### L2 human

Norman Anning and Paul Erdős proved the theorem in 1945.
The proof is a short argument with hyperbolas, using the definition of a hyperbola as the set of points with a fixed difference of distances to two foci.
In contrast, for every $n$ there are $n$ points in the plane, no three on a line, with all distances integers; one can take suitable points on a circle.
