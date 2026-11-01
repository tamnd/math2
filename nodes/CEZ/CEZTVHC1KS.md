---
tag: CEZTVHC1KS
kind: concept
name: Tietze transformations
msc: [20F05]
sources:
  - url: https://en.wikipedia.org/wiki/Tietze_transformations
same_as:
  wikidata: Q7801155
  wikipedia: Tietze transformations
---

## Summary

Tietze transformations are four elementary moves on a [[group presentation|0JGEQXQ4AC]] that do not change the group up to isomorphism.
They add or remove a redundant relation, or add or remove a redundant generator.
Two finite presentations define isomorphic groups if and only if one can pass from one to the other by finitely many such moves.
They are the basic tool to simplify presentations and to recognise when two presentations give the same group.

## Explanations

### L1 human

A presentation describes a group by letters and rules, and many different presentations describe the same group.
Tietze moves are the safe edits.
You may add a rule that already follows from the others, or delete such a rule.
You may introduce a new letter as an abbreviation for a word, or remove a letter that is only an abbreviation.
For example, $\langle a, b \mid b = a^2 \rangle$ becomes $\langle a \mid \ \rangle$ by removing the abbreviation $b$, so it is the infinite cyclic group.
