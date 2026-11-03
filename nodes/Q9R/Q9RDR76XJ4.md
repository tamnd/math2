---
tag: Q9RDR76XJ4
kind: concept
name: BCM theory
msc: [92C20, 92B20, 68T05]
specializes: [VQZVSFF179]
sources:
  - url: https://en.wikipedia.org/wiki/BCM_theory
same_as:
  wikidata: Q4835208
  wikipedia: BCM theory
---

## Summary

BCM theory is a model of synaptic plasticity proposed by Elie Bienenstock, Leon Cooper and Paul Munro in 1982.
A synapse is strengthened when the postsynaptic activity is above a threshold and weakened when it is below.
The threshold itself slides with the recent average of the squared output, which keeps the weights stable.
It is a form of [[Hebbian learning|VQZVSFF179]] that explains how neurons in the visual cortex become selective to some inputs.

## Explanations

### L1 human

In plain Hebbian learning, activity together always means strengthening.
BCM adds a dividing line: strong responses strengthen the active inputs, weak responses weaken them.
If the neuron has been very active lately, the line moves up, so it becomes harder to strengthen further.
This feedback stops runaway growth and pushes the neuron to respond strongly to a few input patterns and weakly to the rest.
