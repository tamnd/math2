---
tag: V2HTMG4KT1
kind: statement
role: theorem
name: Weil's local rigidity theorem
msc: ["22E40", "22E41"]
uses: [BTYF5Y5PFY, XJS07AJ50Y, 0JYTG5K9Y4]
about: [BTYF5Y5PFY]
sources:
  - url: https://en.wikipedia.org/wiki/Local_rigidity
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite center.
Assume that $G$ has no compact factor and no factor locally isomorphic to $\mathrm{SL}_2(\R)$.
Let $\Gamma$ be a uniform [[lattice|BTYF5Y5PFY]] in $G$, so that $G/\Gamma$ is compact, and let $\iota \colon \Gamma \to G$ be the inclusion.
Give the set $\Hom(\Gamma, G)$ of [[group homomorphisms|0JYTG5K9Y4]] the topology of pointwise convergence.
Then $\iota$ is locally rigid: $\iota$ has a neighbourhood $U$ in $\Hom(\Gamma, G)$ with the following property.
For every $\rho \in U$ there is $g \in G$ with $\rho(\gamma) = g \gamma g^{-1}$ for all $\gamma \in \Gamma$.

## Remarks

A uniform lattice is finitely generated, so the topology on $\Hom(\Gamma, G)$ is that of a real algebraic set, given by the images of finitely many generators.
Weil proved a general criterion for a homomorphism $\rho$ from a finitely generated group $\Gamma$ to $G$.
Let $\Gamma$ act on the Lie algebra $\mathfrak{g}$ of $G$ through $\rho$ and the adjoint representation.
If the first cohomology group $H^1(\Gamma, \mathfrak{g})$ vanishes, then $\rho$ is locally rigid.
The tangent space to deformations of $\rho$ is the space of cocycles, and conjugations give the coboundaries, so vanishing of $H^1$ means that every infinitesimal deformation is a conjugation.
He then proved this vanishing for uniform lattices under the hypotheses above.
The hypothesis on $\mathrm{SL}_2(\R)$ is necessary.
The fundamental group of a closed hyperbolic surface sits in $\mathrm{PSL}_2(\R)$ as a uniform lattice, and it has a continuous family of non-conjugate deformations, described by [[Teichmüller space|ZZGC6BZNJ5]].
Garland and Raghunathan extended the result to non-uniform lattices in groups of real rank one other than those locally isomorphic to $\mathrm{SL}_2(\R)$ and $\mathrm{SL}_2(\C)$.

## Explanations

### L1 human

A uniform lattice is a discrete group of symmetries that tiles a big continuous group with compact tiles.
The theorem says that one cannot wiggle such a lattice slightly to get a genuinely new one.
Every small change of the lattice is just the same lattice seen from a different point, that is, conjugated by an element of $G$.
The only exception is the group $\mathrm{SL}_2(\R)$ and its relatives, where surfaces can be deformed.

### L2 human

Local rigidity is the first of a chain of rigidity results for lattices.
[[Mostow rigidity|4BEWKR0EG7]] upgrades it to a global statement: an abstract isomorphism between lattices extends to the ambient groups.
[[Margulis superrigidity|DSKV65NHZZ]] goes further for higher rank, by controlling all homomorphisms of a lattice into other groups.
