---
tag: BRKFX8BQ60
kind: statement
role: theorem
name: Torelli theorem
msc: [14C34, 14H40]
uses: [XJM2MT4S3Y, ZQ84M9D9TC, R7W03TXRS9, 0PF6TM8TWT]
about: [XJM2MT4S3Y, ZQ84M9D9TC]
sources:
  - url: https://en.wikipedia.org/wiki/Torelli_theorem
same_as:
  wikidata: Q7825663
  wikipedia: Torelli theorem
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]].
Let $C$ and $C'$ be smooth projective connected [[curves|XJM2MT4S3Y]] over $k$.
Let $(J(C), \Theta)$ and $(J(C'), \Theta')$ be their [[Jacobian varieties|ZQ84M9D9TC]] with the principal polarizations given by their theta divisors.
Suppose that an isomorphism of [[abelian varieties|R7W03TXRS9]] $J(C) \to J(C')$ carries the polarization of $\Theta$ to that of $\Theta'$.
Then $C$ and $C'$ are isomorphic.

## Remarks

One proof, due to Andreotti, recovers $C$ from the geometry of $\Theta$.
Let $C$ be a curve that is not hyperelliptic.
The Gauss map sends a smooth point of $\Theta$ to its tangent hyperplane, and its branch locus is the dual of the canonical model of $C$.
Projective duality then gives back $C$.
Over $\C$, let $M_g$ be the moduli of curves of genus $g$ and $A_g$ the moduli of principally polarized abelian varieties of dimension $g$.
The theorem says that the Torelli map $M_g \to A_g$ is injective on points.
For example, two elliptic curves are isomorphic exactly when their Jacobians, which are the curves themselves, are isomorphic.
The polarization cannot be dropped in general: there are non-isomorphic curves whose Jacobians are isomorphic as unpolarized abelian varieties.

## Explanations

### L1 human

Every curve has a Jacobian, an abelian variety built from the curve, together with a special divisor $\Theta$ on it.
The theorem says that the Jacobian with this divisor remembers the curve completely.
So no information is lost when one passes from a curve to its polarized Jacobian.

### L2 human

The theorem reduces questions about curves to questions about principally polarized abelian varieties, which are described by period matrices.
Over $\C$, the period matrix of $C$ in the Siegel upper half space determines $C$.
The image of $M_g$ in $A_g$ is the Jacobian locus, and describing it is the Schottky problem.
There are Torelli theorems for other varieties, such as the global Torelli theorem for K3 surfaces.
In them the curve is replaced by the variety and the Jacobian by a Hodge structure.
