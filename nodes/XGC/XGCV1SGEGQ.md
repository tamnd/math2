---
tag: XGCV1SGEGQ
kind: definition
name: Colimit
msc: [18A30]
defines: BJS1CGTKQ5
uses: [A2DE66937D, HJK75HDWFE, 7TPBQPPN97, EK85VSSRMR, CHS5AFJGWE, DAMK8XE1FR, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_(category_theory)
---

## Definition

Let $J$ and $\mathcal{C}$ be [[categories|A2DE66937D]] and let $D \colon J \to \mathcal{C}$ be a [[diagram|HJK75HDWFE]].
A *colimit* of $D$ is a [[cocone|7TPBQPPN97]] $(C, \iota)$ under $D$, with $\iota_j \colon D(j) \to C$, that satisfies the following condition.
For every cocone $(N, \psi)$ under $D$ there is exactly one morphism $h \colon C \to N$ with $h \circ \iota_j = \psi_j$ for every object $j$ of $J$.
The object $C$ is written $\operatorname{colim} D$ or $\varinjlim D$, and the $\iota_j$ are its *injections*.

## Remarks

Equivalently, a colimit is an [[initial object|EK85VSSRMR]] of the category of cocones under $D$, so it is unique up to unique isomorphism.
A colimit of $D$ in $\mathcal{C}$ is the same as a [[limit|CHS5AFJGWE]] of the corresponding diagram $D^{\mathrm{op}} \colon J^{\mathrm{op}} \to \mathcal{C}^{\mathrm{op}}$ in the [[opposite category|DAMK8XE1FR]].
The colimit of the empty diagram is an initial object.

Example: in the category of sets, every diagram $D$ with $J$ small has a colimit.
Let $\sim$ be the smallest [[equivalence relation|0G8VEZ3WTK]] on the disjoint union $\bigsqcup_j D(j)$ that identifies $x \in D(j)$ with $D(u)(x) \in D(k)$ for every $u \colon j \to k$.
The colimit is the quotient $\left(\bigsqcup_j D(j)\right) / {\sim}$.
The injections send $x$ to its class, and a cocone $(N, \psi)$ induces $h([x]) = \psi_j(x)$, which is well defined by the cocone condition.

Non-example: for the diagram of two parallel functions $f, g \colon X \rightrightarrows Y$ with $f \neq g$, the set $Y$ with $\iota_Y = \id_Y$ and $\iota_X = f$ is not a cocone, since $\iota_Y \circ g = g \neq \iota_X$; so it cannot be a colimit.
