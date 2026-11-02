---
tag: VBW2A4H6TD
kind: concept
name: Ancillary statistic
msc: [62B05]
specializes: [0Q5CG2NEQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Ancillary_statistic
same_as:
  wikidata: Q4753046
  wikipedia: Ancillary statistic
---

## Summary

An ancillary statistic is a [[statistic|0Q5CG2NEQ8]] whose distribution does not depend on the parameter.
On its own it carries no information about the parameter, yet it can tell how precise the data are.
Fisher proposed to condition inference on ancillary statistics, and [[Basu's theorem|6GATRFMJYY]] shows that they are independent of complete sufficient statistics.

## Explanations

### L1 human

Some features of the data do not depend on the quantity you want to learn.
For measurements with an unknown true value and known noise, the difference between two measurements does not depend on the true value.
Such a feature is ancillary: its distribution is known in advance.
It cannot tell you where the true value is, but it can tell you how spread out your data happened to be.
