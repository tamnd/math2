---
tag: QG9QRZAFTG
kind: concept
name: Convergence along an ultrafilter
msc: [54A20, 40J05]
specializes: [F6QDHKE6J3]
sources:
  - url: https://en.wikipedia.org/wiki/Ultrafilter_on_a_set
---

## Summary

Convergence along an [[ultrafilter|J64Y3JC0RE]] is the [[filter limit|F6QDHKE6J3]] of a function along an ultrafilter.
Its key feature is that every function into a [[compact|0TVJZYB6SH]] space has such a limit, and the limit is unique when the space is [[Hausdorff|0S1FJ8VEX9]].
So every bounded real sequence has a limit along a fixed non-principal ultrafilter on $\N$, and this limit is linear and multiplicative.
Ultrafilter limits are used to build ultraproducts, Banach-limit-like functionals and the Stone–Čech compactification.

## Explanations

### L1 human

An ultrafilter on $\N$ decides, for every set of indices, whether it is "large" or "small", and exactly one of a set and its complement is large.
A sequence converges to $x$ along the ultrafilter if, for each small region around $x$, the indices whose terms land there form a large set.
Because the ultrafilter takes a side on every set, a bounded sequence always has such a limit.
For the sequence $1, 0, 1, 0, \dots$, indexed from $1$, the limit is $1$ if the set of odd indices is large and $0$ if the set of even indices is large.
