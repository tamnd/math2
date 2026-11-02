---
tag: 9WD2TZ4ZB5
kind: problem
name: Tammes problem
msc: [52C17, 05B40]
uses: [SDCX4WDP4F]
about: [SDCX4WDP4F]
sources:
  - url: https://en.wikipedia.org/wiki/Tammes_problem
same_as:
  wikidata: Q3406239
  wikipedia: Tammes problem
history:
  posed_by: "Pieter Merkus Lambertus Tammes"
  first_stated: "1930"
---

## Problem

Let $N \ge 2$ be an integer and let $S^2 \subset \R^3$ be the unit sphere.
Find the largest number $d_N$ such that there are $N$ points on $S^2$ with pairwise distances at least $d_N$.
Find also the configurations of $N$ points that attain it.

## Remarks

Equivalently, find the largest radius of $N$ equal non-overlapping circular caps on a sphere, or the best [[spherical code|SDCX4WDP4F]] of size $N$ in $\R^3$.
The botanist Tammes posed it in 1930 while studying the distribution of pores on pollen grains.
For $N = 4$, $6$ and $12$ the answers are the vertices of the regular tetrahedron, octahedron and icosahedron.
The problem is solved for $N \le 14$ and for $N = 24$.
Oleg Musin and Alexey Tarasov solved the case $N = 13$.
It is linked with the [[kissing number problem in three dimensions|Q1H6BCKTBE]]: thirteen unit balls cannot touch a central one, so the optimal angle for $13$ points is below $60^\circ$.

## Explanations

### L1 human

How should $N$ people stand on a round planet so that the two closest people are as far apart as possible?
For small $N$ the answer is often a familiar solid, such as the corners of a tetrahedron for four people.
For most $N$ the answer is unknown, and even small cases needed long proofs.
