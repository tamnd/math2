---
tag: 7H0E1ZBWTB
kind: definition
name: Normal fan
msc: [52B11, 14M25]
defines: XJ83PTS3H0
uses: [300K6CB1KH, KY7SB854VH, 6VE4KA12VD]
sources:
  - url: https://en.wikipedia.org/wiki/Toric_variety
---

## Definition

Let $P$ be a nonempty [[convex polytope|300K6CB1KH]] in $\R^n$, and write $\ip{u}{x}$ for the standard inner product.
For a nonempty [[face|KY7SB854VH]] $F$ of $P$, the *normal cone* of $F$ is
$$N_F = \set{u \in \R^n : \ip{u}{x} \ge \ip{u}{y} \text{ for all } x \in F \text{ and } y \in P}.$$
So $N_F$ is the set of vectors $u$ such that the linear functional $\ip{u}{\cdot}$ attains its maximum over $P$ at every point of $F$.
The *normal fan* of $P$ is the collection $\mathcal{N}(P) = \set{N_F : F \text{ a nonempty face of } P}$.

## Remarks

Each $N_F$ is a polyhedral [[convex cone|6VE4KA12VD]], and $\dim N_F = n - \dim F$.
The collection $\mathcal{N}(P)$ is a complete fan:

1. every face of a cone of $\mathcal{N}(P)$ is a cone of $\mathcal{N}(P)$;
2. the intersection of two cones of $\mathcal{N}(P)$ is a face of each of them;
3. the union of all cones of $\mathcal{N}(P)$ is $\R^n$.

Inclusion is reversed: $F \subseteq G$ holds exactly when $N_G \subseteq N_F$.
Each $N_F$ contains the orthogonal complement of the direction space of the affine hull of $P$.
So the cones are pointed exactly when $P$ is full-dimensional, and then the vertices of $P$ give the $n$-dimensional cones and the facets give the rays.

Example: let $P = [-1,1]^2$.
The vertex $(1,1)$ maximizes $\ip{u}{\cdot}$ exactly when $u_1 \ge 0$ and $u_2 \ge 0$, so its normal cone is the closed first quadrant.
The edge $\set{1} \times [-1,1]$ is maximal exactly for $u_1 \ge 0$ and $u_2 = 0$, so its normal cone is the ray spanned by $(1,0)$.
The face $P$ itself has normal cone $\set{0}$.
So $\mathcal{N}(P)$ consists of the four closed quadrants, the four half-axes and the origin.

Non-example: the closed upper half-plane and the closed right half-plane do not form a fan, even with all their faces added.
Their intersection is the first quadrant, which is not a face of either half-plane, so clause 2 fails.

Some authors use the functionals that are minimal on $F$ instead; this replaces each cone by its negative.
The normal fan of a Minkowski sum $P + Q$ is the common refinement of the normal fans of $P$ and $Q$.
