---
tag: QK2ECEQYA5
kind: statement
role: theorem
name: Atiyah–Singer index theorem
msc: [58J20, 19K56, 19L64]
uses: [MT9P2X85V8, F31T650DKY, 2V9Q4KHY1T, P4DZM975BV, 9E4JE4902G, JBX99NRRB6, WN2DCBSX1C, 6XRTXBPASW, 2YDB5089FR, G3X02FKQCR, TEG1ZX1AGJ, GG6NYPKMHX, JR2M58RCW3]
about: [MT9P2X85V8, 2V9Q4KHY1T]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
same_as:
  wikidata: Q755991
  wikipedia: Atiyah–Singer index theorem
---

## Statement

Let $M$ be a closed smooth manifold, let $E$ and $F$ be complex [[vector bundles|P4DZM975BV]] over $M$, and let $P \colon C^\infty(M; E) \to C^\infty(M; F)$ be an [[elliptic differential operator|MT9P2X85V8]].
Then $P$ has finite-dimensional kernel and cokernel, and its analytic index is
$$\operatorname{ind} P = \dim \ker P - \dim \operatorname{coker} P.$$
The [[principal symbol|F31T650DKY]] of $P$ is invertible off the zero section of the cotangent bundle $T^*M$.
So it defines a class $[\sigma(P)]$ in the compactly supported [[complex K-theory|9E4JE4902G]] $K_c(T^*M)$.
Let $\operatorname{t-ind} \colon K_c(T^*M) \to \Z$ be the topological index, defined as follows.
Embed $M$ in some $\R^N$.
Push the class forward to $K_c(T^*\R^N) = K_c(\C^N)$ by the [[Thom isomorphism in K-theory|JBX99NRRB6]] for the complexified normal bundle.
Then identify $K_c(\C^N) \cong \Z$ by [[Bott periodicity|WN2DCBSX1C]].
The theorem states that
$$\operatorname{ind} P = \operatorname{t-ind}[\sigma(P)].$$

## Remarks

The original proof used cobordism invariance of the index; the K-theoretic proof shows that both sides are homomorphisms $K_c(T^*M) \to \Z$ that are compatible with embeddings and agree for $M$ a point.
Combined with the [[Chern character|6XRTXBPASW]], it gives a cohomological formula.
Up to a sign fixed by orientation conventions, $\operatorname{ind} P$ is the integral over $T^*M$ of $\operatorname{ch}[\sigma(P)]$ times the pullback of the [[Todd class|2YDB5089FR]] of $TM \otimes \C$.

Example: on a compact Riemann surface of genus $g$, the operator $\bar{\partial}$ on sections of a holomorphic line bundle $L$ has index $\deg L + 1 - g$, which is the Riemann–Roch theorem.

Ellipticity is necessary: for a non-elliptic operator such as $\partial/\partial x$ acting on functions on the torus $\R^2/\Z^2$, the kernel is infinite-dimensional, since it contains every function of $y$ alone.

## Explanations

### L1 human

An elliptic operator is a differential operator, like the Laplacian, whose equations have only finitely many independent solutions on a closed manifold.
The index counts solutions minus obstructions to solving, and it does not change when the operator is deformed.
The theorem says that this analytic number can be computed from topology alone: from the leading part of the operator and the shape of the manifold.

### L2 human

Many classical theorems are special cases.
The de Rham operator gives the [[Chern–Gauss–Bonnet theorem|GG6NYPKMHX]], and the signature operator gives the [[Hirzebruch signature theorem|TEG1ZX1AGJ]].
The Dolbeault operator gives the [[Hirzebruch–Riemann–Roch theorem|G3X02FKQCR]].
The spin Dirac operator gives the [[Â-genus as the index of the Dirac operator|JR2M58RCW3]].
The last case shows that the $\hat{A}$-genus of a closed spin manifold is an integer, and that it vanishes when the manifold has a metric of positive scalar curvature.
Generalizations include the equivariant, families, and real index theorems, and the index theorem for manifolds with boundary.
