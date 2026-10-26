---
tag: ~f0cecd69
kind: definition
name: Centraliser
aliases: [centralizer]
msc: [20A05]
defines: ~524f86a3
uses: [~74c6b403]
sources:
  - url: https://en.wikipedia.org/wiki/Centralizer_and_normalizer
    locator: Group and semigroup
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $S$ be a subset of $G$.
The centraliser of $S$ in $G$ is the set $C_G(S) = \{g \in G : gs = sg \text{ for all } s \in S\}$.
For an element $a \in G$, we write $C_G(a)$ for $C_G(\{a\})$.

## Remarks

The centraliser $C_G(S)$ is a [[subgroup|~b600248b]] of $G$.
The centraliser of $G$ itself is the [[centre|~ff52f9c7]] $Z(G)$.
The element $a$ lies in its own centraliser $C_G(a)$, and so does each power of $a$.

## Explanations

### L1 human

The centraliser of an element is the set of elements that commute with it.
If the element commutes with everything, its centraliser is the whole group.
The size of the centraliser tells you how many conjugates the element has.
