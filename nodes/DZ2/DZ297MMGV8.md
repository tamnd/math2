---
tag: DZ297MMGV8
kind: concept
name: Locally finite family
msc: [54D20]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_finite_collection
same_as:
  wikidata: Q643300
  wikipedia: Locally finite collection
---

## Summary

A family of subsets of a [[topological space|0CQHFPGJ45]] is locally finite if each point has a [[neighbourhood|0ZCY0Z80B6]] meeting only finitely many members.
The family may be infinite, but near each point it looks finite.
Local finiteness lets one treat infinite unions and sums as if they were finite.
For example, the closure of the union of a locally finite family is the union of the closures.
It is the key notion in the definition of [[paracompact spaces|8R29G6NG9Q]] and of partitions of unity.

## Explanations

### L1 human

Think of tiles on an infinite floor: there are infinitely many tiles, but around any spot you stand on, only a few tiles are close by.
The intervals $[n, n + 1]$ for integers $n$ form such a family on the real line.
The intervals $(0, 1/n)$ for $n \ge 1$ do not, because every small interval around $0$ meets all of them.
