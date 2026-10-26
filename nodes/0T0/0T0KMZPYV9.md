---
tag: 0T0KMZPYV9
kind: definition
name: Normal core
aliases: [core-of-a-subgroup]
msc: [20D25]
defines: 0GETX79CJN
uses: [0D6WHTTH7T, 0W77CVBCHQ, 0ZTGMDNVTB]
sources:
  - url: https://en.wikipedia.org/wiki/Core_(group_theory)
    locator: Definition
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
The normal core of $H$ in $G$ is the subgroup $\operatorname{Core}_G(H) = \bigcap_{g \in G} gHg^{-1}$.

## Remarks

The core is a [[normal subgroup|0CB0DX5BVV]] of $G$, and it contains each normal subgroup of $G$ that lies in $H$.
The subgroup $H$ is normal exactly when $\operatorname{Core}_G(H) = H$.
The core is the kernel of the action of $G$ on the left cosets of $H$ by left multiplication.

## Explanations

### L1 human

Some subgroups are not normal, but they still contain normal subgroups.
The normal core is the biggest of these.
You find it by keeping only the elements that lie in every conjugate of the subgroup.
