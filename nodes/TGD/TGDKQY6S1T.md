---
tag: TGDKQY6S1T
kind: concept
name: Register machine
msc: [68Q04, 03D10]
specializes: [YFHEG4GYHW]
sources:
  - url: https://en.wikipedia.org/wiki/Register_machine
same_as:
  wikidata: Q1930388
  wikipedia: Register machine
---

## Summary

A register machine is a [[model of computation|YFHEG4GYHW]] whose memory is a finite set of registers, each holding a natural number.
A program is a numbered list of simple instructions, such as adding one to a register or testing a register for zero.
The simplest kind, the counter machine, already computes every [[partial recursive function|HBK5QHC1GC]].
Register machines are closer to real computers than [[Turing machines|758EYCN27B]], and the [[random-access machine|2PQKV1KX24]] extends them.

## Explanations

### L1 human

Picture a few boxes, each holding a pile of pebbles.
The program can add a pebble to a box, or take one out if the box is not empty and jump elsewhere if it is.
That is all, yet such a machine can carry out any algorithm.
For example, to add two numbers, keep moving pebbles from the second box to the first until the second box is empty.
