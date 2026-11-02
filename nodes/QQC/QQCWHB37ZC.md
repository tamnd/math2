---
tag: QQCWHB37ZC
kind: definition
name: Discrete subgroup
msc: ["22E40", 22D05, 20H10]
defines: 5M7D1BSHVZ
uses: [92700QAB5Y, 0X1JXT47GA, 0S2TEHX4E1]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_group
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] and let $\Gamma$ be a [[subgroup|0X1JXT47GA]] of $G$.
The subgroup $\Gamma$ is *discrete* if the subspace topology on $\Gamma$ is the [[discrete topology|0S2TEHX4E1]].

## Remarks

Equivalently, there is an open neighbourhood $U$ of the identity $e$ in $G$ with $U \cap \Gamma = \set{e}$.
Indeed, then $\gamma U$ is an open set with $\gamma U \cap \Gamma = \set{\gamma}$ for each $\gamma \in \Gamma$.

Example: $\Z$ is a discrete subgroup of $\R$, since $U = (-\tfrac12, \tfrac12)$ meets $\Z$ only in $0$.
Likewise $\mathrm{SL}_n(\Z)$ is a discrete subgroup of $\mathrm{SL}_n(\R)$, since two distinct integer matrices differ by at least $1$ in some entry.

Non-example: $\Gamma = \set{a + b\sqrt2 : a, b \in \Z}$ is a subgroup of $\R$ that is not discrete.
The numbers $(\sqrt2 - 1)^k$ lie in $\Gamma$, are nonzero, and tend to $0$, so every neighbourhood of $0$ meets $\Gamma$ in more than one point.

In a Hausdorff topological group, every discrete subgroup is closed.
