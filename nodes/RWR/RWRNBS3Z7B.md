---
tag: RWRNBS3Z7B
kind: concept
name: Church–Turing thesis
msc: [03D10, 03D20, 03A05]
sources:
  - url: https://en.wikipedia.org/wiki/Church–Turing_thesis
same_as:
  wikidata: Q309157
  wikipedia: Church–Turing thesis
---

## Summary

The Church–Turing thesis is a claim about the informal notion of an algorithm.
It says that a function on the natural numbers can be calculated by an effective method exactly when a [[Turing machine|758EYCN27B]] computes it.
It is not a theorem, because "effective method" is an informal notion and cannot be the subject of a proof.
It is supported by the fact that all proposed formal models of computation define the same class of functions.
These models include [[general recursive functions|HBK5QHC1GC]], the [[lambda calculus|BD756KR8FM]] and Turing machines.
The thesis lets one prove that a problem has no algorithm at all by proving that no Turing machine solves it.

## Explanations

### L1 human

People computed with pencil and paper long before there were precise definitions of computation.
In the 1930s Alonzo Church and Alan Turing each proposed a precise definition, and these turned out to describe the same functions.
The thesis claims that these definitions capture everything that can be computed by following exact rules.
For example, when one shows that no Turing machine decides whether a program halts, the thesis lets one conclude that no algorithm of any kind does.
