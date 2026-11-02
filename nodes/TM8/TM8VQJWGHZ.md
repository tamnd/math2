---
tag: TM8VQJWGHZ
kind: concept
name: Boundary value problem
msc: [34B05, 34B15]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_value_problem
same_as:
  wikidata: Q1332643
  wikipedia: Boundary value problem
---

## Summary

A boundary value problem is a differential equation together with conditions on the solution at the boundary of the domain.
For an ordinary differential equation, these are conditions at both ends of an interval.
It differs from an [[initial value problem|0FXDW992DS]], where all conditions are given at one point.
A boundary value problem may have no solution, exactly one, or infinitely many, and the answer depends on the whole interval.
Such problems describe equilibria, such as a string fixed at both ends, and lead to eigenvalue problems and Sturm–Liouville theory.
See the [[definition|1HGGRS57KT]].

## Explanations

### L1 human

Imagine a rope tied to two posts.
Its shape is decided by conditions at both ends, not by where it starts and in which direction it points.
For $y'' + y = 0$ with $y(0) = 0$ and $y(\frac{\pi}{2}) = 1$, the only solution is $y = \sin x$.
With $y(0) = 0$ and $y(\pi) = 1$ instead there is no solution, since every solution with $y(0) = 0$ is $c \sin x$, which vanishes at $\pi$.
