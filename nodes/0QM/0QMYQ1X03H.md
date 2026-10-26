---
tag: 0QMYQ1X03H
kind: definition
name: Orthocentre
msc: [51M04]
defines: 0WB619CA0V
uses: [0CTNFGYMM2, 0C9MZY2RNA, 0MP9BCF6DP]
sources:
  - url: https://en.wikipedia.org/wiki/Orthocenter
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Orthocenter
    locator: History
---

## Definition

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean space $\mathbb{R}^n$. The three [[lines|0MP9BCF6DP]] that contain the [[altitudes|0C9MZY2RNA]] of $ABC$ meet in exactly one point $H$.
This point $H$ is the orthocentre of $ABC$.

## Remarks

The orthocentre is inside the triangle if the triangle is acute. In a right triangle, it is the vertex at the right angle. In an obtuse triangle, it is outside.
In an equilateral triangle, the orthocentre is the same point as the centroid, the circumcentre and the incentre.
The Book of Lemmas, attributed to Archimedes, uses the fact that the three altitudes meet. Al-Nasawi stated and proved it explicitly in the 11th century.
Mathlib's `Affine.Triangle.orthocenter` defines it as the Monge point of the triangle.

## Explanations

### L1 human

Draw the three altitudes of a triangle, each from a corner at a right angle to the opposite side. The three lines always pass through one common point. For the right triangle with the vertices $(0, 0)$, $(3, 0)$ and $(0, 4)$, this point is the corner $(0, 0)$.
