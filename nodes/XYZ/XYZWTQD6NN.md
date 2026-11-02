---
tag: XYZWTQD6NN
kind: definition
name: Skeleton of a category
msc: [18A05, 18A22]
defines: A49QJYG669
uses: [A2DE66937D, V3BFGKBJF7, 859F0TFVA3, K7A04ZBD92, WA60RW9E04]
sources:
  - url: https://en.wikipedia.org/wiki/Skeleton_(category_theory)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
A *skeleton* of $\mathcal{C}$ is a [[full subcategory|V3BFGKBJF7]] $\mathcal{S}$ of $\mathcal{C}$ such that every object of $\mathcal{C}$ is [[isomorphic|859F0TFVA3]] to exactly one object of $\mathcal{S}$.

## Remarks

A category is *skeletal* if isomorphic objects in it are equal; a skeleton is a skeletal full subcategory that meets every isomorphism class.
Under the axiom of choice every category has a skeleton, and its inclusion is fully faithful and essentially surjective.
So the inclusion is an [[equivalence of categories|K7A04ZBD92]] by [[the criterion for equivalences|WA60RW9E04]].
Any two skeletons of $\mathcal{C}$ are isomorphic categories.
Example: in the category of finite sets, the full subcategory on the sets $[n] = \set{1, \dots, n}$, $n \ge 0$, with $[0] = \emptyset$, is a skeleton.
A finite set with $n$ elements is in bijection with $[n]$, and $[m]$ and $[n]$ are not in bijection when $m \ne n$.
Non-example: the full subcategory on the sets $[n]$ together with $\set{a, b}$ is not a skeleton, since $\set{a, b}$ and $[2]$ are two of its objects in the same isomorphism class.
