---
tag: V8PEAAE4K1
kind: definition
name: Stone-type duality for varieties
msc: ["08C20", "06D50", "06E15"]
defines: VH12PN9V13
uses: [AJNZJD8442, WRXEKT4NQS, ZV38HA5PAQ, K7A04ZBD92, DAMK8XE1FR]
sources:
  - url: https://en.wikipedia.org/wiki/Stone_duality
---

## Definition

Let $\mathcal{A}$ be a [[variety|AJNZJD8442]] or a [[quasivariety|WRXEKT4NQS]] of algebras, regarded as a category whose morphisms are the homomorphisms.
Let $\mathcal{X}$ be a category whose objects are [[Stone spaces|ZV38HA5PAQ]] with additional relations or operations.
Recall that a Stone space is a compact Hausdorff totally disconnected space.
The morphisms of $\mathcal{X}$ are the continuous maps that preserve the additional structure.
A *Stone-type duality* for $\mathcal{A}$ is an [[equivalence|K7A04ZBD92]] between $\mathcal{A}$ and the [[opposite category|DAMK8XE1FR]] $\mathcal{X}^{\mathrm{op}}$.
Equivalently, it is a pair of contravariant functors $D \colon \mathcal{A} \to \mathcal{X}$ and $E \colon \mathcal{X} \to \mathcal{A}$ with natural isomorphisms $A \cong E(D(A))$ and $X \cong D(E(X))$.

## Remarks

In most examples $D$ and $E$ are represented by one set with two structures.
Then $D(A)$ is the set of homomorphisms from $A$ to a fixed finite algebra.
And $E(X)$ is the set of morphisms from $X$ to the same set with a discrete topology.

Example: Boolean algebras and Stone spaces.
Here $D(A)$ is the set of homomorphisms $A \to \set{0, 1}$, a closed subspace of $\set{0, 1}^A$, and $E(X)$ is the Boolean algebra of clopen subsets of $X$.
Both composites are naturally isomorphic to the identity, by Stone's representation theorem.

Non-example: Pontryagin duality between abelian groups and compact abelian groups is a dual equivalence, but not of this type.
The circle group $\R / \Z$ is the dual of $\Z$, and it is connected, so it is not a Stone space.

Bounded distributive lattices are dual to Priestley spaces, which are Stone spaces with a partial order satisfying a separation condition.
