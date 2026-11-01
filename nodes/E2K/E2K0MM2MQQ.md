---
tag: E2K0MM2MQQ
kind: counterexample
name: Line with two origins
msc: [54G20, 54D10, 57N99]
uses: [0S1FJ8VEX9, 03PPNCM9GG, 0W4CN9E2W5, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Non-Hausdorff_manifold
    locator: Line with two origins
---

## Counterexample

Let $Y = \R \times \set{0, 1}$, the disjoint union of two copies of the real line.
Identify $(x, 0)$ with $(x, 1)$ for every $x \ne 0$, and give the set $X$ of classes the quotient topology.
The two classes $0_a$ of $(0, 0)$ and $0_b$ of $(0, 1)$ are the two origins.
The space $X$ is locally homeomorphic to $\R$, [[second-countable|03PPNCM9GG]] and $T_1$, but it is not [[Hausdorff|0S1FJ8VEX9]].

## Remarks

Removing $0_b$ leaves an open set homeomorphic to $\R$, and the same holds for $0_a$; these two open sets cover $X$.
Every [[neighbourhood|0ZCY0Z80B6]] of $0_a$ contains the image of $(-\varepsilon, 0) \cup (0, \varepsilon)$ for some $\varepsilon > 0$, and so does every neighbourhood of $0_b$.
So any neighbourhood of $0_a$ meets any neighbourhood of $0_b$, and the two origins cannot be separated.
For the same reason the sequence of classes of $1/n$ [[converges|0W4CN9E2W5]] to both $0_a$ and $0_b$, so limits of sequences are not unique.
This is why the usual definition of a topological manifold requires the Hausdorff condition: without it, this space would count as a $1$-manifold.

## Explanations

### L1 human

Take the real line and double its zero point, keeping everything else the same.
Near each point, the new space still looks like a piece of the line.
But the two zeros are glued so tightly to the same nearby points that no pair of open sets can keep them apart.
A sequence that goes to zero now goes to both zeros at once.
