---
tag: 5QAFGPAZ4A
kind: statement
role: theorem
name: Sphere theorem for 3-manifolds
msc: [57K30]
uses: [R20TB2KEQQ, 702SNFQG0W, P976WYEFMB, FH5WSPD79F]
about: [R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Sphere_theorem_(3-manifolds)
same_as:
  wikidata: Q7576684
  wikipedia: Sphere theorem (3-manifolds)
---

## Statement

Let $M$ be an [[orientable|702SNFQG0W]] [[3-manifold|R20TB2KEQQ]] whose second [[homotopy group|P976WYEFMB]] $\pi_2(M)$ is not trivial.
Then there is an embedding $S^2 \to M$ of the $2$-sphere that is not homotopic to a constant map.

## Remarks

Papakyriakopoulos proved the theorem in 1957 with the tower construction also used for [[Dehn's lemma|FH5WSPD79F]].
For example, in $M = S^2 \times S^1$ the sphere $S^2 \times \set{1}$ is embedded and generates $\pi_2(M) \cong \Z$.
A main consequence: if $M$ is orientable and irreducible, meaning that every embedded $2$-sphere bounds a $3$-ball, then $\pi_2(M) = 0$.
If moreover $\pi_1(M)$ is infinite, then $M$ is aspherical, that is, its universal cover is contractible.
Orientability cannot be dropped: in the non-orientable case one must also allow embedded two-sided projective planes, as in Epstein's version of the theorem.

## Explanations

### L1 human

The second homotopy group records spheres in a space that cannot be shrunk to a point.
The sphere theorem says that, in an orientable $3$-manifold, if there is any such sphere, then there is one that does not cross itself.
So a nontrivial $\pi_2$ is always witnessed by an embedded sphere.

### L2 human

The theorem explains why irreducible orientable $3$-manifolds have trivial $\pi_2$.
With infinite fundamental group, they are then Eilenberg–MacLane spaces, determined up to homotopy by $\pi_1$.
This is the starting point for the study of $3$-manifolds through their fundamental groups.
