---
tag: EXMR7RYRTP
kind: problem
name: Maximum flow problem
msc: [90C35, 90B10, 05C21]
uses: [ZSNXTW5E2K, 4HMR4KQ01T, 9P19SEYN1R, VNMXB0J2KA]
about: [ZSNXTW5E2K]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_flow_problem
same_as:
  wikidata: Q2585642
  wikipedia: Maximum flow problem
history:
  posed_by: "T. E. Harris and F. S. Ross"
  first_stated: "1954"
  notes: "It was formulated as a simplified model of railway traffic; Ford and Fulkerson published the first algorithm in 1956."
---

## Problem

Let $N = (V, A, c, s, t)$ be a [[flow network|ZSNXTW5E2K]], with capacities $c \colon A \to [0, \infty)$.
The *maximum flow problem* asks for an $s$–$t$ flow $f$ in $N$ of largest value $\abs{f}$.

## Remarks

A maximum flow exists, since the flows form a nonempty compact set and the value is continuous.
The [[max-flow min-cut theorem|4HMR4KQ01T]] says that the maximum value equals the least capacity of an $s$–$t$ cut.
The problem is a [[linear program|VNMXB0J2KA]], and the minimum cut problem is its dual.
The [[Ford–Fulkerson method|9P19SEYN1R]] augments along paths in the residual network.
Choosing shortest augmenting paths gives the [[Edmonds–Karp algorithm|PFYANWXNJ1]], and augmenting along blocking flows gives [[Dinic's algorithm|23ZP0GHKD4]].
The [[push–relabel algorithm|HNH4C6DV46]] works with preflows instead of flows.
Orlin gave an algorithm with $O(\abs{V} \abs{A})$ steps in 2013, and for integer capacities, algorithms with almost linear running time in $\abs{A}$ were found in 2022.
Bipartite matching, edge- and vertex-disjoint paths and some scheduling problems reduce to maximum flow.

## Explanations

### L1 human

How much can be sent from one place to another through a network whose links have limited capacities?
For example, take roads $s \to a$ of capacity $2$, $a \to t$ of capacity $3$ and $s \to t$ of capacity $1$.
At most $3$ units can reach $t$, since only $3$ units can leave $s$.
The answer is always set by a bottleneck, a set of links that separates the source from the sink.
Fast algorithms find both the best flow and such a bottleneck.
