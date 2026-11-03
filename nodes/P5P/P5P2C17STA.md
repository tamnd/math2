---
tag: P5P2C17STA
kind: concept
name: Lower K-groups
msc: [19A49, 19B99, 19C99]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
    locator: Lower K-groups
---

## Summary

The lower K-groups of a ring $R$ are the groups $K_0(R)$, $K_1(R)$ and $K_2(R)$ of [[algebraic K-theory|5GVFZWMWC8]].
They are defined by explicit algebraic constructions before Quillen's higher K-theory.
The group [[$K_0(R)$|Q14JS2MA1C]] comes from projective modules, [[$K_1(R)$|SXVNJY4XFY]] from invertible matrices modulo elementary ones, and [[$K_2(R)$|W7T56A6YF8]] from relations among elementary matrices.
Quillen's higher K-groups agree with these three in degrees $0$, $1$ and $2$.
Some authors also count the negative K-groups of Bass among the lower K-groups.

## Explanations

### L1 human

The three lower K-groups describe a ring through linear algebra over it.
$K_0$ counts projective modules, the possible "vector spaces" over the ring.
$K_1$ measures the invertible matrices that cannot be reduced to the identity by row operations; for a field it is the determinant.
$K_2$ measures the relations between row operations that are not forced by the obvious rules.
For a field $F$, these give $K_0(F) = \Z$ and $K_1(F) = F^\times$.
