---
tag: 0NVPNC12JY
kind: definition
name: Open cover
msc: [54D30]
defines: 049PXYHW1T
uses: [01ZQQDCERP, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Cover_(topology)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Cover_(topology)
    locator: Subcover
inventory: [1906G9J52Q]
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $A \subseteq X$.
An open cover of $A$ is a family $(U_i)_{i \in I}$ of [[open subsets|01ZQQDCERP]] of $X$ with $A \subseteq \bigcup_{i \in I} U_i$.
A subcover is a subfamily $(U_j)_{j \in J}$, with $J \subseteq I$, that is still an open cover of $A$.
A subcover is finite when $J$ is a finite set.

## Remarks

The intervals $(-n, n)$ for $n \ge 1$ form an open cover of $\mathbb{R}$. It has no finite subcover.
The intervals $(1/n, 1)$ for $n \ge 2$ form an open cover of $(0, 1)$ with no finite subcover.
A set $K$ is [[compact|00R0X1WGPX]] when each open cover of $K$ has a finite subcover.

## Explanations

### L1 human

An open cover is a collection of open sets that together cover the whole set.
You can think of them as patches, and a finite subcover uses only finitely many patches to cover the set.
