---
tag: 290G1NGAMR
kind: definition
name: Ind-completion
msc: [18A30, 18C35]
defines: 1DKFWGWHH5
uses: [975PMY4FG8, AND2WHZC8P, KCCHH87H6E, BJS1CGTKQ5, 4DKB6AQ8J7]
sources:
  - url: https://en.wikipedia.org/wiki/Ind-completion
---

## Definition

Let $\mathcal{C}$ be a small category, and let $y \colon \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ be the [[Yoneda embedding|4DKB6AQ8J7]] into [[presheaves|AND2WHZC8P]].
A presheaf $P$ on $\mathcal{C}$ is an *ind-object* if there are a small [[filtered category|975PMY4FG8]] $\mathcal{I}$ and a functor $X \colon \mathcal{I} \to \mathcal{C}$ with $P \cong \operatorname{colim}_{i} y(X_i)$.
The *Ind-completion* $\mathrm{Ind}(\mathcal{C})$ is the full subcategory of $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ whose objects are the ind-objects.

## Remarks

So an ind-object is a filtered [[colimit|BJS1CGTKQ5]] of [[representable presheaves|KCCHH87H6E]].
In terms of the diagrams $X \colon \mathcal{I} \to \mathcal{C}$ and $Y \colon \mathcal{J} \to \mathcal{C}$, the morphisms are
$$\mathrm{Ind}(\mathcal{C})(X, Y) = \lim_{i} \operatorname{colim}_{j} \mathcal{C}(X_i, Y_j).$$
The functor $y$ gives a fully faithful functor $\mathcal{C} \to \mathrm{Ind}(\mathcal{C})$, and $\mathrm{Ind}(\mathcal{C})$ has all small filtered colimits.
It is universal: every functor from $\mathcal{C}$ to a category with filtered colimits extends, uniquely up to isomorphism, to a filtered-colimit-preserving functor on $\mathrm{Ind}(\mathcal{C})$.

Example: let $\mathcal{C}$ be a skeleton of the category of finite sets.
Every set is the filtered colimit of its finite subsets, and this gives an equivalence between $\mathrm{Ind}(\mathcal{C})$ and the category of sets.

Non-example: let $\mathcal{C} = \mathbf{1}$, the category with one object and one morphism.
A presheaf on $\mathbf{1}$ is a set, and the only representable is a one-point set.
A filtered category is nonempty and connected, so every filtered colimit of one-point sets along identities is a one-point set.
So a presheaf with two elements, or with none, is not an ind-object.
