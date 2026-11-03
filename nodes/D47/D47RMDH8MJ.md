---
tag: D47RMDH8MJ
kind: concept
name: Syntactic monoid
msc: [20M35, 68Q70]
sources:
  - url: https://en.wikipedia.org/wiki/Syntactic_monoid
same_as:
  wikidata: Q3321297
  wikipedia: Syntactic monoid
---

## Summary

The syntactic monoid of a [[formal language|5MFZ4VNY6D]] $L$ is a quotient of the [[free monoid|CV013KHVJG]] of all words.
One divides by the coarsest [[congruence|DCSXXT4SER]] that does not mix words of $L$ with words outside $L$.
It is the smallest [[monoid|0N6R902FG1]] that recognizes $L$.
A language is [[regular|18WVBDCS38]] exactly when its syntactic monoid is finite.
Algebraic properties of this monoid classify regular languages; for instance [[Schützenberger's theorem|YSXPVN8G0D]] characterizes the [[star-free languages|K83HS1C5WG]] by it.

## Explanations

### L1 human

Two words are syntactically equivalent for a language when they can replace each other inside any context without changing membership in the language.
The classes of this relation can be multiplied by concatenating representatives, and they form a monoid.
For the words over $\set{a}$ with an even number of $a$'s, only the parity of a word matters, so the syntactic monoid is the group $\Z/2\Z$ with two elements.
In general, the syntactic monoid records how words act on the states of the minimal automaton.
