---
tag: 0Z87BHAFTB
kind: definition
name: Matching
msc: [05C70]
defines: 0MJ04A50QW
sources:
  - url: https://en.wikipedia.org/wiki/Matching_(graph_theory)
    locator: Definitions
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
A matching in $G$ is a set $M$ of edges of $G$ such that no two distinct edges of $M$ have a common end.

## Remarks

A vertex is matched if it is an end of an edge of $M$. Otherwise it is unmatched.
A maximal matching is not contained in a larger matching. A maximum matching has the largest number of edges, the matching number $\nu(G)$.
Every maximum matching is maximal, but the converse is false: in the [[path graph|075WR6W3Y3]] $P_4$, the middle edge alone is a maximal matching.

## Explanations

### L1 human

A matching pairs some vertices along edges, and no vertex is in two pairs.
For example, it can pair workers with jobs that they can do, one job per worker.
