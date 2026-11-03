---
tag: 92DM43HQZT
kind: concept
name: Büchi automaton
msc: [68Q45, 03D05]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%BCchi_automaton
same_as:
  wikidata: Q1020380
  wikipedia: Büchi automaton
---

## Summary

A Büchi automaton is a finite automaton that reads infinite words.
It accepts an infinite word when some run on it passes through an accepting state infinitely often.
Nondeterministic Büchi automata recognize exactly the [[omega-regular languages|G6WP8B6NGD]].
They are a main tool in model checking, where formulas of linear temporal logic are translated into them.
Unlike for finite words, deterministic Büchi automata are weaker than nondeterministic ones.

## Explanations

### L1 human

A Büchi automaton looks like an ordinary [[nondeterministic finite automaton|SFMYM96C1B]], but it never stops reading, because its input never ends.
Since there is no last state, acceptance asks instead that the run keeps coming back to an accepting state forever.
For example, with states "just read $a$" (accepting) and "just read $b$", the automaton accepts exactly the infinite words with infinitely many $a$'s.
Such conditions describe properties of systems that run forever, like "every request is eventually answered".
