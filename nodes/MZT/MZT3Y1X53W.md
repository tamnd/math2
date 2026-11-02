---
tag: MZT3Y1X53W
kind: concept
name: Analytic continuation in several variables
msc: [32D05, 32A10]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_continuation
---

## Summary

Analytic continuation in several variables extends a [[holomorphic function|507C34W0ZT]] on an open set of $\C^n$ step by step through overlapping domains.
It generalises [[analytic continuation|0M3YQJ81NB]] in one variable, and by the identity theorem each step is unique.
As in one variable, continuation along different paths can lead to different values.
So the result lives on a domain spread over $\C^n$ rather than on a subset of $\C^n$.
Unlike in one variable, for $n \ge 2$ every holomorphic function on certain domains continues to a strictly larger domain.

## Explanations

### L1 human

Start with a holomorphic function on a small region and try to push it further, like extending a road piece by piece.
Each new piece is forced: there is only one holomorphic way to extend on an overlap.
In several variables something new happens: for some regions, such as a ball with a hole, every function can be extended across the hole.
For example, a holomorphic function on $\set{z \in \C^2 : 1 < \abs{z} < 2}$ always continues to the whole ball $\abs{z} < 2$.
