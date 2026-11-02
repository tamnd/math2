---
tag: F1W3QRBNGJ
kind: statement
role: theorem
name: Helly's theorem
msc: [52A35]
uses: [0XPR1E85W0, 02AS45T3H9, 0R6EWFKRCF, 888R24ZGNY]
about: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Helly%27s_theorem
same_as:
  wikidata: Q1632433
  wikipedia: Helly's theorem
---

## Statement

Let $d \ge 1$ and let $C_1, \dots, C_m$ be [[convex sets|02AS45T3H9]] in $\R^d$, with $m \ge d + 1$.
Suppose that every $d + 1$ of the sets have a point in common.
Then all $m$ sets have a point in common: $C_1 \cap \cdots \cap C_m \ne \emptyset$.

## Remarks

Proof idea: induct on $m$, starting from $m = d + 1$.
For $m \ge d + 2$, the induction hypothesis gives, for each $j$, a point $x_j$ in all the sets except possibly $C_j$.
[[Radon's theorem|888R24ZGNY]] applied to $x_1, \dots, x_m$ gives a partition into $A$ and $B$ with a common point $p$ of their convex hulls.
Each $C_i$ contains all of $A$ or all of $B$, so it contains $p$ by convexity.

Example: if every three of finitely many convex sets in the plane meet, then all of them meet.

The number $d + 1$ cannot be lowered: the three lines that contain the sides of a triangle in $\R^2$ meet in pairs but have no common point.
For an infinite family the statement can fail: the half-lines $[k, \infty)$, $k = 1, 2, \dots$, in $\R$ meet in pairs but have empty intersection.
The infinite version holds when all the sets are [[compact|0R6EWFKRCF]] and convex.

## Explanations

### L1 human

To check that many convex sets share a point, it is enough to check small groups.
In the plane, groups of three suffice; in space, groups of four.
Without convexity this fails.
Cut a circle in the plane into four disjoint arcs, and for each arc let $S_i$ be the circle with that arc removed.
Any three of the sets $S_i$ share the fourth arc, but no point lies in all four.

### L2 human

Helly's theorem is the model of a Helly-type theorem: a global property follows from the same property for all small subfamilies.
It has many consequences, such as the centerpoint theorem and Jung's theorem on the smallest ball containing a set.
It is used in Kirchberger's theorem and has a fractional version and a colourful version.
In optimisation it explains why an infeasible system of convex constraints in $\R^d$ has an infeasible subsystem with at most $d + 1$ constraints.
