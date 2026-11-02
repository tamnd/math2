---
tag: Z5CCVBME2V
kind: concept
name: Oracle machine
msc: [03D10, 03D30]
specializes: [758EYCN27B]
sources:
  - url: https://en.wikipedia.org/wiki/Oracle_machine
same_as:
  wikidata: Q1143357
  wikipedia: Oracle machine
---

## Summary

An oracle machine is a [[Turing machine|758EYCN27B]] with an extra device, the oracle, that answers questions of the form "is $n$ in the set $O$?" in a single step.
The set $O$ can be any set of natural numbers, even an uncomputable one.
Oracle machines define relative computability: what can be computed if some set is given for free.
They are used to define Turing reduction, Turing degrees and the Turing jump.

## Explanations

### L1 human

An oracle machine is an ordinary computer program with a phone line to an all-knowing helper.
The helper knows one fixed set $O$ and answers only yes-or-no questions about it.
The program writes a number, calls the helper, and gets the answer immediately.
For example, with the set of halting programs as oracle, a program can decide whether any given program halts, which no ordinary program can do.
