---
tag: M7SDX137WE
kind: concept
name: Nondeterministic Turing machine
msc: [68Q10, 68Q04, 03D10]
specializes: [YFHEG4GYHW]
sources:
  - url: https://en.wikipedia.org/wiki/Nondeterministic_Turing_machine
same_as:
  wikidata: Q1190223
  wikipedia: Nondeterministic Turing machine
---

## Summary

A nondeterministic Turing machine is a [[Turing machine|758EYCN27B]] that may have several possible moves in a given situation.
It accepts an input when at least one of its possible runs reaches an accepting state.
It recognises the same languages as a deterministic machine, but its time cost can be much smaller.
The class NP consists of the problems that such a machine decides in polynomial time, which makes it central to the P versus NP question.

## Explanations

### L1 human

Imagine a maze explorer who, at every fork, splits into copies that try all branches at once.
The explorer succeeds if any copy finds the exit.
A nondeterministic machine works this way: it accepts if some sequence of choices leads to acceptance.
For example, to check whether a number is composite, it can guess a divisor and then verify the guess by one division.
A real computer has to try the choices one after another, which may take exponentially longer.
