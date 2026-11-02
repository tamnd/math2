---
tag: TX4MSZ0SRP
kind: statement
role: theorem
name: JSJ decomposition
msc: [57K30]
uses: [R20TB2KEQQ, 702SNFQG0W, 6N9GW98MR6, 9V1GF5WMKA, A1E8TDEVJ9]
about: [R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/JSJ_decomposition
same_as:
  wikidata: Q683430
  wikipedia: JSJ decomposition
---

## Statement

Let $M$ be a closed connected [[orientable|702SNFQG0W]] irreducible [[3-manifold|R20TB2KEQQ]], where irreducible means that every embedded $2$-sphere bounds a $3$-ball.
A compact $3$-manifold $N$ is *atoroidal* if every [[incompressible|6N9GW98MR6]] torus in $N$ is parallel to a boundary torus of $N$.
Then $M$ contains a finite collection $\mathcal{T}$ of disjoint embedded incompressible tori with the following property.
Each component of $M$ cut along $\mathcal{T}$ is atoroidal or a [[Seifert fiber space|9V1GF5WMKA]].
A minimal collection $\mathcal{T}$ with this property is unique up to isotopy.

## Remarks

The theorem is due to Jaco and Shalen, and independently to Johannson.
Existence rests on Haken's finiteness theorem, which bounds the number of disjoint, pairwise non-parallel incompressible surfaces.
Uniqueness comes from the study of how incompressible tori meet Seifert fibered pieces.
A version of the theorem holds for compact manifolds whose boundary is a union of tori.
For example, take a [[satellite knot|A1E8TDEVJ9]] in $S^3$.
The boundary of a neighborhood of the companion knot is an incompressible torus in the knot complement, so the complement is not atoroidal.
If $M$ is itself Seifert fibered or atoroidal, the minimal collection is empty.

## Explanations

### L1 human

After splitting a $3$-manifold into prime pieces, one can split each piece further along essential tori.
The JSJ theorem says there is a best way to do this, and that it is unique.
Each resulting piece is either built from circles in a regular way or contains no essential torus at all.

### L2 human

The JSJ decomposition is the second step of geometrization, after the prime decomposition.
By the geometrization theorem, the atoroidal pieces that are not Seifert fibered have hyperbolic interiors.
So every closed orientable irreducible $3$-manifold is assembled from Seifert fibered and hyperbolic pieces glued along tori.
