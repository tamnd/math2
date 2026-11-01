---
tag: 6E83YKANV3
kind: concept
name: Erdős–Rényi model
msc: [05C80, 60C05]
specializes: [TNT3DG0HRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Erdős–Rényi_model
same_as:
  wikidata: Q605807
  wikipedia: Erdős–Rényi model
---

## Summary

The Erdős–Rényi model is the simplest model of a [[random graph|TNT3DG0HRJ]].
In the form $G(n, p)$, each of the $\binom{n}{2}$ possible edges on $n$ labelled vertices is present independently with probability $p$.
In the form $G(n, M)$, a graph with exactly $M$ edges is chosen uniformly at random.
The model shows sharp thresholds, such as the sudden appearance of a giant component, and it is a basic tool of the [[probabilistic method|3B55HNS754]].

## Explanations

### L1 human

Take $n$ dots and, for every pair of dots, flip a biased coin that shows heads with probability $p$.
Draw a line between the two dots exactly when the coin shows heads.
The picture you get is a random graph from $G(n, p)$.
For example, with $n = 3$ and $p = 1/2$, each of the $8$ graphs on the vertices $1, 2, 3$ appears with probability $1/8$.
When $p$ grows, the graph changes quickly from a few scattered edges to one large connected piece.
