---
tag: 0X2GJPNPFN
kind: statement
role: theorem
name: Hall's theorem for bipartite graphs
msc: [05C70]
uses: [01T3TMGTTE, 07DVHJ8N0A, 0Z87BHAFTB]
sources:
  - url: https://en.wikipedia.org/wiki/Hall's_marriage_theorem
    locator: Graph theoretic formulation
---

## Statement

Let $G$ be a finite [[bipartite graph|07DVHJ8N0A]] with parts $X$ and $Y$.
For $W \subseteq X$, let $N(W)$ be the set of vertices of $Y$ that are adjacent to some vertex of $W$.
Then $G$ has a [[matching|0Z87BHAFTB]] that covers every vertex of $X$ if and only if $|N(W)| \ge |W|$ for every $W \subseteq X$.

## Remarks

If $|X| = |Y|$, such a matching is a [[perfect matching|05ZPH8KF9K]]. Thus the condition then characterizes the perfect matchings.
A consequence: a finite regular bipartite graph with at least one edge has a perfect matching.
The theorem is the graph form of [[Hall's marriage theorem|08WCB90WND]]: let $X$ index the sets and let $Y$ be their union.

## Explanations

### L1 human

Think of $X$ as workers and $Y$ as jobs, with an edge when a worker can do a job.
Every worker can get a different job exactly when this holds.
Each group of workers can do, together, at least as many jobs as there are workers in the group.
