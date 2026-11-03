---
tag: 4CK2GSRAGD
kind: concept
name: Reproducing kernel Hilbert space
msc: ["46E22"]
specializes: [HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space
same_as:
  wikidata: Q3345678
  wikipedia: Reproducing kernel Hilbert space
---

## Summary

A reproducing kernel Hilbert space is a [[Hilbert space|HM2HHE3J51]] of functions on a set $X$.
In it, evaluation at each point is a continuous linear functional.
By the [[Riesz representation theorem|TTC40N49M6]], evaluation at $x$ is the inner product with a function $k_x$, and $K(x, y) = k_y(x)$ is the reproducing kernel.
The kernel is a [[positive-definite kernel|SCMS389SBG]], and by the Moore–Aronszajn theorem each positive-definite kernel comes from exactly one such space.
These spaces appear in complex analysis, as Hardy and Bergman spaces, and in statistics and machine learning, through kernel methods.

## Explanations

### L1 human

In such a space, functions that are close in norm are also close at every single point.
The value of a function at a point can be read off by taking the inner product with one special function for that point.
A simple example: the vectors of $\C^n$, seen as functions on $\set{1, \dots, n}$, form such a space.
The special function for the point $i$ is the unit vector $e_i$.
