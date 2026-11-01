---
tag: J5XQRP1SNQ
kind: concept
name: Automatic group
msc: [20F65, 20F10, 68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Automatic_group
same_as:
  wikidata: Q4826571
  wikipedia: Automatic group
---

## Summary

An automatic group is a finitely generated group whose elements can be named by words of a regular language.
The naming must allow finite automata to check when two named elements differ by a generator.
The idea comes from the work of Cannon, Epstein, Thurston and others on computing with groups.
Automatic groups are finitely presented, their word problem can be solved in quadratic time, and their [[Dehn function|Q4HGMRA9JQ]] is at most quadratic.
[[Hyperbolic groups|JWJ8YPR7EB]], $\Z^n$, braid groups and many [[Coxeter groups|G6FND7X69J]] are automatic.

## Explanations

### L1 human

A finite automaton is a machine with finitely many states that reads a word one letter at a time.
In an automatic group, such a machine can recognise a chosen list of normal-form words, one or more for each element.
Further machines, reading two words side by side, can tell whether the elements they name differ by one generator.
In $\Z^2$ with generators $a$ and $b$, the words $a^m b^n$ with $m, n \in \Z$ form such a list.
This makes many computations in the group fast and mechanical.
