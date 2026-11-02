---
tag: JCG0MRFGC7
kind: definition
name: Clean ring
msc: [16U60, 16U40]
defines: CYCTQ0CR3K
uses: [0894J980RK, 0X4JKZXJ86, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Clean_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with unit $1$.
An element $a \in R$ is *clean* if $a = e + u$ for an [[idempotent|0X4JKZXJ86]] $e$ (so $e^2 = e$) and a [[unit|019NFGFPR5]] $u$ of $R$.
The ring $R$ is *clean* if every element of $R$ is clean.

## Remarks

Example: a local ring $R$, one whose non-units form a two-sided ideal $\mathfrak{m}$.
If $a$ is a unit, then $a = 0 + a$.
If $a \in \mathfrak{m}$, then $a - 1 \notin \mathfrak{m}$, since otherwise $1 \in \mathfrak{m}$; so $a - 1$ is a unit and $a = 1 + (a - 1)$.
Non-example: the ring $\Z$, whose idempotents are $0, 1$ and units are $\pm 1$.
The sums $e + u$ are $-1, 0, 1, 2$, so $3$ is not clean.
Every homomorphic image of a clean ring is clean, since idempotents and units map to idempotents and units.
