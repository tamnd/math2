---
tag: 05MDKQBEAF
kind: statement
role: theorem
name: Angle sum of a triangle
aliases: [triangle-angle-sum-theorem]
msc: [51M04]
uses: [0CTNFGYMM2, 0GJAJC6TNZ]
sources:
  - url: https://en.wikipedia.org/wiki/Sum_of_angles_of_a_triangle
    locator: Euclidean geometry
same_as:
  wikidata: Q7840113
  wikipedia: Sum of angles of a triangle
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in a Euclidean space $\mathbb{R}^n$, and let $\angle$ denote the [[angle at a point|0GJAJC6TNZ]]. Then
$$\angle BAC + \angle CBA + \angle ACB = \pi.$$

## Remarks

Mathlib proves the formula under the weaker hypothesis that $B \neq A$ and $C \neq A$, with its convention for the angle at a repeated point.
An equilateral triangle has three equal angles, so each one is $\pi / 3$.
In the axioms of plane geometry, the statement is equivalent to the parallel postulate. It is false in spherical geometry, where the sum is more than $\pi$, and in hyperbolic geometry, where it is less.

## History

Euclid's Elements proves the statement as part of Proposition 32 of Book I.

## Explanations

### L1 human

Cut a paper triangle and tear off its three corners. Put the corners side by side with their tips at one point. They always fill a straight line, which is half a turn, or $\pi$ radians.
