---
tag: NGHWZ9Y7ZV
kind: concept
name: Kripke semantics
msc: [03B45, 03B20]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
same_as:
  wikidata: Q2462350
  wikipedia: Kripke semantics
---

## Summary

Kripke semantics interprets [[modal logic|C3RZY20ETK]] in a set of possible worlds linked by an accessibility relation.
A formula $\square\varphi$ is true at a world when $\varphi$ is true at every world accessible from it.
Many modal logics are exactly the sets of formulas valid on a class of such frames.
A variant of the semantics also serves [[intuitionistic logic|Q11N8X99FK]].

## Explanations

### L1 human

Picture a set of points, the possible worlds, with arrows between some of them.
At each world, each basic statement is either true or false.
"Necessarily $p$" holds at a world when $p$ holds at every world that its arrows reach.
For example, with two worlds $u \to v$, where $p$ is true only at $v$, the formula $\square p$ holds at $u$, but $p$ itself does not.
