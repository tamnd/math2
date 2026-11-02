---
tag: 58WSWYBCWA
kind: example
name: Complex projective plane
msc: [51N15, 14N05, 32Q15]
instance_of: [DANFNN8C4Y]
uses: [FS9FRJ17D2, ZT9A6JK8QF, 0J78KBPFZB, RNDDWDAFJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_projective_plane
same_as:
  wikidata: Q4426755
  wikipedia: Complex projective plane
---

## Example

The *complex projective plane* $\mathbb{CP}^2$ is the set of 1-dimensional complex linear subspaces of $\C^3$, the [[projective space|ZT9A6JK8QF]] of dimension $2$ over $\C$.
A point is written in [[homogeneous coordinates|FS9FRJ17D2]] $[z_0 : z_1 : z_2]$ with $(z_0, z_1, z_2) \ne 0$, up to multiplication by a nonzero complex number.
A line is the set $\set{[z_0 : z_1 : z_2] : a_0 z_0 + a_1 z_1 + a_2 z_2 = 0}$ for some $(a_0, a_1, a_2) \in \C^3 \setminus \set{0}$.

Check that it is a [[projective plane|DANFNN8C4Y]]: the arguments for the real case work over any field.
Two distinct points span a unique 2-dimensional subspace of $\C^3$, so they lie on a unique line.
Two distinct 2-dimensional subspaces of $\C^3$ meet in a 1-dimensional subspace, so two distinct lines meet in a unique point.
The points $[1 : 0 : 0]$, $[0 : 1 : 0]$, $[0 : 0 : 1]$, $[1 : 1 : 1]$ have no three on a line.

## Remarks

Each line is a copy of $\mathbb{CP}^1$, which is the [[Riemann sphere|0J78KBPFZB]].
So, as a real manifold, $\mathbb{CP}^2$ is a compact simply connected manifold of real dimension $4$ that contains many 2-spheres meeting in single points.
It is a compact complex manifold of complex dimension $2$, and with the Fubini–Study metric it is a Kähler manifold.
Its integral cohomology is $\Z$ in degrees $0$, $2$, $4$ and zero otherwise, so its [[Euler characteristic|RNDDWDAFJ5]] is $3$.
Plane algebraic curves over $\C$ live naturally in $\mathbb{CP}^2$, and there Bézout's theorem holds without exceptions.
Two curves of degrees $d$ and $e$ with no common component meet in exactly $de$ points, counted with multiplicity.

## Explanations

### L1 human

The complex projective plane is built like the real one, but with complex numbers as coordinates.
Each point is a line through the origin in $\C^3$, and parallel lines of $\C^2$ are made to meet at infinity.
Every line in it is a sphere, so the plane is a four-dimensional space woven out of spheres, any two of which cross at exactly one point.
It is the natural home of plane algebraic curves: there, a line and a circle always meet in exactly two points, counted correctly.
