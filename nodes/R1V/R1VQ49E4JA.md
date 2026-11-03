---
tag: R1VQ49E4JA
kind: concept
name: Hall basis
msc: [17B01, 17A50, 68R15]
sources:
  - url: https://en.wikipedia.org/wiki/Hall_word
---

## Summary

A Hall basis is a basis of a [[free Lie algebra|NNAXK7BM3H]] made of iterated brackets of the generators.
The brackets are chosen by a Hall set.
This is a totally ordered set of binary trees with simple rules on how a tree splits into its two subtrees.
Hall bases give explicit bases of free Lie algebras, and the related basic commutators describe the quotients of the lower central series of free groups.
The [[Lyndon basis|EERQK96TFT]] is one important Hall basis.

## Explanations

### L1 human

In a free Lie algebra on letters $a$ and $b$ one can write many brackets, such as $[a, b]$, $[b, a]$ and $[\,[a, b], [a, b]\,]$.
Most of them are redundant: $[b, a] = -[a, b]$, and $[x, x] = 0$ for every $x$.
A Hall set is a rule that selects some of the brackets.
Every bracket is a combination of the selected ones, and no selected one is a combination of the others.
So the selected brackets form a basis.
For two letters, the brackets of length at most $3$ in one such basis are $a$, $b$, $[a, b]$, $[a, [a, b]]$ and $[[a, b], b]$.
