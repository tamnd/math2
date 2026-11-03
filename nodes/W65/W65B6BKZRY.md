---
tag: W65B6BKZRY
kind: concept
name: Deterministic finite automaton
msc: [68Q45]
specializes: [NDC0E9BZ94]
sources:
  - url: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
same_as:
  wikidata: Q837528
  wikipedia: Deterministic finite automaton
---

## Summary

A deterministic finite automaton (DFA) is a [[finite-state machine|NDC0E9BZ94]] with a set of accepting states.
It reads a word symbol by symbol, follows one transition per symbol, and accepts the word when it ends in an accepting state.
The languages accepted by DFAs are exactly the [[regular languages|18WVBDCS38]].
DFAs are used in lexical analysis, text search and the design of digital circuits.

## Explanations

### L1 human

A DFA is a finite diagram of circles (states) and arrows (transitions), each arrow labelled by a letter.
From each state there is exactly one arrow for each letter, so the path for a word is fully determined.
Some circles are marked as accepting.
For example, take two states "even" and "odd", and switch state on each letter $a$.
If "even" is both the start and the accepting state, this DFA accepts exactly the words with an even number of $a$'s.
