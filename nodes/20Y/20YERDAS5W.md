---
tag: 20YERDAS5W
kind: definition
name: Locally compact group
msc: ["22D05", "22A05"]
defines: AHV05ZBCYW
uses: [92700QAB5Y, 0EQMWQ4WMJ, 0MXB4CKHFW]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_compact_group
---

## Definition

A *locally compact group* is a [[topological group|92700QAB5Y]] $G$ such that:

1. the topology of $G$ is [[Hausdorff|0MXB4CKHFW]];
2. the topology of $G$ is [[locally compact|0EQMWQ4WMJ]], that is, every point of $G$ has a compact neighbourhood.

## Remarks

Example: $(\R^n, +)$ is a locally compact group, since the closed ball of radius $1$ around $x$ is a compact neighbourhood of $x$ by the Heine–Borel theorem.
Every discrete group is locally compact, since $\set{x}$ is a compact neighbourhood of $x$.

Non-example: the additive group of an infinite-dimensional Hilbert space $H$ is a Hausdorff topological group but is not locally compact.
Suppose $0$ had a compact neighbourhood $K$.
Then $K$ contains a closed ball of some radius $r > 0$, and this ball is compact as a closed subset of $K$.
For an orthonormal sequence $(e_k)$, the points $r e_k$ lie in this ball.
They have no convergent subsequence, a contradiction, since $\norm{r e_j - r e_k} = r\sqrt{2}$ for $j \ne k$.

By homogeneity it is enough that the identity has a compact neighbourhood.
Some authors omit the Hausdorff condition; a locally compact group in that wider sense becomes Hausdorff after dividing by the closure of the identity.
