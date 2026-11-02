---
tag: CGH8C8EA9N
kind: concept
name: Elementary embedding
msc: [03C07]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
---

## Summary

An elementary embedding is a map between two [[structures|983GZBQYT4]] of the same signature that preserves and reflects the truth of every first-order formula.
Its image is an [[elementary substructure|8WZF9SBP39]] of the target, isomorphic to the source.
Elementary embeddings are the natural maps of model theory, and in set theory they are used to define large cardinals.

## Explanations

### L1 human

An ordinary embedding copies a structure into another one while keeping the operations and relations.
An elementary embedding keeps much more: every first-order statement about elements holds before the map exactly when it holds after.
The inclusion of $(\Q, <)$ into $(\R, <)$ is elementary.
The map $n \mapsto n + 1$ from $(\N, <)$ to $(\N, <)$ is an embedding, but not an elementary one: $0$ has no element below it, while its image $1$ has $0$ below it.
