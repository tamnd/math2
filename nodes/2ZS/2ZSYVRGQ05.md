---
tag: 2ZSYVRGQ05
kind: concept
name: Automata theory
msc: [68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Automata_theory
same_as:
  wikidata: Q214526
  wikipedia: Automata theory
---

## Summary

Automata theory is the part of the [[theory of computation|W0236NVT62]] that studies abstract machines, called automata, and the problems they can solve.
Its basic objects are [[finite-state machines|NDC0E9BZ94]], [[pushdown automata|8YEY51Q3B5]] and [[Turing machines|758EYCN27B]].
Each kind of machine recognizes a class of [[formal languages|5MFZ4VNY6D]], and these classes form the [[Chomsky hierarchy|V7HSWG6R5F]].
The theory underlies compilers, text search, hardware design and the verification of programs.

## Explanations

### L1 human

An automaton is an idealized machine that reads a string of symbols, one at a time, and changes its internal state as it reads.
At the end it answers yes or no, or it produces some output.
Automata theory asks which tasks such machines can do when their memory is limited in a given way.
For example, a machine with only two states can check whether a word has an even number of letters $a$.
But no machine with finitely many states can check whether a word has as many letters $a$ as letters $b$.
