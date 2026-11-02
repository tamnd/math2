---
tag: AT8K76KJ5R
kind: definition
name: Subcategory
msc: [18A05]
defines: D8C0EYD9ED
uses: [A2DE66937D, 859F0TFVA3, 082GHNPJ53, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Subcategory
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
A *subcategory* $\mathcal{D}$ of $\mathcal{C}$ consists of a subclass $\mathrm{Ob}(\mathcal{D}) \subseteq \mathrm{Ob}(\mathcal{C})$ and, for all $A, B \in \mathrm{Ob}(\mathcal{D})$, a subclass $\Hom_{\mathcal{D}}(A, B) \subseteq \Hom_{\mathcal{C}}(A, B)$ of [[morphisms|859F0TFVA3]], such that:

1. $1_A \in \Hom_{\mathcal{D}}(A, A)$ for every $A \in \mathrm{Ob}(\mathcal{D})$;
2. $g \circ f \in \Hom_{\mathcal{D}}(A, C)$ for all $f \in \Hom_{\mathcal{D}}(A, B)$ and $g \in \Hom_{\mathcal{D}}(B, C)$.

## Remarks

With the composition and identities of $\mathcal{C}$, a subcategory is a category.
It is *wide* if $\mathrm{Ob}(\mathcal{D}) = \mathrm{Ob}(\mathcal{C})$, and *full* if $\Hom_{\mathcal{D}}(A, B) = \Hom_{\mathcal{C}}(A, B)$ for all its objects $A$, $B$.
Example: inside the category of [[groups|G5S1M9]], the [[abelian groups|082GHNPJ53]] with all homomorphisms between them form a subcategory.
The identity of an abelian group is a homomorphism, and a composite of homomorphisms is a homomorphism.
Non-example: in the category of sets, keep all sets but only the functions whose image has at most one point.
Composites of such functions are again of this kind, so clause 2 holds, but the identity of $\set{0, 1}$ is missing, so clause 1 fails.
