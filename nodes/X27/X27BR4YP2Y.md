---
tag: X27BR4YP2Y
kind: concept
name: Bisimulation
msc: [68Q85, 68Q55, 03B45]
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
same_as:
  wikidata: Q866364
  wikipedia: Bisimulation
---

## Summary

A bisimulation is a [[binary relation|05AVARPXA2]] between states of labelled transition systems.
Related states can match each other's moves step by step, forever.
Two states are bisimilar when some bisimulation relates them.
Bisimilarity is the standard notion of behavioural equivalence for concurrent systems and [[process calculi|1CQRPEWCFD]].
It is finer than equality of the sets of traces, and it is exactly the equivalence that [[modal logic|C3RZY20ETK]] cannot tell apart on image-finite systems.

## Explanations

### L1 human

Think of two machines with buttons labelled by actions.
They are bisimilar when, whatever button you press on one, the other can respond with the same button and land in a state that is again equivalent, and vice versa.
The game never ends, so the match must hold at every future step.
For example, a single state with an $a$-loop is bisimilar to a cycle of two states joined by $a$-steps: both can do $a$ forever and nothing else.
