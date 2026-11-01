---
tag: ETDW4AK1W1
kind: definition
name: Lindelöf space
msc: [54D20]
defines: SW0SN1NEJE
uses: [0CQHFPGJ45, 049PXYHW1T]
sources:
  - url: https://en.wikipedia.org/wiki/Lindel%C3%B6f_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
The space $X$ is a *Lindelöf space* if every [[open cover|049PXYHW1T]] $\mathcal{U}$ of $X$ has a countable subcover.
That is, there is a countable family $\mathcal{V} \subseteq \mathcal{U}$ with $\bigcup \mathcal{V} = X$.

## Remarks

Example: $\R$ with the usual topology is Lindelöf.
It is [[second-countable|03PPNCM9GG]], with the countable base of open intervals with rational end points.
For an open cover $\mathcal{U}$, pick for each basic interval contained in some member of $\mathcal{U}$ one such member; these countably many members cover $\R$.

Non-example: an uncountable set $X$ with the discrete topology is not Lindelöf.
The cover $\set{\set{x} : x \in X}$ is an open cover, and every subcover must contain all of its uncountably many members.

The [[Sorgenfrey line|Y4T3GVK8GV]] is Lindelöf, but its square, the Sorgenfrey plane, is not.
So a product of two Lindelöf spaces need not be Lindelöf.
