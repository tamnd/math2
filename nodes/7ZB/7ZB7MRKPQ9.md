---
tag: 7ZB7MRKPQ9
kind: concept
name: Transformation semigroup
msc: [20M20]
specializes: [0XMEM406JM]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_semigroup
same_as:
  wikidata: Q3022116
  wikipedia: Transformation semigroup
---

## Summary

A transformation semigroup is a set of maps from a set $X$ to itself that is closed under [[composition|0THBK9V825]].
It is to [[semigroups|0XMEM406JM]] what a [[permutation group|ZDJQRKPWGA]] is to groups.
Every semigroup is isomorphic to a transformation semigroup, by an analogue of Cayley's theorem.
Transformation semigroups model the actions of finite automata, which is the starting point of [[Krohn–Rhodes theory|3WDZY1J002]].

## Explanations

### L1 human

Think of a machine with a finite set of states, and buttons that each move every state to some state.
Pressing buttons one after another composes these moves, and the set of all composite moves is a transformation semigroup.
Unlike the symmetries of a group, the moves need not be reversible: a reset button that sends every state to one start state loses information.
