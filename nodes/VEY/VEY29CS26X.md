---
tag: VEY29CS26X
kind: concept
name: Wasserstein metric
msc: [49Q22, 60B10, 28A33]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
same_as:
  wikidata: Q768993
  wikipedia: Wasserstein metric
---

## Summary

The Wasserstein metric is a distance between [[probability measures|059TJN0NZ1]] on a [[metric space|0VKD1TP7F3]].
It is the least cost of moving one mass distribution onto the other.
The cost of moving a unit of mass is a power of the distance it travels.
It is the central distance of optimal transport, and it metrizes weak convergence together with convergence of moments.

## Explanations

### L1 human

Think of one measure as a pile of earth and the other as a hole of the same volume.
A transport plan says how much earth goes from each place to each other place.
The Wasserstein distance is the cheapest total cost of such a plan.
This is why the $1$-Wasserstein distance is also called the earth mover's distance.
For two point masses at $x$ and $y$, all the mass must travel from $x$ to $y$, so the distance is $d(x, y)$.
