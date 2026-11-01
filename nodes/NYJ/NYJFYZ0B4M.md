---
tag: NYJFYZ0B4M
kind: definition
name: Adele ring
msc: [11R56]
defines: SEH68BA1QQ
uses: [MWBDFS2KJ5, BT5V3TSNY6, BT6T702C28, V6TJAFZ4MD, 0B1261B5ED, 0FE2SB8WVJ, 0GBG8B49AA]
sources:
  - url: https://en.wikipedia.org/wiki/Adele_ring
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]].
For each [[place|BT5V3TSNY6]] $v$ of $K$, let $K_v$ be the completion of $K$ at $v$.
For each finite place $v$, let $\mathcal{O}_v = \set{x \in K_v : \abs{x}_v \le 1}$ be its valuation ring.
The *adele ring* of $K$ is
$$\mathbb{A}_K = \Big\{ (x_v)_v \in \prod_v K_v : x_v \in \mathcal{O}_v \text{ for all but finitely many finite } v \Big\},$$
with componentwise addition and multiplication, so it is a [[ring|0B1261B5ED]].
Its topology is the restricted product topology.
A basis of open sets is formed by the sets $\prod_{v \in S} U_v \times \prod_{v \notin S} \mathcal{O}_v$.
Here $S$ is a finite set of places containing all infinite places, and each $U_v \subseteq K_v$ is open.

## Remarks

With this topology, $\mathbb{A}_K$ is a [[locally compact|0FE2SB8WVJ]] topological ring.
The topology is finer than the one induced by the [[product topology|0GBG8B49AA]] on $\prod_v K_v$.
The diagonal map $K \to \mathbb{A}_K$, $x \mapsto (x)_v$, is well defined because an element of $K$ lies in $\mathcal{O}_v$ for all but finitely many $v$; its image is discrete and $\mathbb{A}_K / K$ is compact.

Example: for $K = \Q$, the places are $\infty$ and the primes $p$, with $\Q_\infty = \R$, $\Q_p$ the [[p-adic numbers|BT6T702C28]] and $\mathcal{O}_p = \Z_p$ the [[p-adic integers|V6TJAFZ4MD]].
The family $x = (x_v)$ with $x_\infty = \pi$, $x_2 = 1/2$ and $x_p = 1$ for $p \ge 3$ is an adele, since only one $p$-adic entry lies outside $\Z_p$.

Non-example: the family with $x_\infty = 0$ and $x_p = 1/p$ for every prime $p$ lies in $\prod_v \Q_v$ but not in $\mathbb{A}_{\Q}$, since $1/p \notin \Z_p$ for infinitely many $p$.
