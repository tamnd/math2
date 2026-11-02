---
tag: P9PYM71GMM
kind: example
name: Hypercube
msc: [52B12, 52B11, 51M20]
instance_of: [300K6CB1KH, 7E6FXTGH2Y]
uses: [DPDXN2FJC4, R7V3S9V891, 872BAKDQQK]
sources:
  - url: https://en.wikipedia.org/wiki/Hypercube
same_as:
  wikidata: Q213723
  wikipedia: Hypercube
---

## Example

For $d \ge 1$, the $d$-dimensional *hypercube* is
$$C_d = [0,1]^d = \set{x \in \R^d : 0 \le x_i \le 1 \text{ for } i = 1, \dots, d}.$$
It is a [[convex polytope|300K6CB1KH]]: it is the convex hull of the $2^d$ points with all coordinates in $\set{0, 1}$, and these are its [[vertices|R7V3S9V891]].
Its [[facets|DPDXN2FJC4]] are the $2d$ sets where one coordinate is fixed to $0$ or to $1$.

A face of $C_d$ is obtained by fixing some coordinates to $0$ or $1$ and leaving the others free.
A $k$-dimensional face leaves $k$ coordinates free, so the number of $k$-faces is
$$f_k(C_d) = 2^{d-k} \binom{d}{k}.$$
For $d = 3$ this gives the [[f-vector|872BAKDQQK]] $(8, 12, 6)$ of the ordinary cube.

$C_d$ is a [[simple polytope|7E6FXTGH2Y]].
At a vertex $v$ the edges change exactly one coordinate of $v$, and there are $d$ coordinates, so every vertex lies in $d$ edges.

## Remarks

The graph of $C_d$ is the hypercube graph: its vertices are the $0/1$ strings of length $d$, joined when they differ in one place.
Many authors use $[-1, 1]^d$ instead; it has the same combinatorics and is centrally symmetric about $0$.
For $d = 4$ the hypercube is also called the tesseract, with $f$-vector $(16, 32, 24, 8)$.

## Explanations

### L1 human

The hypercube is the cube in any dimension.
A segment is a $1$-cube, a square is a $2$-cube and the ordinary cube is a $3$-cube.
To get the next one, slide the previous cube one unit in a new direction and fill in the space it sweeps out.
Each step doubles the number of corners, so the $d$-cube has $2^d$ corners.
