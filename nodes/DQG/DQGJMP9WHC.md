---
tag: DQGJMP9WHC
kind: concept
name: Contiguity of measures
msc: ["62E20", 60B10]
sources:
  - url: https://en.wikipedia.org/wiki/Contiguity_(probability_theory)
same_as:
  wikidata: Q5165214
  wikipedia: Contiguity (probability theory)
---

## Summary

Contiguity is an asymptotic form of absolute continuity for sequences of probability measures.
A sequence $(Q_n)$ is contiguous with respect to $(P_n)$ if every sequence of events whose $P_n$-probability tends to zero also has $Q_n$-probability tending to zero.
It was introduced by Lucien Le Cam.
It lets one transfer convergence in probability from a null hypothesis to nearby alternatives.
This is the basis of asymptotic power calculations and of local asymptotic theory.

## Explanations

### L1 human

Two sequences of probability models are contiguous if, as the sample grows, events that become impossible under one also become impossible under the other.
The models may differ, but never so much that the data could tell them apart with certainty.
For $n$ normal observations, a mean of $0$ and a mean of $1/\sqrt{n}$ stay contiguous, because the shift is of the size of the statistical noise.
A mean of $0$ and a mean of $1$ are not contiguous: with many observations one can tell them apart almost surely.
