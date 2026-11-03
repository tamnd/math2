---
tag: YFHEG4GYHW
kind: concept
name: Model of computation
msc: [68Q04, 03D10]
sources:
  - url: https://en.wikipedia.org/wiki/Model_of_computation
same_as:
  wikidata: Q2651576
  wikipedia: Model of computation
---

## Summary

A model of computation is a precise mathematical description of how a machine computes an output from an input.
It fixes the allowed basic steps and how they are combined, so that the cost of a computation can be measured.
Examples are the [[Turing machine|758EYCN27B]], the [[register machine|TGDKQY6S1T]], the [[random-access machine|2PQKV1KX24]], [[Boolean circuits|SQXNFGVADX]] and the [[lambda calculus|BD756KR8FM]].
Without such a model, statements like "no algorithm solves this problem" or "this needs quadratic time" have no exact meaning.

## Explanations

### L1 human

A recipe is only clear when one knows which kitchen actions are allowed.
A model of computation is the list of allowed actions for an algorithm.
For a Turing machine they are: read one symbol, write one symbol, move one cell, change state.
For a register machine they are: add one to a counter, subtract one, test a counter for zero.
Different models look very different, yet the usual ones can compute exactly the same functions.
