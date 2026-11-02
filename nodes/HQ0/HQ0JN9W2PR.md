---
tag: HQ0JN9W2PR
kind: definition
name: Projective conic
msc: ["51N15", "51E21"]
defines: R3TMVHTP3A
uses: [ZT9A6JK8QF, 0RBQS1JJCR, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Conic_section
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $\mathbb{P}^2(F)$ be the [[projective plane|ZT9A6JK8QF]] over $F$, with homogeneous coordinates $[x : y : z]$.
Let $Q$ be a nonzero [[quadratic form|0RBQS1JJCR]] on $F^3$.
The *projective conic* of $Q$ is the set
$$C(Q) = \set{[x : y : z] \in \mathbb{P}^2(F) : Q(x, y, z) = 0}.$$
The form $Q$ and its conic are *non-degenerate* if no invertible linear change of coordinates turns $Q$ into a form in at most two variables.

## Remarks

Example: $Q(x, y, z) = xz - y^2$.
Its points are $[1 : t : t^2]$ for $t \in F$ and the point $[0 : 0 : 1]$: if $x \ne 0$ scale to $x = 1$ and get $z = y^2$; if $x = 0$ then $y = 0$.
It is non-degenerate.
If $Q$ involved at most two variables in some coordinates, there would be a nonzero vector $v$ with $Q(u + v) = Q(u)$ for all $u$.
Here $Q(u + v) - Q(u) = u_x v_z + u_z v_x - 2 u_y v_y + Q(v)$, and this vanishes for all $u$ only if $v_x = v_z = 0$ and $Q(v) = -v_y^2 = 0$, so $v = 0$.
If $F = \F_q$, this conic has $q + 1$ points.

Non-example of non-degeneracy: $Q(x, y, z) = xy$ gives the union of the two lines $x = 0$ and $y = 0$.
It involves only $x$ and $y$, so it is degenerate.

Over $\R$, the non-degenerate form $x^2 + y^2 + z^2$ has an empty conic, so the form carries more information than the point set.
Over an algebraically closed field, or over $\R$ when the conic has a point, all non-degenerate conics are equivalent under projective transformations.
The affine [[conic sections|00HJCMC2CD]] are the parts of projective conics off the line at infinity.
