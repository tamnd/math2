---
tag: W1MPPTS4ED
kind: concept
name: Raptor code
msc: [94B60, 68P30]
sources:
  - url: https://en.wikipedia.org/wiki/Raptor_code
same_as:
  wikidata: Q7294373
  wikipedia: Raptor code
---

## Summary

A Raptor code is a fountain code made of two layers.
The first is a fixed high-rate erasure code, the precode.
The second is a [[Luby transform code|6G24FVAKZX]] with a degree distribution of constant average degree.
The LT layer only needs to recover most of the intermediate symbols, and the precode fills in the rest.
This gives linear-time encoding and decoding, which plain LT codes cannot reach.
Shokrollahi introduced Raptor codes, and versions of them are standardized for multimedia broadcast and file delivery.

## Explanations

### L1 human

An LT code that must recover every input symbol needs some output symbols of high degree, which makes it slow.
A Raptor code first adds a little redundancy to the input with an ordinary erasure code.
Then it uses a cheap LT code that is allowed to leave a small fraction of symbols unknown.
The first code then recovers those missing symbols, just as it would recover erased symbols on a channel.
