---
tag: M4H3QNJPGD
kind: definition
name: Noetherian topological space
msc: [54D30, 14A05, "13E05"]
defines: 2VQX2E8EAH
uses: [0CQHFPGJ45, 0ZCK8DQYN1]
sources:
  - url: https://en.wikipedia.org/wiki/Noetherian_topological_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
The space $X$ is *Noetherian* if it satisfies the descending chain condition on [[closed sets|0ZCK8DQYN1]].
That is, for every sequence $C_1 \supseteq C_2 \supseteq C_3 \supseteq \cdots$ of closed subsets of $X$, there is $n$ with $C_m = C_n$ for all $m \ge n$.

## Remarks

Equivalent forms: every ascending chain of open subsets stabilises.
Also equivalent: every nonempty family of closed subsets has a minimal element.
Also equivalent: every subset of $X$ is [[compact|0TVJZYB6SH]] in the subspace topology.

Example: any set $X$ with the [[cofinite topology|0B906ZBTMZ]].
A proper closed subset is finite, so a strictly descending chain of closed sets has finitely many steps after its first proper member.

Non-example: $\R$ with the usual topology.
The closed sets $C_n = [n, \infty)$ satisfy $C_1 \supsetneq C_2 \supsetneq \cdots$, so the chain never stabilises.
