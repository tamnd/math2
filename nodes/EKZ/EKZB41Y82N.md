---
tag: EKZB41Y82N
kind: concept
name: Neyman construction
msc: [62F25, 62F03]
sources:
  - url: https://en.wikipedia.org/wiki/Neyman_construction
same_as:
  wikidata: Q7021454
  wikipedia: Neyman construction
---

## Summary

The Neyman construction is a general method to build a [[confidence interval|0S6T9KQNC0]] for a parameter.
It starts from a family of acceptance regions, one for each value of the parameter.
The confidence set collects all parameter values whose acceptance region contains the observed data.
It is the inversion of a family of [[hypothesis tests|087P03NEND]], and it gives the required coverage without any pivot.

## Explanations

### L1 human

For each possible value of the parameter, draw a band of data values that are likely, with probability $1 - \alpha$, under that value.
After the experiment, keep every parameter value whose band contains what you saw.
Picture a plot with the parameter on one axis and the data on the other.
The bands form a belt, and the confidence interval is the slice of the belt at the observed data.
For a coin with unknown head probability $p$, the bands are ranges of head counts, and the slice gives an interval for $p$ with at least the required coverage.
