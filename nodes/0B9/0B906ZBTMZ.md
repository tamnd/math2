---
tag: 0B906ZBTMZ
kind: example
name: Cofinite topology
aliases: [finite-complement-topology]
msc: [54A05]
instance_of: [0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Cofiniteness
    locator: Cofinite topology
inventory: [CGNX9Z67M3]
---

## Example

Let $X$ be a set and let $\tau$ consist of $\varnothing$ and of all sets $U \subseteq X$ whose complement $X \setminus U$ is [[finite|0BBTH3YSZA]].
Then $\tau$ is a [[topology|0CNQXVBHCX]] on $X$, the cofinite topology.

## Remarks

The closed sets are $X$ and the finite subsets of $X$.
The cofinite topology is [[T1|05GQJXBP3F]]: each one-point set is closed.
If $X$ is infinite, any two nonempty open sets meet. Thus the space is not [[Hausdorff|0MXB4CKHFW]].
Each space with the cofinite topology is [[compact|0QPHW703PV]].

## Explanations

### L1 human

In the cofinite topology, a set is open when it misses only finitely many points.
On an infinite set, open sets are very large, so no two nonempty open sets are disjoint.
