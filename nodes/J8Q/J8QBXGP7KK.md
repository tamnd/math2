---
tag: J8QBXGP7KK
kind: definition
name: Metacompact space
msc: [54D20]
defines: WQG81SEDZ4
uses: [0CQHFPGJ45, 049PXYHW1T]
sources:
  - url: https://en.wikipedia.org/wiki/Metacompact_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A family $\mathcal{V}$ of subsets of $X$ is *point-finite* if each $x \in X$ belongs to only finitely many members of $\mathcal{V}$.
The space $X$ is *metacompact* if every [[open cover|049PXYHW1T]] $\mathcal{U}$ of $X$ has a point-finite open refinement.
That is, there is a point-finite open cover $\mathcal{V}$ such that each $V \in \mathcal{V}$ lies in some $U \in \mathcal{U}$.

## Remarks

Example: every [[paracompact space|8R29G6NG9Q]] is metacompact.
A [[locally finite|DZ297MMGV8]] family is point-finite, since a neighbourhood of $x$ meeting finitely many members also shows that $x$ lies in finitely many.

Non-example: the space $[0, \omega_1)$ of countable ordinals with the order topology is not metacompact.
It is [[countably compact|S3N3CHZV89]] but not compact.
A countably compact metacompact space is always compact.
