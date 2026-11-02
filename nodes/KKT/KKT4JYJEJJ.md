---
tag: KKT4JYJEJJ
kind: object
name: Aronszajn tree
msc: ["03E05"]
uses: [011C29Q1S1, 0F1D6PK9RZ, 0ZG61TFBES, 0X55M9XET4]
sources:
  - url: https://en.wikipedia.org/wiki/Aronszajn_tree
same_as:
  wikidata: Q1192020
  wikipedia: Aronszajn tree
---

## Description

A tree, in set theory, is a [[partially ordered set|011C29Q1S1]] $(T, <)$ in which, for each $t \in T$, the set $\set{s \in T : s < t}$ is [[well-ordered|0F1D6PK9RZ]].
The height of $t$ is the order type of this set, and level $\alpha$ of $T$ is the set of elements of height $\alpha$.
A branch is a maximal linearly ordered subset of $T$.
An Aronszajn tree is a tree with these three properties:

1. Its height is $\omega_1$, the least [[uncountable|0X55M9XET4]] ordinal: the levels $\alpha < \omega_1$ are nonempty, and level $\omega_1$ is empty.
2. Each level is [[countable|0ZG61TFBES]].
3. It has no branch of length $\omega_1$, that is, no uncountable branch.

## Remarks

Aronszajn trees exist in ZFC, by a construction of Nachman Aronszajn.
One construction uses bounded, strictly increasing sequences of rational numbers, each of countable successor length, ordered by extension.
Levels are chosen by recursion on $\alpha < \omega_1$, so that each level is countable and each node has extensions at all higher levels with only slightly larger supremum.
An uncountable branch would give a strictly increasing sequence of rationals of length $\omega_1$, which is impossible since $\mathbb{Q}$ is countable.
This shows that König's lemma, which gives an infinite branch in each infinite finitely branching tree, has no analogue at $\omega_1$.
An Aronszajn tree in which every antichain is countable is a Suslin tree, and its existence is independent of ZFC.

## Explanations

### L1 human

Picture a tree that grows upward through $\omega_1$ levels, with only countably many nodes on each level.
You might expect some path to climb all the way to the top.
An Aronszajn tree is a tree of this kind in which every path stops at some countable level.
It shows that infinite combinatorics at $\omega_1$ behaves very differently from the countable case.
