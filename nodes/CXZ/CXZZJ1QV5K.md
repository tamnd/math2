---
tag: CXZZJ1QV5K
kind: definition
name: Alexandrov topology
msc: [54A05, 06A06]
defines: ATP1JK3V27
uses: [0CQHFPGJ45, 02BH3MCBQB, 0VABYWJWH9, ETCE287E2R]
sources:
  - url: https://en.wikipedia.org/wiki/Alexandrov_topology
---

## Definition

Let $X$ be a set and let $\tau$ be a [[topology|0CQHFPGJ45]] on $X$.
The topology $\tau$ is an *Alexandrov topology* if for every family $(U_i)_{i \in I}$ of [[open sets|02BH3MCBQB]] of $\tau$, the intersection $\bigcap_{i \in I} U_i$ is open.
A topological space whose topology is an Alexandrov topology is called an *Alexandrov space* or an Alexandrov-discrete space.

## Remarks

Equivalently, every point $x \in X$ has a smallest open set $U_x$ containing it, namely the intersection of all open sets that contain $x$.

For a [[preorder|0VABYWJWH9]] $\le$ on $X$, the family of all [[upper sets|ETCE287E2R]] of $(X, \le)$ is an Alexandrov topology.
Conversely, every Alexandrov topology arises in this way from exactly one preorder, its [[specialization preorder|CMYVK9CEKZ]].

Example: every topology on a finite set is an Alexandrov topology, because then every family of open sets is finite.

Non-example: the usual topology of $\R$ is not an Alexandrov topology.
The open sets $(-1/n, 1/n)$ for $n \ge 1$ have intersection $\set{0}$, which is not open.

The name "Alexandrov space" is also used in metric geometry for spaces with curvature bounded below; that notion is unrelated.
