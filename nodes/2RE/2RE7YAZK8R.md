---
tag: 2RE7YAZK8R
kind: concept
name: Ehrenfeucht–Fraïssé game
msc: [03C07, 03C13]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht–Fraïssé_game
same_as:
  wikidata: Q1300013
  wikipedia: Ehrenfeucht–Fraïssé game
---

## Summary

The Ehrenfeucht–Fraïssé game is a two-player game played on two [[structures|983GZBQYT4]] of the same signature.
One player, Spoiler, tries to show that the structures differ, and the other, Duplicator, tries to show that they look alike.
For a finite relational signature, Duplicator wins the $n$-round game exactly when the structures satisfy the same sentences of quantifier depth at most $n$.
The game is a main tool to prove that a property is not first-order definable, in particular in finite model theory.

## Explanations

### L1 human

In each round, Spoiler points at an element of one of the two structures, and Duplicator answers with an element of the other.
After all rounds, Duplicator wins if the chosen elements relate to each other in the same way on both sides.
On the linear orders with $3$ and $4$ elements, Duplicator wins the game with $2$ rounds.
Spoiler wins with $3$ rounds, so some first-order sentence with three nested quantifiers tells the two orders apart.
