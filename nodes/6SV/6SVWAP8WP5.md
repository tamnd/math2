---
tag: 6SVWAP8WP5
kind: concept
name: Descending chain condition
msc: [06A06, "13E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Ascending_chain_condition
---

## Summary

A partially ordered set satisfies the descending chain condition when every decreasing sequence of its elements is eventually constant.
It is the dual of the [[ascending chain condition|0GZ6Y1H4RN]].
Applied to the ideals of a ring, it defines [[Artinian rings|20QEAM8AX2]]; applied to submodules, it defines [[Artinian modules|YQNZTQGP1X]].
For posets it is equivalent, under the axiom of dependent choice, to being a [[well-founded order|55WD0H03CZ]].

## Explanations

### L1 human

Picture going down a staircase in a poset, one step at a time, never going back up.
The descending chain condition says that you must stop moving after finitely many real steps.
The natural numbers satisfy it, since you cannot go down from $10$ more than ten times.
The integers do not: $0 > -1 > -2 > \cdots$ goes down forever.
