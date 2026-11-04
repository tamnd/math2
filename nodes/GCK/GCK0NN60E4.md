---
tag: GCK0NN60E4
kind: concept
name: Extension by definition
aliases: [definitional-extension, extension-by-definitions]
sources:
  - wikipedia: en:12219849@r1350903386
    locator: Extension by definition
    note: adopted
    mention: wikipedia://en/12219849
    sections: [Summary]
same_as:
  wikidata: Q5421941
  wikipedia: Extension by definition
inventory: [1W9VJE9M4M]
---

## Summary

In mathematical logic, more specifically in the proof theory of [[first-order theories|086QKPF0A6]], an **extension by definition** formalizes the introduction of a new symbol by means of a definition. For example, it is common in naive set theory to introduce a symbol $\emptyset$ for the [[set|0BSJ7RQ9BW]] that has no member. In the formal setting of first-order theories, this can be done by adding to the theory a new constant $\emptyset$ and the new axiom $\forall x(x\notin\emptyset)$, meaning "for all *x*, *x* is not a member of $\emptyset$". It can then be proved that doing so adds essentially nothing to the old theory, as should be expected from a definition. More precisely, the new theory is a conservative extension of the old one.
