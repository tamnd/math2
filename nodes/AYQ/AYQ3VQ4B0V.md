---
tag: AYQ3VQ4B0V
kind: definition
name: Essentially surjective functor
msc: [18A22]
defines: 6ERBSBVF14
uses: [28NQ0KRHD3, 859F0TFVA3, V3BFGKBJF7, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Essentially_surjective_functor
---

## Definition

Let $F \colon \mathcal{C} \to \mathcal{D}$ be a [[functor|28NQ0KRHD3]].
The functor $F$ is *essentially surjective* if, for every object $D$ of $\mathcal{D}$, there is an object $A$ of $\mathcal{C}$ with $F(A) \cong D$.
Here $\cong$ means that there is an [[isomorphism|859F0TFVA3]] in $\mathcal{D}$.

## Remarks

Example: let $K$ be a field and let $\mathcal{C}$ be the [[full subcategory|V3BFGKBJF7]] of finite-dimensional [[vector spaces|000AYPA9AJ]] over $K$ spanned by the spaces $K^n$, $n \ge 0$.
Its inclusion into all finite-dimensional vector spaces over $K$ is essentially surjective, since a space of dimension $n$ is isomorphic to $K^n$.
Non-example: the inclusion of the full subcategory of finite sets into the category of sets is not essentially surjective.
An infinite set is not isomorphic, that is, not in bijection with, any finite set.
Every functor that is surjective on objects is essentially surjective.
