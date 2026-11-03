---
tag: 129CMCWCAG
kind: concept
name: Olami–Feder–Christensen model
msc: [86A15, 82C22, 37B15]
specializes: [5QXNC6NTVN]
sources:
  - url: https://en.wikipedia.org/wiki/Olami%E2%80%93Feder%E2%80%93Christensen_model
same_as:
  wikidata: Q3556930
  wikipedia: Olami–Feder–Christensen model
---

## Summary

The Olami–Feder–Christensen model is a lattice model of earthquakes.
Each site carries a stress that grows slowly and is partly passed to its neighbours when it reaches a threshold.
Its rule is a continuous-valued [[cellular automaton|5QXNC6NTVN]] that keeps only a fraction of the stress in each transfer, so the model is not conservative.
It was introduced by Zeev Olami, Hans Feder and Kim Christensen as a simplified spring-block model of a fault.
Its avalanche sizes follow a power law over a range of parameters, similar to the [[Gutenberg–Richter law|9ZEBGCR93V]].
So it is a basic test case for [[self-organized criticality|FVJ624HTV0]] without conservation.

## Explanations

### L1 human

Picture a square grid of blocks stuck to the ground and joined to their neighbours by springs, all pulled slowly by a moving plate.
The pull on every block grows at the same rate until one block slips.
When it slips, its force drops to zero and some of that force is pushed onto its four neighbours, which may then slip too, in a chain reaction.
Such a chain reaction is a model earthquake, and its size is the number of slips.
For example, if a site at threshold $1$ slips with transfer fraction $0.2$, each neighbour gets $0.2$ more, and only $0.8$ of the force stays in the system.
