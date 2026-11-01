---
tag: 5JESM2ZN48
kind: concept
name: Spectral graph theory
msc: [05C50]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_graph_theory
same_as:
  wikidata: Q3180727
  wikipedia: Spectral graph theory
---

## Summary

Spectral graph theory studies a graph through the [[eigenvalues|0BQAA2BK3Q]] and eigenvectors of matrices attached to it, mainly the [[adjacency matrix|08B9CX109G]] and the [[Laplacian matrix|TN6M6DVZRP]].
These eigenvalues are invariants of the graph up to isomorphism, and many of them have combinatorial meaning.
For example, a finite graph is bipartite if and only if the spectrum of its adjacency matrix is symmetric about $0$.
Its number of connected components equals the multiplicity of the Laplacian eigenvalue $0$.
The [[Cheeger constant|Y7S6W12N64]] is controlled by the second Laplacian eigenvalue, which links the subject to [[expander graphs|DXJXVFV79H]].

## Explanations

### L1 human

A graph can be turned into a matrix, and a matrix has eigenvalues.
Spectral graph theory asks what these numbers tell us about the graph.
They detect, for example, whether the graph is connected, whether it is bipartite, and how hard it is to cut it into two large pieces.
They do not tell everything: the star with four leaves and the $4$-cycle together with an isolated vertex have the same adjacency eigenvalues $2, 0, 0, 0, -2$, but they are different graphs.
