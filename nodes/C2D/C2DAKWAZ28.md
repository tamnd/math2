---
tag: C2DAKWAZ28
kind: definition
name: Wedge sum
msc: [54B17, 55P99]
defines: 5JSWM1HBX2
uses: [T9DG8DDE75, ZXJKSB30WF, 0NQ1H2X495]
sources:
  - url: https://en.wikipedia.org/wiki/Wedge_sum
---

## Definition

Let $(X_i, x_i)_{i \in I}$ be a family of [[pointed spaces|T9DG8DDE75]].
The *wedge sum* of the family is the space
$$\bigvee_{i \in I} X_i = \Bigl( \bigsqcup_{i \in I} X_i \Bigr) / \set{x_i : i \in I}.$$
It is the quotient of the [[disjoint union|ZXJKSB30WF]] that collapses the set of base points to one point.
It carries the [[quotient topology|0NQ1H2X495]].
The image of the base points is the base point of the wedge sum.

## Remarks

For two spaces one writes $X \vee Y$.
Each $X_i$ embeds in the wedge sum, and a pointed map out of $\bigvee_i X_i$ is the same as a family of pointed maps out of the $X_i$.
Example: $S^1 \vee S^1$ is homeomorphic to the figure eight $\set{z \in \C : \abs{z - 1} = 1 \text{ or } \abs{z + 1} = 1}$, where the two circles meet only at $0$.
Non-example: the disjoint union $S^1 \sqcup S^1$ without collapsing the base points is not a wedge sum; it is disconnected, while the wedge of connected spaces is connected.
The wedge sum depends on the choice of base points in general, but not up to homotopy for well-behaved spaces such as connected CW complexes.
