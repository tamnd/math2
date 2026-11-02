---
tag: 60P2XWY5QX
kind: concept
name: Turing jump
msc: [03D28, 03D30]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_jump
same_as:
  wikidata: Q6128725
  wikipedia: Turing jump
---

## Summary

The Turing jump of a set $A$ of natural numbers is the halting problem for [[oracle machines|Z5CCVBME2V]] with oracle $A$.
It produces from $A$ a set $A'$ that is strictly harder than $A$ in the sense of [[Turing reducibility|PA4PYQ1PZ0]].
Iterating the jump starting from the empty set gives the sets $\emptyset', \emptyset'', \ldots$, which line up with the levels of the [[arithmetical hierarchy|7CVJCQKY41]].

## Explanations

### L1 human

Give a computer access to a set $A$ as an oracle.
Even then it cannot decide which of its own programs halt; that question is the jump $A'$.
So each set leads to a harder one, and there is no hardest set.
For the empty set, which gives the computer no help at all, the jump is the ordinary [[halting problem|Z7TN2B35B0]].
