---
tag: 0TCHAS04WK
kind: definition
name: Convex hull
aliases: [convex-envelope, convex-closure]
msc: [52A20]
defines: 0FQSDC2EQ2
uses: [02AS45T3H9, 0KJH6SRFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_hull
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Convex_hull
    locator: Equivalence of definitions
  - url: https://en.wikipedia.org/wiki/Convex_hull
    locator: Topological properties
---

## Definition

Let $X$ be a subset of $\mathbb{R}^n$. The convex hull of $X$ is the intersection of all [[convex sets|02AS45T3H9]] of $\mathbb{R}^n$ that contain $X$:
$$\operatorname{conv}(X) = \bigcap \{\, S \subseteq \mathbb{R}^n \;:\; S \supseteq X \text{ and } S \text{ is convex} \,\}.$$

## Remarks

$\operatorname{conv}(X)$ is convex, and it is the smallest convex set that contains $X$.
It is also the set of all convex combinations $\sum_{i=1}^{k} w_i x_i$, with $k \geq 1$, $x_i \in X$, $w_i \geq 0$ and $\sum_i w_i = 1$. These are the [[affine combinations|0KJH6SRFZK]] with nonnegative weights.
The convex hull of a compact set is compact, and the convex hull of an open set is open.
The convex hull of a finite set is a convex polytope. For three points not on a line, it is the triangle with its inside.

## Explanations

### L1 human

For a finite set of points in the plane, put a rubber band round all the points and let it go. The band takes the shape of the boundary of the convex hull. The convex hull of the four corners of a square is the full square.
