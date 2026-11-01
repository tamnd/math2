---
tag: 5HDNJWZ6K9
kind: definition
name: Hyperconnected space
msc: [54D05, 14A05]
defines: 38CDCK1RYB
uses: [0CQHFPGJ45, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperconnected_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
The space $X$ is *hyperconnected*, or *irreducible*, if the following two conditions hold.

1. $X$ is nonempty.
2. For all nonempty [[open sets|02BH3MCBQB]] $U, V \subseteq X$, the intersection $U \cap V$ is nonempty.

## Remarks

Equivalent forms: every nonempty open subset of $X$ is [[dense|0BSJSX7ME2]] in $X$.
Also equivalent: $X$ is nonempty and is not the union of two closed subsets different from $X$.

Example: an infinite set $X$ with the [[cofinite topology|0B906ZBTMZ]].
Nonempty open sets have finite complements, so the union of the complements of $U$ and $V$ is finite and cannot be all of $X$.

Non-example: a [[Hausdorff space|0S1FJ8VEX9]] with at least two points fails clause 2.
Two distinct points have disjoint open neighbourhoods.
