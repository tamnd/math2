---
tag: 85H7PRHDPZ
kind: concept
name: Injective module
msc: [13C11, 16D50]
specializes: [0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_module
same_as:
  wikidata: Q2716519
  wikipedia: Injective module
---

## Summary

An injective module is a module $E$ such that every linear map into $E$ from a submodule extends to the whole module.
It is the dual notion of a [[projective module|BFFA03GE3V]], with the arrows reversed.
Every module embeds into an injective module, and the smallest such embedding is the [[injective hull|QCJN05GN64]].
Injective modules are used to build injective resolutions, which compute derived functors such as [[Ext|4P7GBWJ4RR]] and local cohomology.

## Explanations

### L1 human

Think of $E$ as a target that is big and flexible enough to receive maps.
If a linear map into $E$ is defined only on part of a module, it can always be extended to the whole module.
The rational numbers $\Q$ form an injective $\Z$-module, because you can divide in $\Q$ by any nonzero integer.
The integers $\Z$ are not injective: the map $2\Z \to \Z$ sending $2$ to $1$ cannot be extended to $\Z$, since then $1 = 2 \cdot (\text{image of } 1)$.
