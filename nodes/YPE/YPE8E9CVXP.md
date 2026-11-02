---
tag: YPE8E9CVXP
kind: concept
name: Affine arithmetic
msc: [65G30, 65G40]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_arithmetic
same_as:
  wikidata: Q3622729
  wikipedia: Affine arithmetic
---

## Summary

Affine arithmetic is a method of range analysis that represents each uncertain quantity as an affine function of shared noise symbols, each ranging over $[-1, 1]$.
Because quantities that depend on the same source of error share a noise symbol, their correlations are kept.
This avoids much of the overestimation of [[interval arithmetic|QPKKTE1ZY0]], where $x - x$ for $x \in [0, 1]$ gives $[-1, 1]$ instead of $0$.
Nonlinear operations are approximated by affine ones, and the approximation error becomes a new noise symbol, so the bounds remain guaranteed.

## Explanations

### L1 human

Suppose one only knows that a quantity $x$ lies between $1$ and $3$.
Interval arithmetic forgets where a range came from, so it treats $x$ and a second copy of $x$ as unrelated, and $x - x$ seems to lie anywhere between $-2$ and $2$.
Affine arithmetic writes $x = 2 + \varepsilon$ with an unknown $\varepsilon \in [-1, 1]$, and keeps the same $\varepsilon$ wherever $x$ appears.
Then $x - x = 0$ exactly, and sums such as $x + 2x = 6 + 3\varepsilon$ also come out sharp.
