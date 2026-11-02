---
tag: 33C1KEK3SC
kind: concept
name: Outer regular measure
msc: [28C15]
specializes: [DYR1QFNGNJ]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_measure
---

## Summary

A measure on a topological space is outer regular when each measurable set is approximated from outside by open sets.
The measure of the set is the infimum of the measures of the open sets that contain it.
Lebesgue measure on $\R^n$ is outer regular, which is how it is often first constructed.
Outer regularity, together with inner regularity, is part of the usual definitions of a regular measure and of a Radon measure.

## Explanations

### L1 human

To measure a set, wrap it in open sets and shrink the wrapping.
If the wrappings can get as close to the set's measure as one likes, the measure is outer regular.
For length on the real line, a single point is covered by tiny open intervals of length as small as one likes, which matches its length $0$.
Counting measure fails: every open interval around a point contains infinitely many points.
