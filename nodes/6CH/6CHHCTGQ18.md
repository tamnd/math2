---
tag: 6CHHCTGQ18
kind: concept
name: False discovery rate and the Benjamini–Hochberg procedure
msc: [62J15]
sources:
  - url: https://en.wikipedia.org/wiki/False_discovery_rate
same_as:
  wikidata: Q5432696
  wikipedia: False discovery rate
---

## Summary

The false discovery rate of a multiple testing procedure is the expected proportion of false rejections among all rejections.
Controlling it is less strict than controlling the [[family-wise error rate|GQCY1N8JZT]], so it allows more discoveries when many hypotheses are tested.
The Benjamini–Hochberg procedure is a simple step-up rule on the ordered [[p-values|0GGKJGZF6D]] that controls the false discovery rate under independence.

## Explanations

### L1 human

In a study with thousands of tests, such as gene screens, a few false alarms are acceptable if most discoveries are real.
The false discovery rate is the average fraction of false alarms in the list of discoveries.
The Benjamini–Hochberg procedure sorts the p-values and compares the $i$-th smallest with $i q/m$.
It rejects all hypotheses up to the last p-value below its threshold.
With $q = 0.1$, on average at most about one discovery in ten is false.
