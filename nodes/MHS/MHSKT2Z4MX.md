---
tag: MHSKT2Z4MX
kind: statement
role: theorem
name: Birkhoff–Kakutani theorem
msc: [22A05, "54E35", 54H11]
uses: [7GKCGQ7215, 091GJ3FYD7, 0CP5NDD21C, 0VKD1TP7F3]
about: [7GKCGQ7215, 091GJ3FYD7]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Statement

Let $G$ be a [[Hausdorff topological group|7GKCGQ7215]].
The following are equivalent.

1. $G$ is [[metrizable|091GJ3FYD7]].
2. $G$ is [[first-countable|0CP5NDD21C]], that is, the identity of $G$ has a countable base of neighbourhoods.
3. There is a [[metric|0VKD1TP7F3]] $d$ on $G$ that induces the topology of $G$ and is left-invariant: $d(gx, gy) = d(x, y)$ for all $g, x, y \in G$.

## Remarks

The implications from 3 to 1 and from 1 to 2 are immediate.
For the main step from 2 to 3, choose a base $U_0 \supseteq U_1 \supseteq \cdots$ of symmetric neighbourhoods of the identity with $U_{n+1}^3 \subseteq U_n$.
These sets are used to build a function that plays the role of $d(e, x)$, and then $d(x, y)$ is defined from $x^{-1} y$.
Example: the $p$-adic integers $\Z_p$ have the countable base $p^n \Z_p$ at $0$, and $d(x, y) = p^{-v_p(x - y)}$ is an invariant metric, where $v_p$ is the $p$-adic valuation.
The Hausdorff hypothesis is needed: a group with two or more elements and the indiscrete topology is first-countable but not metrizable.
Without first countability the conclusion fails: an uncountable product of copies of $\Z/2\Z$ is a compact Hausdorff group that is not metrizable.

## Explanations

### L1 human

For a topological group, having a distance function that describes its topology costs very little.
It is enough that the identity has a countable list of shrinking neighbourhoods that capture all of its neighbourhoods.
Then one can even choose the distance so that multiplying on the left by a fixed element does not change distances.

### L2 human

The theorem turns questions about first-countable Hausdorff groups into questions about metric spaces, so sequences suffice to describe the topology.
It is a basic tool for Polish groups and for second-countable locally compact groups, where one often fixes a compatible left-invariant metric.
A left-invariant metric need not be complete even when the group is complete for its two-sided uniformity, which is why the theory of Polish groups distinguishes these notions.
