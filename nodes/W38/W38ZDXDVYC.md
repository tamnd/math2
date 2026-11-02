---
tag: W38ZDXDVYC
kind: concept
name: Gelfand pair
msc: [43A90, 22D10, 43A85]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand_pair
same_as:
  wikidata: Q5530423
  wikipedia: Gelfand pair
---

## Summary

A Gelfand pair is a [[locally compact group|AHV05ZBCYW]] $G$ with a compact subgroup $K$ such that convolution of $K$-bi-invariant functions on $G$ is commutative.
Equivalently, each irreducible unitary representation of $G$ has at most a one-dimensional space of $K$-fixed vectors.
For a Gelfand pair, harmonic analysis on the homogeneous space $G/K$ is governed by [[spherical functions|BKZNC76RC8]].
They play the role of the exponentials in Fourier analysis.
Examples are $(\mathrm{SO}(3), \mathrm{SO}(2))$, related to the sphere, and $(\mathrm{SL}_2(\R), \mathrm{SO}(2))$, related to the hyperbolic plane.

## Explanations

### L1 human

Think of functions on the sphere that only depend on the latitude.
They can be seen as functions on the rotation group that do not change under rotations around the north pole, on either side.
For such functions, convolution does not depend on the order of the factors.
This commutativity makes their analysis almost as simple as Fourier series.
A group with a subgroup that behaves like this is called a Gelfand pair.
The pair of all rotations and the rotations around one axis is the main example.
