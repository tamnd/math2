---
tag: 3SZESKX3N5
kind: concept
name: Total variation distance between probability measures
msc: [60B10, 62B10]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation_distance_of_probability_measures
same_as:
  wikidata: Q7828155
  wikipedia: Total variation distance of probability measures
---

## Summary

The total variation distance between two probability measures is the largest difference between the probabilities they give to the same event.
It is half the [[total variation|EPBND51CR5]] norm of their difference.
It is the natural distance for questions of distinguishing two distributions: it controls the best possible success probability of a test between them.

## Explanations

### L1 human

Two distributions are close in total variation if no event at all has very different chances under them.
For two coins with heads probabilities $p$ and $q$, the distance is $\abs{p - q}$.
For densities, it is half the area between the two density curves.
A distance of $0$ means the distributions are equal, and a distance of $1$ means they live on disjoint sets.
