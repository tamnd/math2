---
tag: Y1EGR8DF84
kind: concept
name: Liouville property of graphs
msc: [31C20, 05C81]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
---

## Summary

A graph has the Liouville property if every bounded [[discrete harmonic function|WRY0M7SW59]] on it is constant.
The name comes from Liouville's theorem, whose harmonic form says that bounded harmonic functions on $\R^n$ are constant.
The lattices $\Z^d$ have the property, while regular trees of degree at least $3$ do not.
For Cayley graphs of groups it says that the [[Poisson boundary|6EEF2E8XPF]] of the simple random walk is trivial.

## Explanations

### L1 human

A harmonic function on a graph gives each vertex the average of the values at its neighbours.
On a graph with the Liouville property, the only way to do this with values that stay bounded is to use the same value everywhere.
On the integers, the harmonic functions are the lines $an + b$, and only the constant ones are bounded.
On a tree that branches into two or more new directions at every vertex, a random walk drifts off along one branch.
The probability of ending up in a fixed branch is then a bounded harmonic function that is not constant.
