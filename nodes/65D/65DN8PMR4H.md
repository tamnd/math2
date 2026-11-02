---
tag: 65DN8PMR4H
kind: definition
name: Duality in projective geometry
msc: [51A10, 51A05]
defines: DCMP1A0138
uses: [FGKNAFNHA3, DANFNN8C4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_(projective_geometry)
---

## Definition

Let $\Pi = (P, L, I)$ be a [[projective plane|DANFNN8C4Y]], seen as an [[incidence structure|FGKNAFNHA3]].
Its *dual plane* is $\Pi^{*} = (L, P, I^{\top})$, whose points are the lines of $\Pi$, whose lines are the points of $\Pi$, and where $(\ell, p) \in I^{\top}$ exactly when $(p, \ell) \in I$.
The *dual* of a statement about points, lines and incidence is the statement obtained by exchanging "point" with "line" and "lies on" with "passes through".
A *duality* (or *correlation*) of $\Pi$ is an isomorphism of incidence structures from $\Pi$ to $\Pi^{*}$.

## Remarks

The axioms of a projective plane are self-dual, so $\Pi^{*}$ is again a projective plane.
Hence the *principle of duality*: if a statement holds in every projective plane, so does its dual.

Example: $\mathbb{P}^2(k)$ over a field $k$ has a duality sending the point $[a : b : c]$ to the line $a x_0 + b x_1 + c x_2 = 0$ and the line $a x_0 + b x_1 + c x_2 = 0$ to the point $[a : b : c]$.
Check: the point $[x_0 : x_1 : x_2]$ lies on the line with coefficients $(a, b, c)$ exactly when $a x_0 + b x_1 + c x_2 = 0$, a condition symmetric in the two triples, so incidence is preserved in both directions.

Non-example: the dual of an [[affine plane|EC7XT2ZM5S]] is not an affine plane.
Two parallel lines become two points with no line through both, which fails the first axiom of an affine plane.

Let $\mathbb{P}(V)$ be a projective space of finite dimension $n$.
The map $W \mapsto W^{0}$, sending a subspace to its annihilator in the [[dual space|07JBSZE0V4]], reverses inclusion and exchanges projective dimensions $d$ and $n - 1 - d$.
