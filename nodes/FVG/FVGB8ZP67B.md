---
tag: FVGB8ZP67B
kind: concept
name: Topology of pointwise convergence
msc: [54C35, 54B10]
specializes: [1NWC3710WW]
sources:
  - url: https://en.wikipedia.org/wiki/Pointwise_convergence
---

## Summary

The topology of pointwise convergence lives on a set of functions from a set $X$ to a space $Y$.
In it, convergence means [[pointwise convergence|0GFGK40582]].
It is the [[product topology|0GBG8B49AA]] on $Y^X$, or its restriction to a subset such as the continuous maps.
It is coarser than the [[topology of uniform convergence|YW5P7NEKR4]] and than the [[compact-open topology|RG15F0TWPW]].

## Explanations

### L1 human

Think of a function $f \colon X \to Y$ as a long list of values, one value for each point $x$.
Two functions are close in this topology when they are close at finitely many chosen points.
Nothing is asked at the other points.
For example, the functions $f_n(x) = x^n$ on $[0, 1]$ converge in this topology to the function that is $0$ on $[0, 1)$ and $1$ at $x = 1$.
They do not converge uniformly.
