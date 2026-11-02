---
tag: VY0HXD3GC4
kind: concept
name: Haar measure
msc: ["28C10", "22D05", "43A05"]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
same_as:
  wikidata: Q1162676
  wikipedia: Haar measure
---

## Summary

A Haar measure on a [[locally compact group|AHV05ZBCYW]] is a nonzero [[Radon measure|HZNEQQBCW4]] that does not change under left translation by elements of the group.
Every locally compact group has one, and it is unique up to a positive constant.
It extends Lebesgue measure on $\R^n$ and counting measure on discrete groups, and it is the basic tool for integration and harmonic analysis on groups.

## Explanations

### L1 human

On the real line, the length of an interval does not change when the interval is shifted.
A Haar measure is a way of assigning sizes to subsets of a group with the same property: moving a set by a group element keeps its size.
On the circle it is arc length, on a finite group it counts points, and on the positive reals under multiplication it is $dx/x$.
Indeed, the interval $[a, b]$ has measure $\log(b/a)$ for $dx/x$, and multiplying it by $c > 0$ gives $[ca, cb]$ with the same measure.
