---
tag: 54KHZGC0CV
kind: definition
name: Compact group
msc: [22C05]
defines: EVHCE5VR6Y
uses: [92700QAB5Y, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_group
---

## Definition

A *compact group* is a [[topological group|92700QAB5Y]] $G$ whose topology is Hausdorff and [[compact|0TVJZYB6SH]].

## Remarks

Example: the unitary group $U(n) = \set{A \in M_n(\C) : A^* A = I}$ with the topology from $M_n(\C) \cong \C^{n^2}$ is a compact group.
It is Hausdorff as a subspace of $\C^{n^2}$.
It is closed, as the zero set of the continuous map $A \mapsto A^*A - I$.
It is bounded, since each column of a unitary matrix has norm $1$, so it is compact by the Heine–Borel theorem.
Non-example: the group $\R$ with addition and the usual topology is a Hausdorff topological group.
It is not compact, since the open cover by the intervals $(-n, n)$ has no finite subcover.
Every finite group with the discrete topology is a compact group.
Some authors do not require the Hausdorff condition; others include it in the definition of a topological group.
