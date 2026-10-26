---
tag: 0C38S0KMJK
kind: definition
name: Interior
aliases: [interior-of-a-set]
msc: [54A05]
defines: 0RZH6W98HK
uses: [0CNQXVBHCX, 01ZQQDCERP, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_(topology)
    locator: Definitions
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
The interior of $S$ is the [[union|05GK32H72H]] of all [[open sets|01ZQQDCERP]] $U$ of $X$ with $U \subseteq S$.
It is written $\operatorname{int} S$ or $S^\circ$.
A point of $\operatorname{int} S$ is an interior point of $S$.

## Remarks

A point $x$ is an interior point of $S$ if and only if there is an open set $U$ with $x \in U \subseteq S$.
In a metric space, $x$ is an interior point of $S$ if and only if $B(x, \varepsilon) \subseteq S$ for some $\varepsilon > 0$.
In $\mathbb{R}$, the interior of $[0, 1]$ is $(0, 1)$, and the interior of $\mathbb{Q}$ is $\emptyset$.

## Explanations

### L1 human

The interior of a set is what remains when you remove its edge points.
A point is in the interior when a whole small neighbourhood of it lies in the set.
