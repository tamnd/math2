---
tag: 1WPX24AEAT
kind: concept
name: DFA minimization
msc: [68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/DFA_minimization
same_as:
  wikidata: Q5204896
  wikipedia: DFA minimization
---

## Summary

DFA minimization is the task of turning a [[deterministic finite automaton|W65B6BKZRY]] into an equivalent one with as few states as possible.
For every [[regular language|18WVBDCS38]] the minimal DFA is unique up to renaming of states, by the [[Myhill–Nerode theorem|96BRMR4P3N]].
It is computed by removing unreachable states and merging states that no input word can distinguish.
Minimal DFAs give a canonical form, so two regular languages are equal exactly when their minimal DFAs are the same up to renaming.

## Explanations

### L1 human

Different machines can accept the same language, and some of them waste states.
Two states are redundant if, from either of them, exactly the same words lead to acceptance.
Minimization merges such states until no two remaining states behave alike.
For example, take a DFA that tracks the number of $a$'s modulo $4$ and accepts when that number is even.
It can be shrunk to the two-state DFA that tracks the number modulo $2$.
