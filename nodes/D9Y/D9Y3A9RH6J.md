---
tag: D9Y3A9RH6J
kind: concept
name: Cluster analysis
msc: [62H30]
sources:
  - url: https://en.wikipedia.org/wiki/Cluster_analysis
same_as:
  wikidata: Q622825
  wikipedia: Cluster analysis
---

## Summary

Cluster analysis groups a set of objects into clusters.
Objects in the same cluster should be more similar to each other than to objects in other clusters.
Unlike classification, it uses no labels known in advance.
Main families of methods are centroid methods such as [[k-means clustering|D5PN3G41D6]], hierarchical clustering, density-based methods and model-based clustering.
There is no single best notion of a cluster, and different methods can give different answers.

## Explanations

### L1 human

Throw a handful of coins on a table: you see them lying in a few heaps.
Cluster analysis tries to find such heaps in data, for instance groups of customers who buy similar things.
Nobody tells the method which group each object belongs to; it must discover the groups from the data alone.
A simple rule is to put points that are close to each other in the same group.
