---
tag: 8FRWATNNMX
kind: concept
name: Logarithmically convex function
msc: [26A51]
specializes: [07Q7CNM5WF]
sources:
  - url: https://en.wikipedia.org/wiki/Logarithmically_convex_function
same_as:
  wikidata: Q3610230
  wikipedia: Logarithmically convex function
---

## Summary

A logarithmically convex function is a positive function whose logarithm is a [[convex function|07Q7CNM5WF]].
Every such function is itself convex, but the converse fails.
The best known example is the [[gamma function|0H5SYBSED9]] on the positive reals, and log-convexity is the key hypothesis of the [[Bohr–Mollerup theorem|QFF87AXWN2]].
The [[definition|E97P413DKM]] gives the precise condition.

## Explanations

### L1 human

Take a positive function and look at the graph of its logarithm.
If that graph bends upward everywhere, the function is log-convex.
This is a strong form of convexity: between any two points, the graph lies below the exponential curve through the two end points.
For example $e^{x^2}$ is log-convex, since its logarithm is $x^2$.
The function $x^2$ on $(0, \infty)$ is convex but not log-convex, since its logarithm $2 \ln x$ bends downward.
