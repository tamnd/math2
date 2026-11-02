---
tag: HQVXKEMN5N
kind: concept
name: Distribution function of a measurable function
msc: [28A20, "46E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Layer_cake_representation
---

## Summary

The distribution function of a measurable function $f$ records, for each level $t \ge 0$, the measure of the set where $\abs{f}$ is larger than $t$.
It forgets where the large values of $f$ sit and keeps only how much room they take.
Many quantities, such as the $L^p$ norms, depend on $f$ only through its distribution function.
It is the starting point for the layer cake formula, rearrangements, weak $L^p$ spaces and interpolation.

## Explanations

### L1 human

Think of the graph of $\abs{f}$ as a mountain range and of $t$ as the height of a flood.
The distribution function at $t$ is the total length, area or volume of the land that stays above the water.
As the water rises, this amount can only shrink.
For example, for $f(x) = x$ on $[0, 1]$ with length as the measure, the set where $f > t$ is $(t, 1]$, so the distribution function is $1 - t$ for $0 \le t \le 1$ and $0$ for $t \ge 1$.
