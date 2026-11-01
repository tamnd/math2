---
tag: PHHT5W3BEJ
kind: concept
name: Regular conditional probability
msc: [60A10, 28A50]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_conditional_probability
same_as:
  wikidata: Q7309594
  wikipedia: Regular conditional probability
---

## Summary

A regular conditional probability is a version of conditional probability given a σ-algebra that is a genuine probability measure for each outcome.
Conditional probabilities $P(A \mid \mathcal{G})$ are defined one event at a time and only up to null sets.
So in general they need not fit together into a measure.
A regular version is a Markov kernel that does fit them together, and it lets one compute conditional expectations as integrals.
It exists when the underlying space is nice enough, for example a Polish space with its Borel σ-algebra.

## Explanations

### L1 human

Given some partial information, one wants a whole new probability law that describes the remaining uncertainty.
For a point $(x, y)$ chosen uniformly in the unit square, knowing $x$ leaves $y$ uniform on $[0, 1]$, and that uniform law is the regular conditional probability.
The difficulty is that the information may be an event of probability zero, like "$x = 0.3$".
A regular conditional probability fixes one law for each value of the information at once, so that all of them together reproduce the original probabilities.
The [[Borel–Kolmogorov paradox|9RMS0ZJ618]] shows why the family must be chosen together, not one null event at a time.
