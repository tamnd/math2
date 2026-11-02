---
tag: TS442VKWAG
kind: problem
name: No-three-in-line problem
msc: [52C10, 51M04]
uses: [0AFNNTRTJE, 0HGVCWQGY3]
about: [0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/No-three-in-line_problem
same_as:
  wikidata: Q6580594
  wikipedia: No-three-in-line problem
history:
  posed_by: "Henry Dudeney"
  first_stated: "1900"
---

## Problem

For an integer $n \ge 1$, consider the $n \times n$ grid $\set{1, \dots, n}^2$ of points in the plane.
Find the largest number of points of the grid that can be chosen so that no three chosen points are [[collinear|0AFNNTRTJE]].
In particular, decide for which $n$ this number equals $2n$.

## Remarks

Henry Dudeney posed the problem in 1900.
Each of the $n$ rows can contain at most $2$ chosen points, so by the [[pigeonhole principle|0HGVCWQGY3]] at most $2n$ points can be chosen.
The bound $2n$ is attained for all $n$ up to at least $46$, by solutions found with computer searches.
For a prime $p$, the $p$ points $(x, x^2 \bmod p)$ with $0 \le x < p$ have no three in a line, an observation of Erdős.
Indeed, three of them on a line would give three roots in the field $\F_p$ of a nonzero polynomial of degree at most $2$.
Hall, Jackson, Sudbery and Wild refined such constructions in 1975.
They showed that for every $\varepsilon > 0$ and all large $n$, at least $(3/2 - \varepsilon)n$ points can be chosen.
It is conjectured that for large $n$ the maximum is strictly less than $2n$.

## Explanations

### L1 human

On an $n$ by $n$ board of dots, choose as many dots as you can so that no three of your dots lie on a straight line, in any direction.
Two dots per row is the most you can hope for, which gives $2n$.
For small boards one can reach $2n$, but whether this works for all boards is unknown.
