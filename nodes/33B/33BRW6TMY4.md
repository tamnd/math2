---
tag: 33BRW6TMY4
kind: concept
name: POVM
msc: [81P15, 81P16, 46N50]
sources:
  - url: https://en.wikipedia.org/wiki/POVM
same_as:
  wikidata: Q907206
  wikipedia: POVM
---

## Summary

A POVM, or positive operator-valued measure, is the most general description of the outcome statistics of a quantum measurement.
It assigns to each set of outcomes a [[positive operator|77020CY5ZW]], and the operator of the set of all outcomes is the identity.
In a state $\rho$, the probability of a set of outcomes is the trace of $\rho$ times its operator.
It generalizes a [[projection-valued measure|ATGT25E5FF]], which describes the measurement of a self-adjoint [[observable|DF5RN297GE]].
By Naimark's dilation theorem, every POVM is a projective measurement on a larger system.

## Explanations

### L1 human

An ordinary quantum measurement splits the space into orthogonal pieces, one for each outcome.
A POVM relaxes this: each outcome gets a positive operator, called an effect, and the effects only have to add up to the identity.
This allows more outcomes than the dimension, and unsharp or noisy measurements.
For example, a qubit can be measured with three outcomes that correspond to three directions at $120^\circ$ to each other in a plane of the Bloch sphere.
