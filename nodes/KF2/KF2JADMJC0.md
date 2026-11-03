---
tag: KF2JADMJC0
kind: concept
name: Linear bounded automaton
msc: [68Q45, 68Q04, 03D10]
specializes: [M7SDX137WE]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_bounded_automaton
same_as:
  wikidata: Q1149323
  wikipedia: Linear bounded automaton
---

## Summary

A linear bounded automaton is a nondeterministic [[Turing machine|758EYCN27B]] whose head never leaves the part of the tape that holds the input.
So it uses only an amount of memory proportional to the length of the input.
Linear bounded automata accept exactly the [[context-sensitive languages|NYJ7PD4025]].
Whether deterministic linear bounded automata accept the same languages as nondeterministic ones is an open question.

## Explanations

### L1 human

A linear bounded automaton is a computer that may only write on the paper on which the question was written.
It may read and overwrite these cells as often as it likes, and it may guess, but it gets no extra room.
Such a machine can check that a word has the form $a^n b^n c^n$ by crossing off one $a$, one $b$ and one $c$ in each pass.
Its limited memory means it can only reach finitely many situations on a given input, which makes its languages decidable.
