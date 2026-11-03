---
tag: 4A2BAEWRPZ
kind: concept
name: Brzozowski derivative
msc: [68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Brzozowski_derivative
same_as:
  wikidata: Q17005656
  wikipedia: Brzozowski derivative
---

## Summary

The Brzozowski derivative of a [[formal language|5MFZ4VNY6D]] $L$ by a word $u$ is the set of words $v$ with $uv$ in $L$.
For a [[regular expression|4DMYF2PR4Q]] it can be computed symbolically, by simple rules on the structure of the expression.
Testing whether a word belongs to a language then reduces to repeated derivation followed by a check for the empty word.
Derivatives give a direct way to build a [[deterministic finite automaton|W65B6BKZRY]] from a regular expression, and they are closely tied to the [[Myhill–Nerode theorem|96BRMR4P3N]].

## Explanations

### L1 human

The derivative of a language by a letter $a$ answers the question: if a word starts with $a$, what may follow?
For the language $\set{ab, ac, bc}$, the derivative by $a$ is $\set{b, c}$ and the derivative by $c$ is empty.
Reading a word letter by letter and taking derivatives step by step, the word belongs to the language exactly when the final derivative contains the empty word.
For regular languages, only finitely many different derivatives occur, and they serve as the states of an automaton.
