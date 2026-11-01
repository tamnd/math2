---
tag: TNT3DG0HRJ
kind: concept
name: Random graph
msc: [05C80, 60C05]
sources:
  - url: https://en.wikipedia.org/wiki/Random_graph
same_as:
  wikidata: Q910404
  wikipedia: Random graph
---

## Summary

A random graph is a graph chosen at random according to a probability distribution on a set of graphs.
The most studied model is the [[Erdős–Rényi model|6E83YKANV3]] $G(n, p)$, in which each possible edge on $n$ labelled vertices is present independently with probability $p$.
One studies which properties hold with probability tending to $1$ as $n$ grows.
There are sharp thresholds, for example for connectivity and for the appearance of a giant component.
Random graphs are a main tool of the [[probabilistic method|3B55HNS754]] and a model for large real networks.

## Explanations

### L1 human

Take $n$ dots and, for each pair of dots, flip a coin to decide whether to draw a line between them.
The result is a random graph.
Typical questions are: how likely is the graph to be connected, or to contain a triangle, when $n$ is large?
Often the answer jumps from almost never to almost always as the probability of each edge passes a critical value.
