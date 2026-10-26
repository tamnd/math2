---
tag: 0ZDDNBQSC4
kind: definition
name: Angle at a point
aliases: [unoriented-angle]
msc: [51M05]
defines: 0GJAJC6TNZ
uses: [0ZEHZY85E6, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Angle
    locator: Inner product
---

## Definition

Let $A$, $B$ and $C$ be points of a [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$ with $A \neq B$ and $C \neq B$.
The angle $\angle ABC$ is the [[angle between the vectors|0ZEHZY85E6]] $A - B$ and $C - B$. Thus it is the unique real number $\theta$ with $0 \leq \theta \leq \pi$ such that
$$\cos \theta = \frac{(A - B) \cdot (C - B)}{\|A - B\| \, \|C - B\|}.$$
The point $B$ is the vertex of the angle.

## Remarks

The angle is symmetric: $\angle ABC = \angle CBA$.
The angle is $\pi$ if and only if $B$ lies strictly between $A$ and $C$ on a line. It is $0$ if and only if $A$ and $C$ are on the same ray from $B$.
Mathlib's `EuclideanGeometry.angle` uses the same formula for all points. It gives $\pi / 2$ when $A = B$ or $C = B$.
The angle is a right angle when $\theta = \pi / 2$, acute when $\theta < \pi / 2$ and obtuse when $\theta > \pi / 2$.

## Explanations

### L1 human

To measure the angle at $B$, stand at $B$ and look at $A$, then turn to look at $C$. The angle is how far you turn, using the short way round. The order of $A$ and $C$ does not matter.
