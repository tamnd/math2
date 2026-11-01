---
tag: 8KPDNVKX7B
kind: concept
name: Formally smooth map
msc: [13B40, 13D10, 14B25]
sources:
  - url: https://en.wikipedia.org/wiki/Formally_smooth_map
same_as:
  wikidata: Q5469991
  wikipedia: Formally smooth map
---

## Summary

A map of commutative rings $R \to A$ is formally smooth when it has a lifting property.
Every map from $A$ to a quotient $C/J$ by an ideal $J$ with $J^2 = 0$ must lift to a map to $C$.
This is the algebraic form of an idea from geometry.
On a smooth space, there is no obstruction to extending a point to a small thickening.
Together with finite presentation it gives the notion of a [[smooth morphism of rings|286G0P1B69]], and with uniqueness of the lift it gives formally étale maps.

## Explanations

### L1 human

Think of a map $A \to C/J$ as a point of the space of $A$ with coordinates in $C/J$.
Since $J^2 = 0$, the ring $C$ is only a little bigger than $C/J$, like adding a first-order neighbourhood.
Formal smoothness says that every such point extends to $C$.
A polynomial ring has this property, because one may lift the images of the variables freely.
The ring $k[x]/(x^2)$ does not: the point $x \mapsto x$ of $k[x]/(x^2)$ does not extend to $k[x]/(x^3)$, since no lift squares to $0$.
