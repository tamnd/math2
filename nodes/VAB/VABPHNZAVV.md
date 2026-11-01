---
tag: VABPHNZAVV
kind: definition
name: Profinite group
msc: ["20E18", 22C05]
defines: KA0YDB6QXE
uses: [0TVJZYB6SH, 0S1FJ8VEX9, 0RJSBR9GW1, V6TJAFZ4MD]
sources:
  - url: https://en.wikipedia.org/wiki/Profinite_group
---

## Definition

Let $(G_i)_{i \in I}$ be an inverse system of finite groups indexed by a directed set $I$, each with the discrete topology.
Give its inverse limit $\varprojlim_{i \in I} G_i$ the subspace topology of the product $\prod_{i \in I} G_i$.
A *profinite group* is a topological group $G$ that is isomorphic, as a topological group, to such an inverse limit.

## Remarks

A topological group is profinite if and only if it is [[compact|0TVJZYB6SH]], [[Hausdorff|0S1FJ8VEX9]] and [[totally disconnected|0RJSBR9GW1]].
Then $G$ is the inverse limit of its finite quotients $G/N$, where $N$ runs over the open normal subgroups.

Example: the [[p-adic integers|V6TJAFZ4MD]] $\Z_p = \varprojlim_n \Z/p^n\Z$, with the reduction maps $\Z/p^{n+1}\Z \to \Z/p^n\Z$.
Each $\Z/p^n\Z$ is finite and discrete, so $\Z_p$ is profinite.

Non-example: $\Z$ with the discrete topology is Hausdorff and totally disconnected but not compact, so it is not profinite.
Its profinite completion $\hat\Z = \varprojlim_n \Z/n\Z$ is profinite and contains $\Z$ as a dense subgroup.

Every finite group with the discrete topology is profinite.
Closed subgroups, quotients by closed normal subgroups, and arbitrary products of profinite groups are profinite.
