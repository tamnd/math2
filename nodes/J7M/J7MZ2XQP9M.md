---
tag: J7MZ2XQP9M
kind: concept
name: Channel capacity
msc: [94A40, 94A24, 94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Channel_capacity
same_as:
  wikidata: Q870845
  wikipedia: Channel capacity
---

## Summary

The capacity of a communication channel is the highest rate at which information can cross it with arbitrarily small error probability.
It is measured in bits per channel use.
Shannon showed that it equals the largest mutual information between the input and the output, over all input distributions.
This turns an engineering limit into a computable quantity.
The [[capacity of a quantum channel|JYHQQGGZJZ]] is the analogue for quantum channels.

## Explanations

### L1 human

Every channel has a speed limit for reliable communication.
Below the limit, clever coding makes errors as rare as one wants; above it, errors cannot be avoided.
A channel that flips each bit with probability $0.1$ has capacity about $0.53$ bits per use.
So about $53$ useful bits can pass reliably for every $100$ bits sent, when long codes are used.
