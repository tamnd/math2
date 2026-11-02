---
tag: EPWB2JEXPE
kind: problem
name: Unit distance problem
msc: [52C10, 05C62]
uses: [0XW7V9ZZ05, 0NPPGHQNXQ, 0RYTGBJAGN, 34B1PW5EE2]
about: [0XW7V9ZZ05]
sources:
  - url: https://en.wikipedia.org/wiki/Unit_distance_graph
history:
  posed_by: "Paul Erdős"
  first_stated: "1946"
---

## Problem

Let $n \ge 2$, and let $\norm{p - q}$ be the [[Euclidean distance|0NPPGHQNXQ]] in the [[Euclidean plane|0XW7V9ZZ05]].
Let $u(n)$ be the largest number of pairs $\set{p, q}$ with $\norm{p - q} = 1$ in a set of $n$ points of the plane.
Determine the order of growth of $u(n)$ as $n \to \infty$.

## Remarks

Paul Erdős posed the problem in 1946.
In the same paper he showed $u(n) = O(n^{3/2})$, and, using a suitably scaled square grid, $u(n) \ge n^{1 + c/\log \log n}$ for a constant $c > 0$; here $O$ is [[big O notation|0RYTGBJAGN]].
Joel Spencer, Endre Szemerédi and William Trotter proved $u(n) = O(n^{4/3})$ in 1984.
A short proof of this bound by László Székely uses the [[crossing number inequality|34B1PW5EE2]].
The exact order of growth is still not known.
The pairs at distance $1$ form the edges of a unit distance graph on the $n$ points.

## Explanations

### L1 human

Place $n$ points in the plane and count the pairs that are exactly one unit apart.
How large can this count be?
A square grid of the right size does a little better than $n$, and nobody has done much better.
The best upper bound is about $n^{4/3}$, and closing the gap is a famous open question of Erdős.
