---
tag: FEAFDTMMW7
kind: definition
name: Knot
msc: [57K10]
defines: QYEAZTYGPT
uses: [060W5CBZP6, 0XPR1E85W0, 0QT00PB5G2, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Knot_(mathematics)
---

## Definition

Let $S^1$ be the [[circle|060W5CBZP6]] and let $\R^3$ be [[Euclidean space|0XPR1E85W0]] of dimension $3$.

1. A *knot* is a subset $K \subset \R^3$ that is the image of a continuous injective map $f \colon S^1 \to \R^3$.
2. Two knots $K$ and $K'$ are *equivalent* if there is a continuous family of [[homeomorphisms|0QT00PB5G2]] $h_t \colon \R^3 \to \R^3$, $t \in [0, 1]$, with $h_0 = \id$ and $h_1(K) = K'$. Such a family is an *ambient isotopy*.
3. A knot is *tame* if it is equivalent to a knot that is a closed polygon with finitely many edges.

## Remarks

Equivalence of knots is an [[equivalence relation|0G8VEZ3WTK]], and knot theory studies the equivalence classes.
Since $S^1$ is compact, the map $f$ is a homeomorphism onto $K$.
Most texts consider only tame knots.
Every knot that is the image of a smooth embedding is tame, and every tame knot is equivalent to such a knot.
Some texts use the $3$-sphere $S^3$ in place of $\R^3$; this gives the same theory.
Often a knot is also oriented, by choosing a direction along $S^1$.

Example: the circle $\set{(x, y, 0) : x^2 + y^2 = 1}$ is a knot, the image of $t \mapsto (\cos t, \sin t, 0)$, which is injective on $[0, 2\pi)$; it is a tame knot, the [[unknot|1TQ06R4Q66]].
Non-example: the figure-eight curve $t \mapsto (\sin 2t, \sin t, 0)$ is not a knot, because it is not injective: $t = 0$ and $t = \pi$ both map to the origin.
A [[wild knot|QYDQ28X8MA]] satisfies the first clause but not the third.
