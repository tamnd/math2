---
tag: 91WG6QWRQ1
kind: definition
name: Open segment
msc: [52A05]
defines: CCZA91NE5X
uses: [000AYPA9AJ, VQ4Q2V45RP]
sources:
  - url: https://en.wikipedia.org/wiki/Line_segment
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]] and let $x, y \in V$.
The *open segment* between $x$ and $y$ is the set
$$(x, y) = \set{(1 - t) x + t y : t \in \R,\ 0 < t < 1}.$$

## Remarks

Example: on the real line, $(0, 1)$ in this sense is the open interval of numbers strictly between $0$ and $1$; the point $1/4$ is in it with $t = 1/4$.

Non-example: the endpoint $x$ of a [[line segment|VQ4Q2V45RP]] $[x, y]$ with $x \ne y$ is not in $(x, y)$, since $(1 - t) x + t y = x$ forces $t (y - x) = 0$, so $t = 0$, which is not allowed.

If $x \ne y$, then $(x, y) = [x, y] \setminus \set{x, y}$.
If $x = y$, then $(x, y) = \set{x}$, so the open segment is not empty.
