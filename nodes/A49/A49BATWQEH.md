---
tag: A49BATWQEH
kind: definition
name: Ordered group
msc: ["06F15", "20F60"]
defines: KRDR04RQ7N
uses: [G5S1M9, 011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_group
---

## Definition

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $\le$ be a [[partial order|011C29Q1S1]] on $G$.
The pair $(G, \le)$ is an *ordered group*, or *partially ordered group*, if for all $a, b, c \in G$,
$$a \le b \implies ca \le cb \text{ and } ac \le bc.$$

## Remarks

Example: $\Z^2$ under addition, with $(a, b) \le (c, d)$ when $a \le c$ and $b \le d$, is an ordered group.
If $a \le c$ and $b \le d$, then $a + x \le c + x$ and $b + y \le d + y$ for each $(x, y) \in \Z^2$.
Non-example: on $\Z$, let $a \preceq b$ when $a = b$ or $(a, b) = (0, 1)$.
This is a partial order, but $0 \preceq 1$ while $1 \not\preceq 2$, so adding $1$ breaks the condition.
The *positive cone* of $G$ is $P = \set{g \in G : e \le g}$.
It satisfies $PP \subseteq P$, $P \cap P^{-1} = \set{e}$ and $gPg^{-1} = P$ for each $g \in G$.
Conversely, each subset $P$ with these three properties defines an ordered group by $a \le b \iff a^{-1} b \in P$.
For an abelian group the condition is written additively: $a \le b$ implies $a + c \le b + c$.
