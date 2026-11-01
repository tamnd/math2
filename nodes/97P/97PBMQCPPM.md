---
tag: 97PBMQCPPM
kind: concept
name: Exponential sum
msc: [11L03, 11L07]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_sum
same_as:
  wikidata: Q4446020
  wikipedia: Exponential sum
---

## Summary

An exponential sum is a finite sum of numbers $e^{2\pi i f(n)}$ on the unit circle, where $f$ is a real function on the integers.
The trivial bound for such a sum is its number of terms, and the aim is to show cancellation, that is, a much smaller bound.
Such bounds are central in analytic number theory: they control [[equidistribution modulo one|XM6DH57BWY]], the zeros of zeta functions, and the circle method.
Weyl sums, [[Gauss sums|EQ6A3ZN48K]] and [[Kloosterman sums|E1SQWQ2PAV]] are important special cases.

## Explanations

### L1 human

Each term $e^{2\pi i f(n)}$ is a point on the unit circle, like an arrow of length $1$ pointing in the direction $f(n)$.
Adding the arrows is like a random walk: if the directions vary enough, the arrows cancel and the sum stays small.
For example, with $f(n) = n/4$, the arrows point to $i, -1, -i, 1$ and the sum of each block of four is $0$.
Showing that such cancellation happens is the main problem of the theory.
