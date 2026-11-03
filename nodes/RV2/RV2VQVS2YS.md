---
tag: RV2VQVS2YS
kind: concept
name: BCJR algorithm
msc: [94B35, 94B10, 62M05]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/BCJR_algorithm
same_as:
  wikidata: Q625117
  wikipedia: BCJR algorithm
---

## Summary

The BCJR algorithm is named after Bahl, Cocke, Jelinek and Raviv.
It computes the [[posterior probability|0KJ7ZS8AJA]] of each state and each transition of a trellis, given all the received data.
It is the forward–backward algorithm applied to the trellis of a code, such as a [[convolutional code|JCFC831VS2]].
From these probabilities it gives, for each information bit, the decision with the smallest probability of error, and a soft reliability value.
These soft outputs are what makes iterative decoding of [[turbo codes|SGRYABP8D0]] work.

## Explanations

### L1 human

The [[Viterbi algorithm|356PTJ3R46]] answers "what is the single most likely path through the trellis?".
The BCJR algorithm answers "for each time, how likely is each state, given everything received?".
It runs one pass forward in time and one pass backward, and then combines them at each step.
The forward pass summarizes the past, the backward pass summarizes the future, and their product gives the full picture at each time.
