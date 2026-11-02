---
tag: GCBY80CSC6
kind: statement
role: theorem
name: Tubular neighborhood theorem
msc: [57R40, 57N40, 58A05]
uses: [F45VQ47GPV, VKFW27WXEZ, WY6K3P4YCG, 0KZZ70ZHXP]
about: [VKFW27WXEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Tubular_neighborhood
---

## Statement

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $S \subseteq M$ be an [[embedded submanifold|VKFW27WXEZ]] without boundary.
Let $NS = TM|_S / TS$ be the normal bundle of $S$.
It is the quotient of the restriction to $S$ of the [[tangent bundle|WY6K3P4YCG]] of $M$ by the tangent bundle of $S$.
Identify $S$ with the zero section of $NS$.
Then there is an open neighbourhood $U$ of $S$ in $M$ and a [[diffeomorphism|0KZZ70ZHXP]] $\Phi \colon NS \to U$ such that $\Phi(s) = s$ for every $s \in S$.

## Remarks

Such a $U$, with the diffeomorphism $\Phi$, is a *tubular neighbourhood* of $S$.
For $M = \R^n$ the proof is direct: identify $NS$ with the bundle of vectors orthogonal to $S$, and consider $E(s, v) = s + v$.
Its differential along the zero section is an isomorphism.
By the inverse function theorem, $E$ is a local diffeomorphism near the zero section.
An extra argument shows that $E$ is injective, hence a diffeomorphism onto an open set, on a neighbourhood of the zero section that may shrink along $S$.
A fibrewise rescaling of $NS$ onto that neighbourhood finishes the proof.
For a general $M$ one replaces $s + v$ by the exponential map of a Riemannian metric, or embeds $M$ in some $\R^N$.
Example: the circle $S^1 \times \set{0}$ in $\R^3$ has trivial normal bundle, and a solid torus around it is a tubular neighbourhood, diffeomorphic to $S^1 \times \R^2$.
A tubular neighbourhood of the central circle of the open Möbius band is the whole band, which is the total space of the nontrivial line bundle over $S^1$.
Tubular neighbourhoods are unique up to isotopy.

## Explanations

### L1 human

Around a smooth submanifold there is always a thickened copy of it that looks like a bundle of small discs, one disc sticking out at each point.
Around a closed curve in space this is a thin tube, which is where the name comes from.
The theorem lets one study the neighbourhood of a submanifold through linear algebra on its normal bundle.

### L2 human

The theorem is used to cut and paste manifolds along submanifolds, as in surgery, connected sums along submanifolds and Dehn surgery on knots.
It identifies the quotient of $M$ by the complement of a tubular neighbourhood of $S$ with the Thom space of $NS$, which is the key step of the Pontryagin–Thom construction.
It also gives a smooth retraction of a neighbourhood of $S$ onto $S$, which is used to approximate continuous maps by smooth ones.
For manifolds with boundary, the companion result is the collar neighbourhood theorem.
