---
tag: X1D1C7VH6P
kind: concept
name: Kolmogorov–Sinai entropy
msc: [37A35, 28D20]
sources:
  - url: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system
---

## Summary

The Kolmogorov–Sinai entropy, or metric entropy, of a [[measure-preserving transformation|556WBDAHNP]] measures how much new information each step of the map produces.
It is defined from the Shannon entropy of finite partitions, refined along the orbit and taken per step.
It is an isomorphism invariant.
It tells apart systems with the same spectral data, such as two Bernoulli shifts whose probability vectors have different entropies.
By the [[Ornstein isomorphism theorem|8H4GF58E9M]] it is a complete invariant for Bernoulli shifts.

## Explanations

### L1 human

Watch a system through a coarse lens that only tells you in which of a few boxes the point is.
Record the sequence of boxes visited over many steps.
The entropy is the number of bits per step that you need, in the long run, to write down this record, for the best choice of boxes.
Tossing a fair coin produces $\log 2$ of entropy per step, one bit.
A rotation of a circle produces none, because after a while the past record predicts the future.
