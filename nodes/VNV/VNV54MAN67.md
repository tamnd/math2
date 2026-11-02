---
tag: VNV54MAN67
kind: definition
name: Extreme point
msc: [46A55, 52A07]
defines: 3MSGFJM2NX
uses: [000AYPA9AJ, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_point
---

## Definition

Let $X$ be a [[vector space|000AYPA9AJ]] over $\R$ or $\C$, and let $K \subseteq X$ be a [[convex set|02AS45T3H9]].
A point $x \in K$ is an *extreme point* of $K$ if, whenever $x = t y + (1 - t) z$ with $y, z \in K$ and $0 < t < 1$, one has $y = z = x$.
The set of extreme points of $K$ is written $\operatorname{ext} K$.

## Remarks

In $\R^2$, let $K = [0, 1]^2$.
The corner $(0, 0)$ is extreme: if $(0, 0) = t y + (1 - t) z$ with $y, z \in K$ and $0 < t < 1$, then each coordinate is a combination of nonnegative numbers with positive weights equal to $0$, so $y = z = (0, 0)$.
The point $(1/2, 0)$ is not extreme, because it is the midpoint of $(0, 0)$ and $(1, 0)$, which lie in $K$ and differ from it.
Equivalently, $x$ is extreme when $x$ is not the midpoint of two distinct points of $K$.
An open ball in a nonzero normed space has no extreme points.
The closed unit ball of the sequence space $c_0$ also has no extreme points.
