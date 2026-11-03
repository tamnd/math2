---
tag: BDP8CBGV5Z
kind: definition
name: Motivic homotopy theory
msc: ["14F42", "19E15", "55P42"]
defines: K33643SC1Y
uses: [ND6XEY68P4, EXKGG9X6J0, H84VHC8PX2, WW81ARB8K9, AND2WHZC8P, SDTZVZ6B4Q, 48QQ7T98Z9]
sources:
  - url: https://en.wikipedia.org/wiki/A¹_homotopy_theory
---

## Definition

Let $S$ be a [[Noetherian scheme|ND6XEY68P4]] of finite Krull dimension, and let $\mathrm{Sm}_S$ be the category of [[smooth|EXKGG9X6J0]] schemes of finite type over $S$.
A family of [[étale morphisms|H84VHC8PX2]] $\{U_i \to X\}$ in $\mathrm{Sm}_S$ is a *Nisnevich covering* if the following holds.
For every point $x \in X$ there are an index $i$ and a point $u \in U_i$ over $x$ with the same residue field as $x$.
Consider the category of [[presheaves|AND2WHZC8P]] of [[simplicial sets|WW81ARB8K9]] on $\mathrm{Sm}_S$ with the Nisnevich-local [[model structure|SDTZVZ6B4Q]].
Its weak equivalences are the maps that induce isomorphisms on all Nisnevich sheaves of homotopy groups.
The *motivic*, or *$\mathbb{A}^1$-, model structure* is its left Bousfield localization at the projections $X \times_S \mathbb{A}^1_S \to X$ for all $X$ in $\mathrm{Sm}_S$.
Its [[homotopy category|48QQ7T98Z9]] $\mathcal{H}(S)$ is the *unstable motivic homotopy category* of $S$.
*Motivic homotopy theory* over $S$ is the study of this model category and of its stabilisation with respect to $\mathbb{P}^1$.

## Remarks

By construction the projection $\mathbb{A}^1_S \to S$ becomes an isomorphism in $\mathcal{H}(S)$, so the affine line is contractible.

There are two basic spheres: the simplicial circle $S^1$ and the punctured line $\mathbb{G}_m = \mathbb{A}^1 \setminus \{0\}$.
The projective line $\mathbb{P}^1_S$ is isomorphic in $\mathcal{H}(S)$ to the smash product $S^1 \wedge \mathbb{G}_m$ (with suitable base points).

Non-example: over a field $k$ with more than two elements, $\mathbb{G}_m$ is not contractible.
The sheaf of units is a Nisnevich sheaf with $\mathcal{O}(X \times \mathbb{A}^1)^\times = \mathcal{O}(X)^\times$ for reduced $X$, so it is $\mathbb{A}^1$-local.
Hence the morphisms $\operatorname{Spec} k \to \mathbb{G}_m$ in $\mathcal{H}(k)$ are the elements of $k^\times$, which is not a single point.

For a regular base $S$, algebraic K-theory of smooth $S$-schemes is representable in $\mathcal{H}(S)$ by $\Z \times \mathrm{BGL}_\infty$.
