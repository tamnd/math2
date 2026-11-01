---
tag: XM6DH57BWY
kind: concept
name: Equidistribution modulo one
msc: [11K06, 11J71]
sources:
  - url: https://en.wikipedia.org/wiki/Equidistributed_sequence
---

## Summary

A sequence of real numbers is equidistributed modulo one when its fractional parts fill the interval $[0, 1)$ evenly in the long run.
Each subinterval then receives a proportion of the terms equal to its length.
The notion connects Diophantine approximation, Fourier analysis and probability, and Weyl's criterion reduces it to estimates of [[exponential sums|97PBMQCPPM]].

## Explanations

### L1 human

Wrap the real line around a circle of length $1$, so that only the fractional part of a number matters.
Place the terms of a sequence on this circle one by one.
The sequence is equidistributed if, after many steps, every arc holds a share of the points equal to its length.
For example the multiples $n \sqrt{2}$ are equidistributed modulo one, while the multiples $n/2$ only visit the two points $0$ and $1/2$.
