---
tag: 0TP2QKJ8DE
kind: definition
name: Circumcentre
aliases: [circumcenter]
msc: [51M04]
defines: 0F98FZK14A
uses: [0CTNFGYMM2, 0YMB1676R1, 0NPPGHQNXQ, 055VNYT0PB]
sources:
  - url: https://en.wikipedia.org/wiki/Circumcircle
    locator: lead section
---

## Definition

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean space $\mathbb{R}^n$, and let $d$ be the [[Euclidean distance|0NPPGHQNXQ]]. Let $P$ be the plane through $A$, $B$ and $C$, their [[affine span|0YMB1676R1]].
The circumcentre of $ABC$ is the unique point $O$ of $P$ with
$$d(O, A) = d(O, B) = d(O, C).$$
This common distance $R$ is the circumradius of $ABC$.

## Remarks

The point $O$ exists and is unique. In the plane, it is the common point of the three [[perpendicular bisectors|055VNYT0PB]] of the sides. Two of them meet in one point because the sides are not parallel.
The circumcentre is inside the triangle if the triangle is acute, on the longest side if it is right, and outside if it is obtuse.
In a right triangle, the circumcentre is the midpoint of the hypotenuse, by [[Thales's theorem|0GSDHYMA1T]].
Mathlib defines the circumcentre of each simplex in the same way, inside the affine span of the vertices.

## Explanations

### L1 human

The circumcentre is the point that is equally far from the three corners of a triangle. To find it, draw the perpendicular bisectors of two sides; they cross at the circumcentre. A circle with this centre through one corner passes through all three.
