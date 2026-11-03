---
tag: 4TA4GXQP6Q
kind: concept
name: Fast multipole method
msc: [65Y20, 78M16, 70F10]
sources:
  - url: https://en.wikipedia.org/wiki/Fast_multipole_method
same_as:
  wikidata: Q5437040
  wikipedia: Fast multipole method
---

## Summary

The fast multipole method computes all pairwise interactions among $N$ particles, such as gravitational or electrostatic potentials.
It needs $O(N)$ operations for a prescribed accuracy, instead of $O(N^2)$.
It groups the particles in a tree of boxes and replaces the field of each distant group by a truncated [[multipole expansion|KE84W5KNT8]].
It was introduced by Greengard and Rokhlin in 1987.
It speeds up [[n-body|62SNWC5E45]] simulations and the matrix-vector products of integral-equation solvers such as the [[method of moments|YXKZYG618P]].
It is also a model for [[hierarchical matrices|5P5EMYHXE5]].

## Explanations

### L1 human

Seen from far away, a cluster of stars pulls almost like a single star at its centre.
The fast multipole method uses this idea at all scales: it treats far clusters as a few numbers and only near neighbours one by one.
A second trick collects the influence of all far clusters into one smooth expansion around each box.
For a million particles this turns about $10^{12}$ pair computations into a number proportional to a million.
