---
tag: N05WC9ZCWA
kind: concept
name: Displacement convexity
msc: [49Q22, 52A41, 35K55]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
---

## Summary

A functional on probability measures is displacement convex if it is convex along the paths of optimal transport, rather than along straight-line mixtures of measures.
Robert McCann introduced the notion in 1997, and used it to prove uniqueness of minimizers for energies that are not convex in the usual sense.
In the language of the [[Wasserstein distance|VEY29CS26X]], displacement convexity is convexity along geodesics.
Key examples are potential energies with a convex potential, interaction energies with a convex kernel, and the entropy $\int \rho \log \rho$.

## Explanations

### L1 human

There are two ways to go from one cloud of sand to another.
One can fade the first cloud out while fading the second in, or one can move each grain along a straight line to its destination.
Displacement convexity asks for convexity along the second kind of path.
For example, measure the height of each grain by a bowl-shaped function and take the average.
This average is convex along such paths, since each grain moves on a straight line inside the bowl.
