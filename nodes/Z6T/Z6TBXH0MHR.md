---
tag: Z6TBXH0MHR
kind: definition
name: Locally compact abelian group
msc: [22B05, 43A40]
defines: ZR09S9R3AW
uses: [92700QAB5Y, 082GHNPJ53, 0FE2SB8WVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_compact_abelian_group
---

## Definition

A *locally compact abelian group* is a [[topological group|92700QAB5Y]] $G$ such that:

1. the group $G$ is [[abelian|082GHNPJ53]];
2. the topology of $G$ is Hausdorff;
3. the topology of $G$ is [[locally compact|0FE2SB8WVJ]], that is, each point of $G$ has a compact neighbourhood.

## Remarks

Example: $\R^n$ with addition and the usual topology is an LCA group.
It is abelian, Hausdorff, and each point $x$ has the compact neighbourhood $\set{y : \norm{y - x} \le 1}$.
Non-example: the additive group $\Q$ of rational numbers with the topology from $\R$ is abelian and Hausdorff, but it is not locally compact.
Each neighbourhood of $0$ contains a set $(-\varepsilon, \varepsilon) \cap \Q$, hence a sequence of rationals that converges in $\R$ to an irrational number.
This sequence has no subsequence that converges in $\Q$, so no neighbourhood of $0$ is contained in a compact subset of $\Q$.
The usual abbreviation is "LCA group".
Many authors include the Hausdorff condition in the definition of a topological group.
