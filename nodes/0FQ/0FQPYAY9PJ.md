---
tag: 0FQPYAY9PJ
kind: definition
name: Meagre set
aliases: [meager-set, first-category-set]
msc: ["54E52"]
defines: 0XGCZ4GDZ6
uses: [0KSM23SN3H, 0ZG61TFBES]
sources:
  - url: https://en.wikipedia.org/wiki/Meagre_set
    locator: Definitions
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $A \subseteq X$.
The set $A$ is meagre in $X$ when there is a [[countable|0ZG61TFBES]] family $(A_n)_{n \in \mathbb{N}}$ of [[nowhere dense|0KSM23SN3H]] subsets of $X$ with $A = \bigcup_{n} A_n$.

## Remarks

Another name for a meagre set is a set of first category. A set that is not meagre is of second category.
Each subset of a meagre set is meagre, and each countable union of meagre sets is meagre.
The set $\mathbb{Q}$ is meagre in $\mathbb{R}$, because it is a countable union of one-point sets.
By the [[Baire category theorem|0A7KGAYHGV]], $\mathbb{R}$ itself is not meagre in $\mathbb{R}$.

## Explanations

### L1 human

A meagre set is made of countably many thin pieces.
It can still be dense, as $\mathbb{Q}$ is, but in a complete metric space it can never fill an open set.
