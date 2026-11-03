---
tag: VCTMYPDXPX
kind: concept
name: Fortuin–Kasteleyn random cluster model
msc: [82B20, 60K35, 82B43]
sources:
  - url: https://en.wikipedia.org/wiki/Random_cluster_model
same_as:
  wikidata: Q65067094
  wikipedia: Random cluster model
---

## Summary

The random cluster model is a probability measure on sets of edges of a graph with two parameters $p$ and $q$.
It weights each edge set by the usual [[percolation|BH7YPXCYDK]] weight times $q$ to the number of connected components.
For $q = 1$ it is Bernoulli bond percolation, and for integer $q \ge 2$ it is coupled with the $q$-state [[Potts model|5GY2J6ZGXJ]].
This puts percolation, the [[Ising model|R0KGM32QN6]] and the Potts models into one family and gives geometric tools for their phase transitions.

## Explanations

### L1 human

Open each edge of a graph at random, and look at the clusters that the open edges form.
In plain percolation the edges are independent.
In the random cluster model each configuration also gets a bonus factor $q$ for each cluster, so the edges are no longer independent.
For example, with $q = 2$ the clusters of the model carry the correlations of the Ising model: two spins are correlated exactly through being in the same cluster.
