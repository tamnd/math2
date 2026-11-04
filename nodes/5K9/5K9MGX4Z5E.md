---
tag: 5K9MGX4Z5E
kind: statement
role: proposition
name: Additivity of variance over an orthonormal basis
msc: [62H25, 15A63]
uses: [0FWJ0VW561, 0Q8HZTJC7G]
about: [ABXD13M340]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-1.xml#L1710
    locator: src/section7-1.xml:1710
---

## Statement

Take a finite data set of points in $\R^m$, centered at the origin.
For a subspace $W$ of $\R^m$, let $V_W$ be the variance of the points after [[orthogonal projection|0Q8HZTJC7G]] onto $W$.
For a unit vector $u$, let $V_u$ be the variance of the points projected onto the line spanned by $u$.

Suppose $u_1, \dots, u_n$ is an [[orthonormal basis|0FWJ0VW561]] of $W$.
Then the variance of the projected points splits over the basis:

$$V_W = V_{u_1} + V_{u_2} + \dots + V_{u_n}.$$

## Remarks

The variance here is the mean squared length of the projected points.
For a point $x$, the projection onto $W$ is $\sum_j (x \cdot u_j) u_j$.
Its squared length is $\sum_j (x \cdot u_j)^2$, because the $u_j$ are orthonormal.
Averaging over the points gives the claim.

The result is the basis for choosing the directions of largest variance in principal component analysis.
