---
tag: VKETGMSX5H
kind: concept
name: Distributed source coding
msc: [94A29, 94A15]
sources:
  - url: https://en.wikipedia.org/wiki/Distributed_source_coding
same_as:
  wikidata: Q5283181
  wikipedia: Distributed source coding
---

## Summary

Distributed source coding is the compression of several correlated sources by encoders that cannot talk to each other, followed by one joint decoder.
The basic question is which combinations of rates allow the decoder to recover all sources.
The Slepian–Wolf theorem answers it for lossless recovery of two discrete sources.
Applications include sensor networks, where nearby sensors measure related quantities.

## Explanations

### L1 human

Two weather stations measure temperatures that are close to each other, and each sends its readings to a common centre.
The stations cannot compare notes before sending.
One might think each station must then send its readings in full.
Surprisingly, the total number of bits needed is the same as if one station knew the other's readings, as long as the centre decodes both together.
