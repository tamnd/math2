---
tag: PQRJ30QTYD
kind: definition
name: Pro-object
msc: [18A30]
defines: GAFQDGF6FM
uses: [1DKFWGWHH5, DAMK8XE1FR, 975PMY4FG8, CHS5AFJGWE, KA0YDB6QXE]
sources:
  - url: https://en.wikipedia.org/wiki/Ind-completion
---

## Definition

Let $\mathcal{C}$ be a category.
A small category $\mathcal{I}$ is *cofiltered* if its [[opposite category|DAMK8XE1FR]] $\mathcal{I}^{\mathrm{op}}$ is [[filtered|975PMY4FG8]].
A *pro-object* in $\mathcal{C}$ is a functor $X \colon \mathcal{I} \to \mathcal{C}$ with $\mathcal{I}$ small and cofiltered, written $(X_i)_{i \in \mathcal{I}}$.
For pro-objects $X \colon \mathcal{I} \to \mathcal{C}$ and $Y \colon \mathcal{J} \to \mathcal{C}$ the morphisms are
$$\mathrm{Pro}(\mathcal{C})(X, Y) = \lim_{j} \operatorname{colim}_{i} \mathcal{C}(X_i, Y_j).$$
The pro-objects with these morphisms form the category $\mathrm{Pro}(\mathcal{C})$.

## Remarks

There is an equivalence $\mathrm{Pro}(\mathcal{C}) \simeq \mathrm{Ind}(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}}$ with the [[Ind-completion|1DKFWGWHH5]] of the opposite category.
An object $c$ gives the constant pro-object indexed by the one-point category, and this gives a fully faithful functor $\mathcal{C} \to \mathrm{Pro}(\mathcal{C})$.
Every pro-object is the [[limit|CHS5AFJGWE]] in $\mathrm{Pro}(\mathcal{C})$ of its stages.

Example: in the category of finite groups, the groups $\Z / p^n \Z$ for $n \ge 1$, with the reduction maps, form a pro-object.
Its index category is the cofiltered poset $\N$ with an arrow $m \to n$ whenever $m \ge n$.
More generally, every [[profinite group|KA0YDB6QXE]] is the limit of the pro-object of its finite quotients.

Non-example: a functor from the discrete category with two objects to $\mathcal{C}$ is not a pro-object.
The discrete category with two objects is not cofiltered, since its two objects have no common object mapping to both.
