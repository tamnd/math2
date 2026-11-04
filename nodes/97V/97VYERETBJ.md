---
about:
- 02AS45T3H9
- 0FQSDC2EQ2
kind: statement
msc:
- 52A20
- 52A07
name: Closed convex sets are intersections of closed half-spaces
role: corollary
sources:
- url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L19474
  locator: scv.tex:19474
tag: 97VYERETBJ
uses:
- 02AS45T3H9
- 0FQSDC2EQ2
- 0ZCK8DQYN1
---

## Statement

Let $S \subseteq \R^n$ be a [[closed|0ZCK8DQYN1]] [[convex set|02AS45T3H9]]. Then $S$ equals the intersection of all closed half-spaces of $\R^n$ that contain $S$.

More generally, let $S \subseteq \R^n$ be any set. Then the intersection of all closed half-spaces that contain $S$ is the closed convex hull of $S$. This is the smallest closed convex set that contains $S$, that is, the closure of the [[convex hull|0FQSDC2EQ2]] of $S$.

## Remarks

Every closed half-space is closed and convex, so the intersection is a closed convex set that contains $S$. The content of the result is the other inclusion: a point outside a closed convex set can be cut off from it by a closed half-space.
