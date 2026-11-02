---
tag: 6KQ6E3YHKR
kind: definition
name: Stone space
msc: ["06E15", "54D30"]
defines: ZV38HA5PAQ
uses: [0CQHFPGJ45, 0TVJZYB6SH, 0S1FJ8VEX9, 0RJSBR9GW1]
sources:
  - url: https://en.wikipedia.org/wiki/Stone_space
---

## Definition

A *Stone space* is a [[topological space|0CQHFPGJ45]] $X$ such that:

1. $X$ is [[compact|0TVJZYB6SH]].
2. $X$ is [[Hausdorff|0S1FJ8VEX9]].
3. $X$ is [[totally disconnected|0RJSBR9GW1]]: its only connected subsets with at least one point are the singletons.

## Remarks

For a compact Hausdorff space, clause 3 is equivalent to having a basis of [[clopen sets|DQ4E55T3BW]], that is, to being [[zero-dimensional|JJ7D0CYECZ]].

Example: the Cantor space $\set{0, 1}^{\N}$ with the product topology.
It is compact by Tychonoff's theorem and Hausdorff as a product of Hausdorff spaces.
Two different sequences differ at some index $n$, and the set of sequences with a fixed $n$-th term is clopen, so no connected set contains both.

Non-example: the interval $[0, 1]$ is compact and Hausdorff but connected, so clause 3 fails.
The space $\Q$ is Hausdorff and totally disconnected but not compact, so clause 1 fails.
