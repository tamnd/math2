---
tag: 72JCVFVP28
kind: concept
name: Felsenstein's pruning algorithm
msc: [92D15, 62P10]
sources:
  - url: https://en.wikipedia.org/wiki/Felsenstein%27s_tree-pruning_algorithm
same_as:
  wikidata: Q5442616
  wikipedia: Felsenstein's tree-pruning algorithm
---

## Summary

Felsenstein's pruning algorithm computes the [[likelihood|0VW9E4QXR6]] of a [[phylogenetic tree|RK58WSHJSG]] with branch lengths, given aligned sequences at its leaves and a [[substitution model|8FQFR871KM]].
It is a [[dynamic programming|R3FXF08WBH]] method that works from the leaves up to the root.
The likelihood is a sum over exponentially many assignments of states to the internal vertices.
The algorithm computes it at a cost that grows linearly with the number of vertices.
It is the core step of maximum likelihood and Bayesian phylogenetics.

## Explanations

### L1 human

The states of the ancestors in a tree are unknown, so the probability of the observed data is a sum over all possible ancestral states.
With $n$ internal vertices and four nucleotides, that sum has $4^n$ terms.
The pruning algorithm handles each subtree only once.
For each vertex and each letter, it stores the probability of the data below that vertex if the vertex had that letter.
These stored numbers for a vertex are computed from those of its children, so one pass from the leaves to the root gives the answer.
