---
tag: 7QFKD5JXH6
kind: statement
role: theorem
name: Stone's theorem on paracompactness of metric spaces
msc: ["54E35", 54D20]
uses: [0VKD1TP7F3, 8R29G6NG9Q, DZ297MMGV8, 049PXYHW1T]
about: [8R29G6NG9Q, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Paracompact_space
---

## Statement

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] with the topology induced by $d$.
Then $X$ is [[paracompact|8R29G6NG9Q]].
That is, every [[open cover|049PXYHW1T]] of $X$ has an open refinement that is a [[locally finite family|DZ297MMGV8]].

## Remarks

The theorem is due to A. H. Stone.
A short proof by Mary Ellen Rudin well-orders the members of the cover.
For each $n$ and each member $U$, it takes the union of balls of radius $2^{-n}$ around suitable points whose first containing member is $U$.
The radii are chosen so that each point has a ball meeting only finitely many of the new sets.
The proof uses the axiom of choice through the well-ordering.

Example at work: every metric space is therefore [[normal|0NSR9V8TED]] and admits partitions of unity subordinate to any open cover.

The metric is essential only through the topology it induces.
So every metrizable space is paracompact.

## Explanations

### L1 human

Metric spaces can be very large and far from compact.
Still, every open cover of a metric space can be replaced by a finer cover that is finite near each point.
This makes metric spaces good spaces for gluing local objects.

### L2 human

Stone's theorem shows that paracompactness is a necessary condition for metrizability.
Metrization theorems such as the [[Nagata–Smirnov theorem|KB11T6389G]] go in the other direction.
Combined with [[Dieudonné's theorem|B6Y8PEY72W]], it gives another proof that metric spaces are normal.
It is also why paracompactness is automatic for metrizable manifolds.
