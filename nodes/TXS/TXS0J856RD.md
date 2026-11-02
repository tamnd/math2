---
tag: TXS0J856RD
kind: definition
name: Link
msc: [57K10]
defines: 1A5WRCNTM3
uses: [060W5CBZP6, 0XPR1E85W0, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Link_(knot_theory)
---

## Definition

Let $m \ge 1$ be an integer, and let $S^1 \sqcup \cdots \sqcup S^1$ be the disjoint union of $m$ copies of the [[circle|060W5CBZP6]].

1. A *link with $m$ components* is a subset $L \subset \R^3$ of [[Euclidean space|0XPR1E85W0]] that is the image of a continuous injective map from $S^1 \sqcup \cdots \sqcup S^1$ to $\R^3$.
2. The *components* of $L$ are the images of the $m$ circles.
3. Two links $L$ and $L'$ are *equivalent* if there is a continuous family of [[homeomorphisms|0QT00PB5G2]] $h_t \colon \R^3 \to \R^3$, $t \in [0, 1]$, with $h_0 = \id$ and $h_1(L) = L'$.

## Remarks

A link with one component is a knot.
As for knots, one usually restricts to tame links, those equivalent to a union of closed polygons.
Example: two disjoint round circles in the plane $z = 0$, far apart, form a link with $2$ components, the *unlink* of two components.
Non-example: two circles that meet in one point do not form a link, because the map from the disjoint union is not injective.
Links are often oriented, by choosing a direction on each component.
