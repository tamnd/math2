---
tag: PA4PYQ1PZ0
kind: concept
name: Turing reduction
msc: [03D30]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_reduction
same_as:
  wikidata: Q4489310
  wikipedia: Turing reduction
---

## Summary

A set $A$ is Turing reducible to a set $B$ if some [[oracle machine|Z5CCVBME2V]] decides membership in $A$ by asking questions about $B$.
It is the most general notion of "$A$ is computable from $B$" in computability theory.
Turing reducibility is the basis of Turing degrees, which measure the amount of uncomputability of a set.

## Explanations

### L1 human

Imagine a computer that has a magic helper: whenever it asks "is this number in $B$?", the helper answers at once.
If such a computer can always decide whether a number lies in $A$, then $A$ is Turing reducible to $B$.
The computer may ask many questions, and later questions may depend on earlier answers.
For example, the complement of a set $B$ is Turing reducible to $B$: ask whether $x \in B$ and flip the answer.
This is more freedom than a [[many-one reduction|JTAH37JTHD]], which asks only one question and must copy its answer.
