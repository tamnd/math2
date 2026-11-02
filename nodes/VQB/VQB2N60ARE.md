---
tag: VQB2N60ARE
kind: statement
role: theorem
name: Slice theorem
msc: ["57S15", "22E15"]
uses: [R2TQ82PCNB, 0YSE802YCQ, 0RGGF8ZS6D, 00F2JFA41J, RK8RV2C998, 0Z1Y7JHGBR, GCBY80CSC6]
about: [0YSE802YCQ, 00F2JFA41J]
sources:
  - url: https://en.wikipedia.org/wiki/Slice_theorem_(differential_geometry)
same_as:
  wikidata: Q17093903
  wikipedia: Slice theorem (differential geometry)
---

## Statement

Let $G$ be a compact Lie group with a smooth [[action|0YSE802YCQ]] on a [[smooth manifold|R2TQ82PCNB]] $M$.
Let $x \in M$, let $G x$ be its [[orbit|00F2JFA41J]], and let $H = G_x$ be its [[stabiliser|0RGGF8ZS6D]], a closed subgroup of $G$.
Let $V = T_x M / T_x(G x)$ be the normal space of the orbit at $x$.
The group $H$ acts linearly on $V$ by the derivatives at $x$ of the maps $y \mapsto h y$ for $h \in H$; this is a [[representation|RK8RV2C998]] of $H$.
Let $G \times_H V$ be the quotient of $G \times V$ by the action $h \cdot (g, v) = (g h^{-1}, h v)$ of $H$, with $G$ acting by $g' [g, v] = [g' g, v]$.
Then there are a $G$-invariant open neighbourhood $U$ of $G x$ in $M$ and a $G$-equivariant [[diffeomorphism|0Z1Y7JHGBR]] $\Phi \colon G \times_H V \to U$.
Moreover $\Phi([e, 0]) = x$, where $e$ is the identity of $G$.

## Remarks

The idea of the proof is to average a Riemannian metric on $M$ over $G$, which is possible because $G$ is compact.
The new metric is $G$-invariant, so the exponential map on the normal bundle of the orbit $G x$ is $G$-equivariant.
The orbit is a compact submanifold diffeomorphic to $G / H$, and its normal bundle is $G \times_H V$.
The [[tubular neighbourhood theorem|GCBY80CSC6]] gives $\Phi$ from this exponential map on vectors of small length.
The image $S = \Phi(\set{[e, v] : v \in V})$ is called a *slice* at $x$: it is $H$-invariant, and $g S \cap S \neq \emptyset$ implies $g \in H$.
Example: let $G = SO(2)$ act on $\R^2$ by rotations and let $x = (1, 0)$.
Then $H$ is trivial, $V$ is the radial line $\R$, and $\Phi([g, t]) = g (e^t, 0)$ is an equivariant diffeomorphism from $SO(2) \times \R$ onto $U = \R^2 \setminus \set{0}$.
Compactness can be replaced by properness of the action, a result of Palais.
Without such a hypothesis the theorem fails.
Let $\R$ act on the torus $\R^2 / \Z^2$ by translations along a line of irrational slope.
Every orbit is dense, so no orbit has a neighbourhood of the form $G \times_H V$ in which it is closed.

## Explanations

### L1 human

When a compact group of symmetries moves a manifold around, the theorem describes how the manifold looks near one orbit.
Near the orbit, the manifold is a thickened copy of the orbit.
The thickening is a small disk at each point of the orbit, and the symmetries that fix the point turn this disk by linear maps.

### L2 human

The theorem reduces local questions about smooth actions of compact groups to linear algebra.
It shows that every orbit has a neighbourhood that retracts onto it equivariantly, and that the stabilisers of nearby points are conjugate to subgroups of $H$.
From it one derives the principal orbit type theorem.
It also shows that the quotient of a manifold by a free action of a compact Lie group is again a manifold.
When $G$ is finite and acts faithfully, it shows that $M / G$ is an [[orbifold|RPAVY0W0XS]].
