---
tag: BDWD5J39DJ
kind: concept
name: Mealy machine
msc: [68Q45]
specializes: [NDC0E9BZ94]
sources:
  - url: https://en.wikipedia.org/wiki/Mealy_machine
same_as:
  wikidata: Q1126309
  wikipedia: Mealy machine
---

## Summary

A Mealy machine is a [[finite-state machine|NDC0E9BZ94]] that emits an output symbol on each transition, depending on the current state and the input symbol read.
It turns an input word into an output word of the same length.
Mealy machines model sequential circuits and controllers, where the output reacts at once to the input.
They compute the same input-output functions as [[Moore machines|6VAZ66YNCA]], up to a shift in time, and they are a special kind of [[finite-state transducer|SDJ23BAFF7]].

## Explanations

### L1 human

Picture a machine that reads a stream of bits and, after each bit, writes a bit of its own.
What it writes depends both on what it remembers, its state, and on the bit just read.
For example, a machine can write $1$ exactly when the bit just read equals the previous bit.
Its states only need to remember the last bit read, or that nothing has been read yet.
