---
tag: 01PKQYTTMT
kind: definition
name: Isolated point
msc: [54A05]
defines: 0A1YXSKB48
uses: [0CNQXVBHCX, 01ZQQDCERP]
sources:
  - url: https://en.wikipedia.org/wiki/Isolated_point
    locator: lead section
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]], let $S \subseteq X$ and let $x \in S$.
The point $x$ is an isolated point of $S$ when there is an [[open set|01ZQQDCERP]] $U$ of $X$ with $U \cap S = \{x\}$.

## Remarks

Each point of $S$ is either an isolated point of $S$ or a [[limit point|0HBQC2GJXT]] of $S$, and not both.
In $\mathbb{R}$, each point of $\mathbb{Z}$ is an isolated point of $\mathbb{Z}$: take $U = (n - 1/2, n + 1/2)$.
A point $x$ is an isolated point of $X$ itself if and only if $\{x\}$ is open.

## Explanations

### L1 human

An isolated point is a point of the set that stands alone: a small region about it contains no other point of the set.
In the set $\{0\} \cup [1, 2]$, the point $0$ is isolated, but $1$ is not.
