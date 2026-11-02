---
tag: MWDB7RACWQ
kind: example
name: Real projective plane
msc: [51N15, 51A05]
instance_of: [DANFNN8C4Y]
uses: [FS9FRJ17D2, 1DDYB6VVSR, 04AJE0M271, RNDDWDAFJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Real_projective_plane
same_as:
  wikidata: Q633815
  wikipedia: Real projective plane
---

## Example

The *real projective plane* $\mathbb{RP}^2$ is the set of 1-dimensional linear subspaces of $\R^3$.
A point is written in [[homogeneous coordinates|FS9FRJ17D2]] $[x : y : z]$ with $(x, y, z) \ne (0, 0, 0)$, where $[x : y : z] = [\lambda x : \lambda y : \lambda z]$ for every $\lambda \ne 0$.
A line is the set of points of a 2-dimensional linear subspace of $\R^3$, that is a set $\set{[x : y : z] : ax + by + cz = 0}$ with $(a, b, c) \ne (0, 0, 0)$.

Check of the axioms of a [[projective plane|DANFNN8C4Y]]:

1. Two distinct points are two distinct lines through $0$ in $\R^3$; they span exactly one plane through $0$, so they lie on exactly one line.
2. Two distinct lines are two distinct planes through $0$; their intersection is exactly one line through $0$, so they meet in exactly one point.
3. The four points $[1 : 0 : 0]$, $[0 : 1 : 0]$, $[0 : 0 : 1]$, $[1 : 1 : 1]$ have no three on a line, since any three of the vectors are linearly independent.

## Remarks

The points with $z \ne 0$ form a copy of the plane $\R^2$ through $[x : y : z] \mapsto (x/z, y/z)$.
The points with $z = 0$ form the line at infinity; two parallel lines of $\R^2$ meet there, at the point given by their common direction.
As a topological space, $\mathbb{RP}^2$ is the sphere $S^2$ with antipodal points identified, a special case of [[real projective space|1DDYB6VVSR]].
It is a compact surface that is not orientable: it contains a [[Möbius strip|04AJE0M271]], and it is obtained by gluing a disc to the boundary circle of a Möbius strip.
Its [[Euler characteristic|RNDDWDAFJ5]] is $1$, and its fundamental group has order $2$.
Desargues's theorem holds in $\mathbb{RP}^2$, as in every projective plane over a field.

## Explanations

### L1 human

The real projective plane is the ordinary plane with one extra point added for each direction, where parallel lines going that way meet.
These extra points form one more line, the line at infinity.
With them, any two lines meet in exactly one point, with no exceptions for parallels.
A picture of it: the set of lines through your eye, each line being one point of the projective plane.
As a surface it is strange: it cannot be built in ordinary space without crossing itself, and it has only one side.
