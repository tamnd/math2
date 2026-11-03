---
tag: ZCFQEZ0A0V
kind: concept
name: Global optimization
msc: [90C26]
specializes: [W3ZXKT3DS1]
sources:
  - url: https://en.wikipedia.org/wiki/Global_optimization
same_as:
  wikidata: Q5570875
  wikipedia: Global optimization
---

## Summary

Global optimization is the part of optimization that seeks a global minimizer of a function over a set, not only a [[local minimum|09WRNGPTMV]].
For a convex problem every local minimizer is global, so the subject is about nonconvex problems with many local minima.
Deterministic methods, such as branch and bound with convex relaxations, can certify that a point is within a given tolerance of optimal.
Stochastic methods, such as simulated annealing and multistart, give no certificate but often work well in practice.

## Explanations

### L1 human

A mountain landscape has many valleys, and walking downhill from where you stand only finds the nearest one.
Global optimization asks for the deepest valley of the whole landscape.
For $f(x) = x^4 - 4x^2 + x$, there is a valley near $x \approx 1.35$ with height about $-2.6$, and a deeper one near $x \approx -1.47$ with height about $-5.4$.
A downhill walk started at $x = 1$ ends in the shallower valley.
