---
tag: 35NNSXJB1K
kind: conjecture
name: Hadwiger conjecture
msc: [05C15, 05C83]
uses: [0C5M7AM6FH, VYQ32ZBPEE, 03WKB2H474]
about: [0C5M7AM6FH, VYQ32ZBPEE]
sources:
  - url: https://en.wikipedia.org/wiki/Hadwiger_conjecture_(graph_theory)
same_as:
  wikidata: Q1128435
  wikipedia: Hadwiger conjecture (graph theory)
history:
  posed_by: "Hugo Hadwiger"
  first_stated: "1943"
---

## Statement

Let $k \ge 1$ be an integer, and let $G$ be a finite graph with [[chromatic number|0C5M7AM6FH]] $\chi(G) \ge k$.
Then the [[complete graph|03WKB2H474]] $K_k$ is a [[minor|VYQ32ZBPEE]] of $G$.

## Remarks

Equivalently, every finite graph with no $K_k$ minor can be properly coloured with $k - 1$ colours.
Hugo Hadwiger stated the conjecture in 1943.
It is easy for $k \le 3$, and Hadwiger proved it for $k = 4$.
For $k = 5$ it is equivalent to the [[four colour theorem|0M406JC8J1]], by a structure theorem of Wagner on graphs without a $K_5$ minor.
For $k = 6$ Robertson, Seymour and Thomas proved it in 1993, by reduction to the four colour theorem.
The conjecture is open for every $k \ge 7$.

## Explanations

### L1 human

A minor of a graph is what you get by deleting vertices and edges and by shrinking edges to points.
Hadwiger's conjecture says that a graph needs many colours only for one reason: it contains a big complete graph in this loose sense.
The case of five colours already contains the four colour theorem, so the conjecture is a far-reaching generalization of it.
