---
tag: PPH99S8MKV
kind: concept
name: Blahut–Arimoto algorithm
msc: [94A40, 94A34, 94A24]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Blahut%E2%80%93Arimoto_algorithm
same_as:
  wikidata: Q4923900
  wikipedia: Blahut–Arimoto algorithm
---

## Summary

The Blahut–Arimoto algorithm computes the capacity of a discrete memoryless channel numerically.
A variant computes the rate–distortion function of a discrete source.
It alternates between two simple optimization steps, each solved in closed form, and the values converge to the optimum.
It was found independently by Richard Blahut and Suguru Arimoto in 1972.

## Explanations

### L1 human

The capacity of a channel is a maximum over all input distributions, and for most channels there is no formula for it.
The algorithm starts from some input distribution and improves it step by step.
At each step, input letters whose outputs are easy to tell apart from the average output get more weight.
For a symmetric channel such as the binary symmetric channel, the uniform input is already optimal and the algorithm stops changing at once.
