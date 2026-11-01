---
tag: A72XTVF2GK
kind: concept
name: Schur-convex function
msc: [26B25, 26D15]
sources:
  - url: https://en.wikipedia.org/wiki/Schur-convex_function
same_as:
  wikidata: Q7433030
  wikipedia: Schur-convex function
---

## Summary

A Schur-convex function is a function of $n$ real variables that preserves the order of [[majorization|5K7VT2VKZT]].
If $x$ is more spread out than $y$ and has the same sum, then $f(x) \ge f(y)$ for a Schur-convex $f$.
Every symmetric convex function is Schur-convex, and many classical inequalities, such as [[Karamata's inequality|FWKSHEJ9RP]], are statements that some function is Schur-convex.
The [[definition|24CEMRAGJ8]] gives the precise condition.

## Explanations

### L1 human

Think of a vector of $n$ numbers as a way to share a fixed total among $n$ people.
One sharing majorizes another when it is less equal.
A Schur-convex function measures inequality: it grows when the sharing becomes less equal.
For example the largest entry $\max_i x_i$ is Schur-convex: $(3, 0)$ is less equal than $(2, 1)$, and $3 \ge 2$.
