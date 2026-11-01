---
tag: WMB2MAEDX4
kind: concept
name: Sequential space
msc: [54D55]
specializes: [0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_space
same_as:
  wikidata: Q2740469
  wikipedia: Sequential space
---

## Summary

A sequential space is a topological space whose topology is determined by its convergent sequences.
A set is closed in it exactly when it contains the limits of all its convergent sequences.
Every [[first-countable space|0CP5NDD21C]], in particular every metric space, is sequential.
In a sequential space, sequences are enough to test closedness and continuity, so nets or filters are not needed.

## Explanations

### L1 human

In a metric space, you can decide whether a set is closed by checking sequences: a closed set keeps the limits of its sequences.
In a general space this test can fail, because sequences may be too short to reach some points.
Sequential spaces are the spaces where the sequence test still works.
For example, in $\R$ the set $(0, 1]$ is not closed, and the sequence $1/n$ in it shows this, because its limit $0$ is outside.
