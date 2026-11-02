---
tag: Y1RAX7VVBX
kind: definition
name: Full subcategory
msc: [18A05]
defines: V3BFGKBJF7
uses: [A2DE66937D, D8C0EYD9ED, 082GHNPJ53, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Subcategory
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
A *full subcategory* of $\mathcal{C}$ is a [[subcategory|D8C0EYD9ED]] $\mathcal{D}$ such that $\Hom_{\mathcal{D}}(A, B) = \Hom_{\mathcal{C}}(A, B)$ for all objects $A$, $B$ of $\mathcal{D}$.

## Remarks

For every subclass $S$ of $\mathrm{Ob}(\mathcal{C})$ there is exactly one full subcategory with object class $S$, the full subcategory *spanned* by $S$.
Example: the [[abelian groups|082GHNPJ53]] form a full subcategory of the category of [[groups|G5S1M9]].
A morphism between two abelian groups in the category of groups is a group homomorphism, and every such homomorphism is a morphism of the subcategory.
Non-example: the subcategory of sets with all sets as objects and only the injective functions as morphisms is not full.
The constant map $\set{0, 1} \to \set{0}$ is a morphism of the category of sets between two of its objects, but it is not injective.
