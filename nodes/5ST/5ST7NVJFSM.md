---
tag: 5ST7NVJFSM
kind: concept
name: Derived category
msc: [18G80, 14F08, 13D09]
sources:
  - url: https://en.wikipedia.org/wiki/Derived_category
same_as:
  wikidata: Q5262626
  wikipedia: Derived category
---

## Summary

The derived category $D(\mathcal{A})$ of an [[abelian category|Y9CZ3MTNF1]] $\mathcal{A}$ is obtained from the category of [[chain complexes|WQ82C0M3QB]] by declaring every [[quasi-isomorphism|C9JEC2WQKV]] to be an isomorphism.
In it, an object and any of its resolutions become isomorphic, so derived functors become ordinary functors between derived categories.
It is a [[triangulated category|T2V7GJJ2EN]], and $\operatorname{Ext}^n(X, Y)$ is the group of morphisms from $X$ to $Y[n]$.
Derived categories are the standard setting for duality theorems, for sheaf theory and for modern algebraic geometry.

## Explanations

### L1 human

In homological algebra one replaces an object by a resolution, and many different resolutions carry the same information.
The derived category builds this freedom into the category itself: two complexes count as the same object when a map between them induces isomorphisms on homology.
For example, the complex $\Z \xrightarrow{2} \Z$ and the group $\Z/2\Z$ become isomorphic.
This makes the machinery of derived functors much simpler to state and compose.
