---
tag: A1XE59ZHNM
kind: concept
name: Shift space
msc: [37B10]
sources:
  - url: https://en.wikipedia.org/wiki/Shift_space
same_as:
  wikidata: Q7496253
  wikipedia: Shift space
---

## Summary

A shift space, or subshift, is a closed set of infinite sequences over a finite alphabet that is invariant under the shift by one place.
Equivalently, it is the set of all sequences that avoid a given list of forbidden finite words.
Shift spaces with the shift map are the objects of symbolic dynamics, and they serve as models for coding more general dynamical systems.
The full shift, the [[subshifts of finite type|624XDXX8FN]] and the sofic shifts are the main classes.

## Explanations

### L1 human

Take an alphabet such as $\set{0, 1}$ and consider infinite words in it.
Forbid some finite patterns, for example the pattern $11$.
The set of all infinite words that never contain a forbidden pattern is a shift space: here, the words in which no two $1$s are adjacent.
Shifting such a word by one place gives again such a word, so the set is mapped to itself by the shift.
Shift spaces are the simplest systems in which complicated dynamics can be described exactly.
