---
tag: EMWW6PKFSG
kind: definition
name: Projective geometry
msc: [51A05, 51N15]
defines: N32Z68F0D3
uses: [FGKNAFNHA3, 0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_geometry
---

## Definition

A *projective geometry*, or projective space in the axiomatic sense, is an [[incidence structure|FGKNAFNHA3]] whose lines are sets of points, incidence being membership, such that:

1. Any two distinct points lie on exactly one line.
2. (Veblen's axiom) Let $a, b, c, d$ be distinct points; if the lines $ab$ and $cd$ meet, then the lines $ac$ and $bd$ meet.
3. Every line contains at least three points.

The subject *projective geometry* is the study of these spaces and of the properties preserved by their isomorphisms.

## Remarks

Example: let $V$ be a vector space of dimension at least $3$ over a field $k$.
The points of the [[projective space|ZT9A6JK8QF]] $\mathbb{P}(V)$, with the lines $\mathbb{P}(W)$ for $\dim W = 2$, form a projective geometry.
Check: two distinct points span a unique $2$-dimensional $W$.
If $ab$ and $cd$ meet, then $a, b, c, d$ lie in a subspace $U$ of dimension at most $3$.
The planes for $ac$ and $bd$ lie in $U$, so they meet in a nonzero vector.
A $2$-dimensional $W$ has $\abs{k} + 1 \ge 3$ points.

Non-example: the real [[affine plane|EC7XT2ZM5S]] $\R^2$ satisfies clauses 1 and 3 but fails Veblen's axiom.
Take $a = (0,0)$, $b = (1,0)$, $c = (0,1)$ and $d = (1,2)$.
The lines $ab$ (given by $y = 0$) and $cd$ (given by $y = x + 1$) meet at $(-1, 0)$, but the lines $ac$ (given by $x = 0$) and $bd$ (given by $x = 1$) are parallel.

A projective geometry of dimension $2$ is the same as a [[projective plane|DANFNN8C4Y]].
By the [[Veblen–Young theorem|NPNNXWMVCC]], every projective geometry of dimension at least $3$ is some $\mathbb{P}(V)$ over a division ring.
