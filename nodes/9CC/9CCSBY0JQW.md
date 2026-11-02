---
tag: 9CCSBY0JQW
kind: definition
name: Betweenness
msc: [51G05, 51N10]
defines: CE8GX6ADZS
uses: [09XNAPTJQ7, 0P3VCBDEE2]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_geometry
---

## Definition

Let $F$ be an [[ordered field|0P3VCBDEE2]], let $V$ be a vector space over $F$, and let $P$ be an [[affine space|09XNAPTJQ7]] over $V$.
Let $x, y, z \in P$.
The point $y$ is *weakly between* $x$ and $z$ if $y = x + t(z - x)$ for some $t \in F$ with $0 \le t \le 1$.
The point $y$ is *strictly between* $x$ and $z$ if it is weakly between them and $y \ne x$ and $y \ne z$.

## Remarks

Example: in $\R^2$, the point $(1, 1)$ is strictly between $(0, 0)$ and $(2, 2)$, with $t = 1/2$.
Non-example: $(3, 3)$ is on the line through $(0, 0)$ and $(2, 2)$, but it is not between them, since it needs $t = 3/2 > 1$.
Weak betweenness is symmetric: if $y$ is weakly between $x$ and $z$, then it is weakly between $z$ and $x$, with $1 - t$ in place of $t$.
The set of points weakly between $x$ and $z$ is the closed segment $[x, z]$.
In axiomatic geometry, betweenness is not defined but taken as a primitive relation that satisfies the axioms of order.
