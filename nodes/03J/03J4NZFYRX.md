---
tag: 03J4NZFYRX
kind: definition
name: Perpendicular bisector
msc: [51M04]
defines: 055VNYT0PB
uses: [0S706JBZBG, 03NK6RSRQ1, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Bisection
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Bisection
    locator: Perpendicular line segment bisectors in space
---

## Definition

Let $A$ and $B$ be distinct points of the Euclidean space $\mathbb{R}^n$, and let $M = \frac{1}{2}(A + B)$ be their [[midpoint|0S706JBZBG]]. Let $\cdot$ be the dot product.
The perpendicular bisector of $A$ and $B$ is the set
$$\{\, X \in \mathbb{R}^n \;:\; (X - M) \cdot (B - A) = 0 \,\}.$$

## Remarks

A point $X$ is on the perpendicular bisector if and only if $d(X, A) = d(X, B)$, where $d$ is the [[Euclidean distance|0NPPGHQNXQ]].
It is a hyperplane with the [[normal vector|0WQJJCCTC8]] $B - A$. In the plane it is a line, and in $\mathbb{R}^3$ it is a plane.
Mathlib's `AffineSubspace.perpBisector` also allows $A = B$. Then the set is the whole space.
The perpendicular bisectors of the three sides of a triangle in the plane meet at the [[circumcentre|0F98FZK14A]].

## Explanations

### L1 human

The perpendicular bisector of a segment cuts it in half at a right angle. Each point on it is as far from one end of the segment as from the other. For the points $(0, 0)$ and $(2, 0)$, the perpendicular bisector is the vertical line $x = 1$.
