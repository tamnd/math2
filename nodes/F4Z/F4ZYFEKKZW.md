---
tag: F4ZYFEKKZW
kind: definition
name: Compact Lie group
msc: ["22E15", 22C05]
defines: 9TFC6ADC1C
uses: [7JBRGCVJRB, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_group
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]].
The group $G$ is a *compact Lie group* if its underlying topological space is [[compact|0TVJZYB6SH]].

## Remarks

Example: the special unitary group $\mathrm{SU}(2)$ is the set of complex matrices $\begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$ with $\abs{a}^2 + \abs{b}^2 = 1$.
It is a closed subgroup of $\mathrm{GL}_2(\C)$, so it is a Lie group.
As a space it is the unit sphere $S^3$ in $\C^2 \cong \R^4$, which is closed and bounded, hence compact.

Non-example: the additive group $\R$ is a Lie group, but it is not compact, since the open cover by the intervals $(-n, n)$ has no finite subcover.

A compact group need not be a Lie group.
The group $\Z_p$ of $p$-adic integers is compact, but each neighbourhood of $0$ contains the nontrivial subgroup $p^k \Z_p$ for $k$ large, so it is not a Lie group.

Each compact Lie group is isomorphic to a closed subgroup of some unitary group $\mathrm{U}(n)$.
