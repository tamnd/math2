---
tag: KJT0AXWQXP
kind: definition
name: Proper forcing axiom
msc: ["03E57", "03E50"]
defines: 35XTXNEWQ9
uses: [Z8XMCCZFA4, F2DTWW9HP7, 6FDYJVG1CK]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_forcing_axiom
---

## Definition

Partial orders, dense sets and filters are as in [[Martin's axiom|Z8XMCCZFA4]].
For an uncountable set $\lambda$, let $[\lambda]^{\omega}$ be the set of countable subsets of $\lambda$.
A set $C \subseteq [\lambda]^\omega$ is club if both conditions hold.
It contains the union of each increasing sequence $x_0 \subseteq x_1 \subseteq \cdots$ of its members.
Each countable subset of $\lambda$ is contained in a member of $C$.
A set $S \subseteq [\lambda]^\omega$ is stationary if it meets each club subset of $[\lambda]^\omega$.
A partial order $P$ is proper if [[forcing|F2DTWW9HP7]] with $P$ preserves stationarity: for each uncountable $\lambda$, each stationary $S \subseteq [\lambda]^\omega$ stays stationary in the generic extension.
The proper forcing axiom, PFA, is the following statement.
Let $P$ be a proper partial order, and let $\mathcal{D}$ be a family of at most $\aleph_1$ dense subsets of $P$.
Then some filter on $P$ meets every member of $\mathcal{D}$.

## Remarks

Example: each ccc partial order is proper, so PFA implies $\mathrm{MA}_{\aleph_1}$.
Each countably closed partial order is proper too.
Non-example: the partial order that collapses $\omega_1$ to be countable, by finite partial functions from $\omega$ to $\omega_1$, is not proper.
Proper forcings preserve $\omega_1$, while this one makes $\omega_1$ countable.
Baumgartner proved that PFA is consistent relative to a supercompact cardinal.
PFA implies $2^{\aleph_0} = \aleph_2$, and it implies that every two $\aleph_1$-dense sets of reals are order isomorphic.
These notions extend the [[stationary sets|6FDYJVG1CK]] of a cardinal to sets of countable subsets.
