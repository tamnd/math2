---
tag: QV27JTGWQ0
kind: concept
name: L-system
msc: [68Q42, 92C80, 92C15]
sources:
  - url: https://en.wikipedia.org/wiki/L-system
same_as:
  wikidata: Q1151098
  wikipedia: L-system
---

## Summary

An L-system, or Lindenmayer system, is a string rewriting system in which every letter of a word is replaced at the same time.
Aristid Lindenmayer introduced it in 1968 to model the growth of simple multicellular organisms such as algae.
Repeated rewriting produces longer and longer words, which can be drawn as branching plants and fractal curves.
A [[formal grammar|DP1HXZGPCM]] in the sense of Chomsky rewrites one symbol at a time.
An L-system instead rewrites in parallel, like cells that all divide at once.

## Explanations

### L1 human

Start with a short word and a list of rules, such as "replace A by AB and B by A".
At each step apply the rule to every letter at once.
From A one gets AB, then ABA, then ABAAB, then ABAABABA.
The lengths are $1, 2, 3, 5, 8$, the [[Fibonacci numbers|0GA9K57A39]].
If the letters are read as drawing commands, such as "draw forward" and "turn left", the words draw pictures that look like ferns and trees.
