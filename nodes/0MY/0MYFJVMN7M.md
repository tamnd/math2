---
tag: 0MYFJVMN7M
kind: statement
role: proposition
name: Compact subsets of a Hausdorff space are closed
msc: [54D30]
uses: [0P6PMJB4MA, 0MXB4CKHFW, 0G5AV9Q4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_space
    locator: Properties of compact spaces
---

## Statement

Let $X$ be a [[Hausdorff space|0MXB4CKHFW]] and let $K$ be a [[compact subset|00R0X1WGPX]] of $X$.
Then $K$ is [[closed|0G5AV9Q4RR]] in $X$.

## Remarks

Proof: fix $y \notin K$. For each $x \in K$, choose disjoint open sets $U_x \ni x$ and $V_x \ni y$. Finitely many $U_{x_1}, \ldots, U_{x_n}$ cover $K$. Then $V_{x_1} \cap \cdots \cap V_{x_n}$ is an open set that contains $y$ and misses $K$.
The Hausdorff condition is needed. With the [[indiscrete topology|0XJ02JBD6S]] on a set with two points, each one-point set is compact but not closed.
Each metric space is Hausdorff, so compact subsets of metric spaces are closed.

## Explanations

### L1 human

In a Hausdorff space, you can separate a point outside $K$ from each point of $K$ by open sets.
Compactness lets you do this with finitely many open sets at once, which gives an open set about the point that misses $K$.
