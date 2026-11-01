---
tag: QQ8GW1ASZM
kind: object
name: Fano plane
msc: ["51E15", 05B05]
instance_of: [2HWB7P1DZN, 7BPSC4T4M3]
sources:
  - url: https://en.wikipedia.org/wiki/Fano_plane
same_as:
  wikidata: Q1395814
  wikipedia: Fano plane
---

## Description

The Fano plane has the $7$ points $1, 2, \dots, 7$ and the $7$ lines
$$\set{1,2,3},\ \set{1,4,5},\ \set{1,6,7},\ \set{2,4,6},\ \set{2,5,7},\ \set{3,4,7},\ \set{3,5,6}.$$
Check: each line has $3$ points, so the lines cover $7 \cdot 3 = 21$ pairs of points.
These $21$ pairs are distinct, and there are $\binom{7}{2} = 21$ pairs in all, so every two points lie on exactly one line.
Every two lines meet in exactly one point, as one sees from the list.
So the Fano plane is a [[finite projective plane|2HWB7P1DZN]] of order $2$ and a [[Steiner system|7BPSC4T4M3]] $S(2, 3, 7)$.

## Remarks

Write each point $i$ in binary as a nonzero vector of $\F_2^3$.
Then the lines are the sets $\set{a, b, a + b}$ with $a \ne b$, for example $1 + 6 = 7$ in binary addition.
So the Fano plane is $PG(2, 2)$, the projective plane over the field with two elements.
Its automorphism group is $GL(3, 2)$, a simple group of order $168$.
It is the smallest projective plane.

## Explanations

### L1 human

The Fano plane is a tiny geometry with $7$ points and $7$ lines, each line with $3$ points.
It is usually drawn as a triangle with its three medians and its inscribed circle; the circle counts as a line.
Any two points share one line and any two lines share one point.
