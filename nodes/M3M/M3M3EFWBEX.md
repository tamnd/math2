---
tag: M3M3EFWBEX
kind: definition
name: Locally finite family
msc: [54D20]
defines: DZ297MMGV8
uses: [0CQHFPGJ45, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_finite_collection
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $(A_i)_{i \in I}$ be a family of subsets of $X$.
The family is *locally finite* if every point $x \in X$ has a [[neighbourhood|0ZCY0Z80B6]] $N$ such that the set $\set{i \in I : N \cap A_i \ne \emptyset}$ is finite.

## Remarks

Example: in $\R$, the family $([n, n + 1])_{n \in \Z}$ is locally finite.
For $x \in \R$, the neighbourhood $(x - 1, x + 1)$ meets $[n, n + 1]$ only when $x - 2 < n < x + 1$, which holds for at most three integers $n$.

Non-example: in $\R$, the family $((0, 1/n))_{n \ge 1}$ is not locally finite.
Every neighbourhood of $0$ contains an interval $(-\varepsilon, \varepsilon)$, which meets every $(0, 1/n)$.

If $(A_i)_{i \in I}$ is locally finite, then the [[closure|0QEAJB91GZ]] of $\bigcup_i A_i$ equals $\bigcup_i \overline{A_i}$.
In particular, the union of a locally finite family of [[closed sets|0ZCK8DQYN1]] is closed.
