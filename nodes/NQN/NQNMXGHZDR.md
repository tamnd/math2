---
tag: NQNMXGHZDR
kind: concept
name: Supervisory control theory of discrete event systems
msc: [93C65, 68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Supervisory_control_theory
same_as:
  wikidata: Q7644327
  wikipedia: Supervisory control theory
---

## Summary

Supervisory control theory studies systems whose behaviour is a sequence of discrete events, such as a machine that starts, finishes or breaks down.
The uncontrolled system, the plant, is modelled by an automaton whose [[formal language|5MFZ4VNY6D]] lists the possible event sequences.
A supervisor watches the events and, after each sequence, disables some of the controllable events.
Its aim is that the closed loop only produces sequences allowed by a specification.
The central notion is the controllability of a language, which says exactly which specifications a supervisor can enforce.
The theory was introduced by Peter Ramadge and W. Murray Wonham in the 1980s.

## Explanations

### L1 human

Think of a factory as a game in which moves are events, some chosen by the operator and some, like breakdowns, chosen by nature.
A supervisor is a referee that, after looking at the moves so far, forbids some of the operator's moves.
It can never forbid nature's moves.
So a rule can be enforced only if no move of nature can break it on its own.
For example, no supervisor can enforce "the machine never breaks down", but one can enforce "the machine is never started while it is broken".
