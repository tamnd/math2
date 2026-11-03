---
tag: 6VAZ66YNCA
kind: concept
name: Moore machine
msc: [68Q45]
specializes: [NDC0E9BZ94]
sources:
  - url: https://en.wikipedia.org/wiki/Moore_machine
same_as:
  wikidata: Q640119
  wikipedia: Moore machine
---

## Summary

A Moore machine is a [[finite-state machine|NDC0E9BZ94]] whose output depends only on its current state.
Each state carries an output symbol, and the machine emits the symbol of every state it enters.
Moore machines model sequential circuits whose outputs change only when the state changes.
They compute the same input-output functions as [[Mealy machines|BDWD5J39DJ]] up to a shift in time, although a Moore machine may need more states.

## Explanations

### L1 human

A traffic light is a natural Moore machine: each state, such as "green" or "red", shows its own colour, whatever signal caused the change.
In a Moore machine the output is attached to the states, not to the arrows.
For example, a machine that reads bits and keeps the parity of the number of $1$'s can show "even" or "odd" as the output of its two states.
