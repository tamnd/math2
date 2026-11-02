---
tag: 5T2J3FDT0X
kind: definition
name: Polish group
msc: [22A05, 54H11, 54H05]
defines: 9C1WSBNQX9
uses: [92700QAB5Y, 584GXXY73M, 0515A6D2Y1, 0ZH5AJ2ED7]
sources:
  - url: https://en.wikipedia.org/wiki/Polish_space
---

## Definition

A *Polish group* is a [[topological group|92700QAB5Y]] $G$ whose underlying topological space is a [[Polish space|584GXXY73M]].
That is, the topology of $G$ is separable and is induced by some complete metric.

## Remarks

Example: the [[symmetric group|0515A6D2Y1]] $S_\infty$ of all bijections $\N \to \N$, with the topology of pointwise convergence.
It is a $G_\delta$ subset of the Polish space $\N^\N$, hence Polish, and composition and inversion are continuous for this topology.
Non-example: $(\Q, +)$ with the topology from $\R$.
It is separable and metrizable, but it is countable without isolated points.
So it is a countable union of nowhere dense singletons and is not a [[Baire space|0ZH5AJ2ED7]]; hence no complete metric induces its topology.
The metric need not be invariant: a Polish group always has a compatible left-invariant metric, but this metric may fail to be complete.
