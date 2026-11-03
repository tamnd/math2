---
tag: V7HSWG6R5F
kind: concept
name: Chomsky hierarchy
msc: [68Q45, 68Q42, 03D05]
sources:
  - url: https://en.wikipedia.org/wiki/Chomsky_hierarchy
same_as:
  wikidata: Q190913
  wikipedia: Chomsky hierarchy
---

## Summary

The Chomsky hierarchy sorts [[formal grammars|DP1HXZGPCM]] into four types by the shape of their rules, and the languages they generate into four nested classes.
From the largest class to the smallest, these are the [[recursively enumerable languages|67R1A5Y54R]] (type 0) and the [[context-sensitive languages|NYJ7PD4025]] (type 1).
They are followed by the [[context-free languages|Q56EWEQYE2]] (type 2) and the [[regular languages|18WVBDCS38]] (type 3).
Each class matches a kind of machine: [[Turing machines|758EYCN27B]], [[linear bounded automata|KF2JADMJC0]], [[pushdown automata|8YEY51Q3B5]] and [[finite automata|W65B6BKZRY]].
All the inclusions between consecutive classes are strict.

## Explanations

### L1 human

The hierarchy is a ladder of four kinds of grammars, from very restricted to completely free.
Each step up allows more complicated rules and produces more languages.
Each step also matches a machine with more memory.
The machines have only a fixed number of states, then a stack, then a tape as long as the input, then an unlimited tape.
For example, $a^n b^n$ needs the stack, and $a^n b^n c^n$ needs a tape as long as the input.
