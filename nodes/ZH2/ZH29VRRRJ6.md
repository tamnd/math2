---
tag: ZH29VRRRJ6
kind: definition
name: Paracompact space
msc: [54D20]
defines: 8R29G6NG9Q
uses: [0CQHFPGJ45, 049PXYHW1T, DZ297MMGV8]
sources:
  - url: https://en.wikipedia.org/wiki/Paracompact_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
An open cover $\mathcal{V}$ of $X$ is a *refinement* of an open cover $\mathcal{U}$ if every $V \in \mathcal{V}$ is contained in some $U \in \mathcal{U}$.
The space $X$ is *paracompact* if every [[open cover|049PXYHW1T]] of $X$ has an open refinement that is a [[locally finite family|DZ297MMGV8]].

## Remarks

Example: $\R$ is paracompact.
Given an open cover $\mathcal{U}$, each compact interval $[n, n + 1]$ is covered by finitely many members of $\mathcal{U}$.
Intersect these members with $(n - 1, n + 2)$; the resulting sets, over all $n \in \Z$, form a locally finite open refinement.

Non-example: the [[long line|1DKCNS63DH]] is not paracompact, although it is Hausdorff and locally homeomorphic to $\R$.

Every [[compact space|0TVJZYB6SH]] is paracompact, since a finite subcover is a locally finite refinement.
Some authors include the Hausdorff condition in the definition of a paracompact space.
