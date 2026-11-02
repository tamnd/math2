---
tag: JDM2M1FRY6
kind: concept
name: Strongly measurable function
msc: [28B05, 46G10, 28A20]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner_measurable_function
same_as:
  wikidata: Q9392172
  wikipedia: Bochner measurable function
---

## Summary

A strongly measurable function is a function from a measurable space to a Banach space that is a pointwise limit of simple measurable functions.
It is the right notion of measurability for functions with values in an infinite-dimensional space.
The Bochner integral is built for strongly measurable functions, and the Pettis measurability theorem describes them through linear functionals.

## Explanations

### L1 human

A simple function takes only finitely many values, each on a measurable piece of the space.
A strongly measurable function is one that such simple functions can approximate as closely as one wants at every point.
For real-valued functions this is the same as ordinary measurability.
For example, a continuous function $f \colon [0, 1] \to E$ into a Banach space $E$ is strongly measurable.
To see it, cut $[0, 1]$ into $n$ intervals and take on each interval the value of $f$ at its left end.
These step functions converge to $f$ at every point as $n$ grows.
