---
tag: A5HTJ565DN
kind: concept
name: Ideal completion
msc: [06B23, 06B35]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_(order_theory)
---

## Summary

The ideal completion of a partially ordered set is the set of its order ideals, the nonempty directed down-closed subsets, ordered by inclusion.
Each element $x$ becomes the principal ideal of all elements below $x$.
The ideal completion is a [[directed-complete partial order|7TSXP95QN6]] in which every element is a directed union of principal ideals.
It is the free way to add suprema of directed sets.
It is a basic construction of [[domain theory|Q2P5D74Q1V]].

## Explanations

### L1 human

An order ideal is a set of elements that is closed downward and in which any two elements have a common bound inside the set.
Below each element $x$ there is the ideal of all elements below $x$, but there may be other ideals that do not have a top.
Adding these ideals as new elements fills in the missing limits of increasing sequences.
For the natural numbers, the only new ideal is $\N$ itself, so the completion is $\N$ with one point $\infty$ added on top.
