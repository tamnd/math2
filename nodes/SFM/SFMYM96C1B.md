---
tag: SFMYM96C1B
kind: concept
name: Nondeterministic finite automaton
msc: [68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
same_as:
  wikidata: Q617295
  wikipedia: Nondeterministic finite automaton
---

## Summary

A nondeterministic finite automaton (NFA) is a finite automaton in which a state may have several transitions, or none, for the same input symbol.
It accepts a word when at least one of its possible runs on the word ends in an accepting state.
Every [[deterministic finite automaton|W65B6BKZRY]] is an NFA, and by the [[powerset construction|DDVYP8RNG8]] every NFA can be turned into a DFA that accepts the same language.
NFAs are often much smaller and easier to build than equivalent DFAs, for example when translating [[regular expressions|4DMYF2PR4Q]] into automata.

## Explanations

### L1 human

An NFA is like a maze in which some doors have the same label.
When you read a letter you may choose any door with that label, and you win if some sequence of choices leads to an accepting room.
For example, to accept the words over $\set{a, b}$ whose second-to-last letter is $a$, an NFA simply guesses when that letter arrives.
It needs only three states.
A DFA cannot guess, so it must remember the last two letters, and it needs four states.
