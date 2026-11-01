---
tag: 3BZAPDBPC8
kind: definition
name: Urysohn space
msc: [54D10]
defines: MF3BWZ9YSW
uses: [0CQHFPGJ45, 0ZCY0Z80B6, 0ZCK8DQYN1, 0S1FJ8VEX9, 03HMJASQBQ]
sources:
  - url: https://en.wikipedia.org/wiki/Urysohn_and_completely_Hausdorff_spaces
---

## Definition

A [[topological space|0CQHFPGJ45]] $X$ is an *Urysohn space* when the following holds.
For all $x, y \in X$ with $x \ne y$, there are [[neighbourhoods|0ZCY0Z80B6]] $U$ of $x$ and $V$ of $y$ such that $\overline{U} \cap \overline{V} = \varnothing$.

## Remarks

Equivalently, any two distinct points have disjoint [[closed|0ZCK8DQYN1]] neighbourhoods.
Every Urysohn space is [[Hausdorff|0S1FJ8VEX9]], since the interiors of $\overline{U}$ and $\overline{V}$ are disjoint open sets around $x$ and $y$.
Every [[regular|03HMJASQBQ]] Hausdorff space is Urysohn.

Example: $\R$ is Urysohn.
For $x < y$, put $r = (y - x)/3$; the closures $[x - r, x + r]$ and $[y - r, y + r]$ of the open intervals of radius $r$ are disjoint.

Non-example: an infinite set with the [[cofinite topology|0B906ZBTMZ]] is not Urysohn.
Any two nonempty open sets in it meet, so even the Hausdorff condition fails.

Notation: $T_{2\frac12}$.
A space in which distinct points are separated by a continuous function $f \colon X \to [0, 1]$ is called completely Hausdorff; some authors call that an Urysohn space.
