---
tag: 4YQ8JYXBKK
kind: concept
name: Starred transform
msc: [44A55, 93C57, 44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Starred_transform
same_as:
  wikidata: Q7601294
  wikipedia: Starred transform
---

## Summary

The starred transform is the [[Laplace transform|0V49JEZW06]] of the impulse-sampled version of a continuous-time signal.
For a sampling period $T$ it equals $X^*(s) = \sum_{n \ge 0} x(nT) e^{-nTs}$.
It is the [[Z-transform|5FY0JQGHYZ]] of the samples with $z = e^{sT}$, and so it links the continuous-time analysis of a system with its discrete-time model.
It is used in the theory of sampled-data control systems.

## Explanations

### L1 human

A digital controller sees a continuous signal only at the instants $0, T, 2T, \ldots$.
One models this by a train of spikes at those instants, each spike weighted by the value of the signal there.
The starred transform is the Laplace transform of that spike train.
For $x(t) = 1$ it is $\sum_{n \ge 0} e^{-nTs} = 1/(1 - e^{-Ts})$ for $\operatorname{Re} s > 0$.
