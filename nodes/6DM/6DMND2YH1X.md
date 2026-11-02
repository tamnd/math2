---
tag: 6DMND2YH1X
kind: definition
name: Concrete category of algebras
msc: ["08C05", "18A05"]
defines: ZD0GTPSJS1
uses: [FYBRP16KAN, WV3BPYCHVG, KBXSZC6BV1]
sources:
  - url: https://en.wikipedia.org/wiki/Concrete_category
---

## Definition

A [[concrete category|FYBRP16KAN]] is a pair $(\mathcal{C}, U)$ of a category $\mathcal{C}$ and a faithful functor $U \colon \mathcal{C} \to \mathbf{Set}$.
Faithful means: for all morphisms $f, g \colon A \to B$, $U(f) = U(g)$ implies $f = g$.
Let $\sigma$ be an algebraic signature and $K$ a class of $\sigma$-algebras closed under isomorphism.
Let $\mathcal{K}$ be the category with the members of $K$ as objects and the [[homomorphisms|KBXSZC6BV1]] between them as morphisms.
The *concrete category of algebras* of $K$ is the pair $(\mathcal{K}, U)$, where $U$ is the [[forgetful functor|WV3BPYCHVG]].

## Remarks

The functor $U$ is faithful because a homomorphism is determined by its underlying map.

Example: the category $\mathbf{Grp}$ of groups with its forgetful functor to $\mathbf{Set}$ is a concrete category of algebras.

Non-example: the category $\mathbf{Grp}$ with the functor that sends $G$ to the underlying set of its abelianization $G / [G, G]$ is not a concrete category, since this functor is not faithful.
The two homomorphisms $\Z \to S_3$ that send $1$ to the transpositions $(1\,2)$ and $(1\,3)$ are different, but both induce the map $\Z \to \Z / 2\Z$ that sends $1$ to the nontrivial element.

Not every category admits a faithful functor to $\mathbf{Set}$: by a theorem of Freyd, the homotopy category of topological spaces does not.
