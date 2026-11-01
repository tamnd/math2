---
tag: QMJ5PNSF9X
kind: concept
name: Graphon
msc: [05C80, 05C63]
sources:
  - url: https://en.wikipedia.org/wiki/Graphon
same_as:
  wikidata: Q5165480
  wikipedia: Graphon
---

## Summary

A graphon is a symmetric measurable function $W \colon [0, 1]^2 \to [0, 1]$.
Graphons are the limit objects of sequences of dense [[graphs|00C0BR7D7H]].
A sequence converges when the density of each fixed small graph in it converges, and then the limit is a graphon.
They also give the most general exchangeable model of a [[random graph|TNT3DG0HRJ]].
Graphons turn questions of [[extremal graph theory|SC5QB5F4TE]], such as [[Sidorenko's conjecture|KN2PXSCT9J]], into questions of analysis.

## Explanations

### L1 human

Draw the adjacency matrix of a large graph as a black and white picture in a unit square, black for an edge and white for no edge.
When the graph grows, the pictures can blur into a grey picture with shades between $0$ and $1$.
That grey picture is a graphon: the shade at a point $(x, y)$ is the probability of an edge between "vertices" $x$ and $y$.
For example, large random graphs with edge probability $1/2$ converge to the constant graphon $W = 1/2$.
