---
tag: KHJ2G2R5G7
kind: concept
name: Strong operator topology
msc: [47L05, 46L10, 46A03]
sources:
  - url: https://en.wikipedia.org/wiki/Strong_operator_topology
same_as:
  wikidata: Q4392013
  wikipedia: Strong operator topology
---

## Summary

The strong operator topology is the topology of pointwise convergence on the bounded operators on a Hilbert space.
A net $T_i$ converges to $T$ when $T_i x \to T x$ in norm for every vector $x$.
It lies between the [[weak operator topology|4XM1VN1C1N]] and the norm topology.
It is the natural topology for limits such as partial sums of orthogonal projections and for one-parameter unitary groups.

## Explanations

### L1 human

Two operators are close in the strong operator topology when they move each of finitely many chosen vectors to nearby places.
This is weaker than being close in norm, which asks for the same accuracy on all unit vectors at once.
For example, let $P_n$ keep the first $n$ coordinates of a sequence and set the rest to $0$.
For each fixed sequence $x$ in $\ell^2$, the truncation $P_n x$ tends to $x$, so $P_n \to I$ strongly.
But $P_n$ never comes close to $I$ in norm, since $I - P_n$ still keeps the $(n+1)$-st basis vector unchanged.
