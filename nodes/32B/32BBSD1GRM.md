---
tag: 32BBSD1GRM
kind: concept
name: Nicholson–Bailey model
msc: [92D25, 39A60, 92D40]
specializes: [1YEMFQ1H32]
sources:
  - url: https://en.wikipedia.org/wiki/Nicholson%E2%80%93Bailey_model
same_as:
  wikidata: Q15635269
  wikipedia: Nicholson–Bailey model
---

## Summary

The Nicholson–Bailey model is a discrete-time [[population model|1YEMFQ1H32]] for a host and a parasitoid.
An example is an insect and a wasp that lays its eggs in it.
It was proposed by Alexander Nicholson and Victor Bailey.
Its positive equilibrium is always unstable, and the populations oscillate with growing amplitude.
So the model is the starting point of many studies of what stabilises host–parasitoid systems.

## Explanations

### L1 human

Each year the hosts lay eggs, and the parasitoid wasps search for hosts to lay their own eggs in.
A host that is found produces wasps the next year instead of new hosts.
The model assumes that the wasps search at random, so the chance that a host escapes is $e^{-aP}$ when there are $P$ wasps.
The result is a pair of rules for the next year's numbers, and their numbers swing up and down more and more until one of them crashes.
