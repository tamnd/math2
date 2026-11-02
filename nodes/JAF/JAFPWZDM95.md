---
tag: JAFPWZDM95
kind: concept
name: Isotonic regression
msc: [62G08, 62G05]
sources:
  - url: https://en.wikipedia.org/wiki/Isotonic_regression
same_as:
  wikidata: Q3455874
  wikipedia: Isotonic regression
---

## Summary

Isotonic regression fits a non-decreasing sequence to data by [[least squares|0BYTQ4X1HC]].
It is used when a response is known to increase with a covariate, as for dose and response.
No formula for the trend is assumed.
The fit is the projection of the data onto a closed convex cone, so it exists and is unique.
It can be computed quickly by the pool adjacent violators algorithm.

## Explanations

### L1 human

Suppose a measurement should grow with the dose, but noise makes some values go down.
Isotonic regression finds the staircase that never goes down and stays as close as possible to the data.
Whenever a value is higher than the next one, the two merge into a block that takes their average.
Blocks keep merging in this way until no drop remains.
For the data $1, 3, 2$, the drop from $3$ to $2$ is replaced by $2.5, 2.5$, giving $1, 2.5, 2.5$.
