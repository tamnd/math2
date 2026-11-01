---
tag: PDDAJEYDE9
kind: definition
name: Residual set
msc: ["54E52"]
defines: GRH8MCVN3N
uses: [0CQHFPGJ45, 0XGCZ4GDZ6, 0BSJSX7ME2]
sources:
  - url: https://en.wikipedia.org/wiki/Meagre_set
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $R \subseteq X$.
The set $R$ is *residual* in $X$ if its complement $X \setminus R$ is [[meagre|0XGCZ4GDZ6]] in $X$.

## Remarks

Equivalently, $R$ contains a set $\bigcap_{n \ge 1} U_n$, where each $U_n$ is open and [[dense|0BSJSX7ME2]] in $X$.
Residual sets are also called comeagre sets.

Example: the set of irrational numbers is residual in $\R$.
Its complement $\Q$ is countable, so it is a countable union of single points, and each single point is [[nowhere dense|0VQYCCQVJ5]].

Non-example: $\Q$ is not residual in $\R$.
Otherwise $\R$ would be the union of the meagre sets $\Q$ and $\R \setminus \Q$.
This contradicts the [[Baire category theorem|0A7KGAYHGV]], since $\R$ is a complete metric space.
