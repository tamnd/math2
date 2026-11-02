---
tag: XA35DT40XS
kind: problem
name: Hilbert's fourth problem
msc: [51F99, 53C60, 51K05]
uses: [0VKD1TP7F3, 0MP9BCF6DP, NSYMQMHPDN]
about: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_fourth_problem
same_as:
  wikidata: Q4515035
  wikipedia: Hilbert's fourth problem
history:
  posed_by: "David Hilbert"
  first_stated: "1900"
---

## Problem

Let $U$ be an open convex subset of $\R^n$.
Determine all [[metrics|0VKD1TP7F3]] $d$ on $U$ for which every straight [[line|0MP9BCF6DP]] segment in $U$ is a shortest path.
That is, determine all $d$ such that $d(x, z) = d(x, y) + d(y, z)$ whenever $y$ lies on the segment from $x$ to $z$.

## Remarks

Such metrics are called projective metrics, and their [[geodesics|NSYMQMHPDN]] include the straight lines.
Examples are the Euclidean metric and the metrics given by any norm on $\R^n$.
Another example is the Hilbert metric on a bounded convex domain; when the domain is a disc, it gives the Beltrami–Klein model of the hyperbolic plane.
Hilbert posed the question in his list of problems of 1900.
Herbert Busemann gave a construction of such metrics from measures on the space of hyperplanes.
Aleksei Pogorelov proved that in the plane every continuous projective metric arises in this way.

## Explanations

### L1 human

In ordinary geometry the shortest way between two points is the straight line.
Hilbert asked which other ways of measuring distance keep this property.
There are many: for example, the taxicab distance $\abs{x_1 - y_1} + \abs{x_2 - y_2}$ in the plane also makes every straight segment a shortest path, although it is not the only shortest path.
