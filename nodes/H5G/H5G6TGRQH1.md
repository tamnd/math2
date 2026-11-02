---
tag: H5G6TGRQH1
kind: example
name: Lattice of subspaces
msc: [06C05, 06B23, 51A05]
instance_of: [D7A0ZGZT5S, QX7WZ92QAK]
uses: [000AYPA9AJ, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_geometry
---

## Example

Let $V$ be a [[vector space|000AYPA9AJ]] over a field $F$, and let $L(V)$ be the set of all [[linear subspaces|00YC1D652K]] of $V$, ordered by inclusion.
The meet of two subspaces $U$ and $W$ is $U \cap W$, and their join is the sum $U + W = \set{u + w : u \in U, w \in W}$.
For any family $(U_i)_{i \in I}$ of subspaces, the intersection $\bigcap_i U_i$ and the span of $\bigcup_i U_i$ are subspaces.
They are the greatest lower bound and the least upper bound of the family.
So $L(V)$ is a [[complete lattice|D7A0ZGZT5S]], with least element $\set{0}$ and greatest element $V$.
It is a [[modular lattice|QX7WZ92QAK]]: if $U \subseteq W$, then $U + (X \cap W) = (U + X) \cap W$ for every subspace $X$.
The inclusion $U + (X \cap W) \subseteq (U + X) \cap W$ holds because $U \subseteq W$.
For the other inclusion, an element $w = u + x$ of the right side with $u \in U$, $x \in X$ has $x = w - u \in W$, so $x \in X \cap W$.

## Remarks

The lattice $L(V)$ is not distributive once $\dim V \ge 2$.
In $V = \R^2$, take three distinct lines $a$, $b$, $c$ through $0$.
Then $a \cap (b + c) = a \cap \R^2 = a$, while $(a \cap b) + (a \cap c) = \set{0}$.
When $V$ is finite-dimensional, the subspaces of dimension $1$ and $2$ are the points and lines of the projective space of $V$, and $L(V)$ encodes its incidence geometry.

## Explanations

### L1 human

Take all the subspaces of a vector space: the zero space, the lines through the origin, the planes through the origin, and so on up to the whole space.
Order them by inclusion.
Any two subspaces have a largest common subspace, their intersection, and a smallest subspace containing both, their sum.
For two distinct lines in $\R^3$, the intersection is $\set{0}$ and the sum is the plane they span.
This ordered set is the basic example of a modular lattice that is not distributive, and it is the algebraic skeleton of projective geometry.
