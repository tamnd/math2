---
tag: N9QDDYY7GK
kind: definition
name: Chebyshev set
msc: [41A65, 41A52, 46B20]
defines: M4RMZNGZ2P
uses: [03J5RAKB30, 7N4988HN3P]
sources:
  - url: https://en.wikipedia.org/wiki/Metric_projection
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]] and let $K \subseteq X$ be nonempty.
The set $K$ is a *Chebyshev set* if every $x \in X$ has exactly one [[best approximation|7N4988HN3P]] from $K$, that is, exactly one $k \in K$ with $\norm{x - k} = \inf_{y \in K} \norm{x - y}$.
The map $P_K \colon X \to K$ sending $x$ to this point is the *metric projection* onto $K$.

## Remarks

Example: in $\R^2$ with the Euclidean norm, the closed unit disc $D$ is a Chebyshev set.
For $\norm{x} \le 1$ the nearest point is $x$ itself.
For $\norm{x} > 1$ it is $x / \norm{x}$ and no other point of $D$, since the triangle inequality is strict off the ray through $x$.

Non-example: the unit circle in $\R^2$ is not a Chebyshev set, because the origin has every point of the circle as a nearest point.

A Chebyshev set is closed, since a point of the closure not in $K$ would have distance $0$ but no nearest point.
Every nonempty closed convex set in a Hilbert space is a Chebyshev set, by the [[Hilbert projection theorem|J5YNTHQMFX]].
In $\R^n$ with the Euclidean norm the converse holds: every Chebyshev set is convex.
Whether every Chebyshev set in an infinite-dimensional Hilbert space is convex is an open problem.
