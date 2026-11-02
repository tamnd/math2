---
tag: D8C0EYD9ED
kind: concept
name: Subcategory
msc: [18A05]
specializes: [A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Subcategory
same_as:
  wikidata: Q541563
  wikipedia: Subcategory
---

## Summary

A subcategory of a [[category|A2DE66937D]] $\mathcal{C}$ is a choice of some objects and some [[morphisms|859F0TFVA3]] of $\mathcal{C}$.
The choice must be closed under composition and contain the identities of its objects.
It is a category in its own right, and its inclusion into $\mathcal{C}$ is a [[faithful functor|GRG8WEBSH5]].
Important special cases are the [[full subcategories|V3BFGKBJF7]], which keep all morphisms between the chosen objects, and the wide subcategories, which keep all objects.
The [[category of abelian groups|082GHNPJ53]] inside the category of groups is a standard example.

## Explanations

### L1 human

Start from a category and keep only part of it: some of the objects, and some of the arrows between them.
To still have a category, the identity arrow of each kept object must be kept, and a chain of kept arrows must compose to a kept arrow.
For example, among all sets and functions, keep all sets but only the injective functions.
Identities are injective and composites of injective functions are injective, so this is a subcategory.
