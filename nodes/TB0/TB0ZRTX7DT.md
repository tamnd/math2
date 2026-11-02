---
tag: TB0ZRTX7DT
kind: example
name: Möbius–Kantor configuration
msc: [05B30, 51A20, "51E30"]
instance_of: [Q2QFXPP9EE]
uses: [Q2QFXPP9EE, S2NAGK9YHF]
sources:
  - url: https://en.wikipedia.org/wiki/M%C3%B6bius%E2%80%93Kantor_configuration
same_as:
  wikidata: Q6950325
  wikipedia: Möbius–Kantor configuration
---

## Example

The *Möbius–Kantor configuration* is the [[configuration|Q2QFXPP9EE]] $(8_3)$: $8$ points and $8$ lines, with $3$ points on each line and $3$ lines through each point.
Up to isomorphism there is only one $(8_3)$ configuration.
A model has the points $0, 1, \dots, 7$ in $\Z/8\Z$ and the lines $\set{i, i + 1, i + 3}$ for $i \in \Z/8\Z$.

Check: each point $j$ lies on the three lines with $i = j$, $i = j - 1$ and $i = j - 3$.
The differences of elements of $\set{0, 1, 3}$ are $\pm 1, \pm 2, \pm 3$, each obtained once and all distinct modulo $8$.
So two points whose difference is one of these lie on exactly one common line, and two points with difference $4$ lie on none.

Another model: delete one point from the [[affine plane of order $3$|S2NAGK9YHF]], together with the $4$ lines through it.
The remaining $8$ points and $8$ lines have $3$ points on each line, and each point lies on $4 - 1 = 3$ of the remaining lines.

The configuration cannot be realized by points and lines of the real plane, but it can be realized in the complex projective plane.
Its incidence graph is the Möbius–Kantor graph.

## Explanations

### L1 human

Can you draw two quadrilaterals so that each vertex of one lies on a side of the other, and the other way round?
Möbius asked this, and the answer is no with real points and straight lines.
The combinatorial pattern still exists: $8$ points and $8$ lines, each line through $3$ points and each point on $3$ lines.
It can be drawn with complex coordinates, or in the finite plane over the field with $3$ elements.
