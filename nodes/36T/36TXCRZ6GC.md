---
tag: 36TXCRZ6GC
kind: concept
name: Choquet integral
msc: ["28E10", 28A25]
sources:
  - url: https://en.wikipedia.org/wiki/Choquet_integral
same_as:
  wikidata: Q5104911
  wikipedia: Choquet integral
---

## Summary

The Choquet integral integrates a non-negative function against a [[fuzzy measure|CRFQEGJDA9]], which need not be additive.
It adds up the sizes of the level sets $\set{f \ge t}$ over all levels $t$, as in the [[layer cake representation|H78RXJC1K1]].
For an ordinary measure it agrees with the Lebesgue integral, but in general it is not additive in the function.
It is used in decision theory, where it models attitudes towards uncertainty, and in the theory of capacities.

## Explanations

### L1 human

To integrate a non-negative function, cut its graph into thin horizontal slices.
At height $t$, the slice covers the set where the function is at least $t$.
The Choquet integral measures each such set with the given set function and adds up the slices over all heights.
With a non-additive set function, two functions can each have integral zero while their sum has a positive integral.
