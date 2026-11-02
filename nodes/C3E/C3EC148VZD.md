---
tag: C3EC148VZD
kind: concept
name: Weak derivative
msc: ["46E35", 35D30, 46F10]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_derivative
same_as:
  wikidata: Q2143116
  wikipedia: Weak derivative
---

## Summary

A weak derivative of a locally integrable function is a function that obeys the integration by parts formula against all smooth compactly supported test functions.
It agrees with the usual [[partial derivative|09EGC6F8PT]] for continuously differentiable functions, but it also exists for many functions with corners.
Weak derivatives are used to define [[Sobolev spaces|M4CEZ5K9HP]] and weak solutions of partial differential equations.

## Explanations

### L1 human

For a smooth function $u$ and a test function $\varphi$ that vanishes near the ends of an interval, integration by parts gives $\int u \varphi' = -\int u' \varphi$.
The weak derivative turns this around: $v$ is called the derivative of $u$ if $\int u \varphi' = -\int v \varphi$ for every test function $\varphi$.
The function $\abs{x}$ has a corner at $0$ and no classical derivative there.
Its weak derivative is the sign function, which is $-1$ for $x < 0$ and $1$ for $x > 0$.
The value at the single point $0$ does not matter, since weak derivatives are only defined up to sets of measure zero.
