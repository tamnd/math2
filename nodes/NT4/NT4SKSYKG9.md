---
tag: NT4SKSYKG9
kind: statement
role: theorem
name: Minkowski–Carathéodory theorem
msc: [52A20]
uses: [0XPR1E85W0, 02AS45T3H9, 0R6EWFKRCF, 3MSGFJM2NX, 0FQSDC2EQ2, 21SXYJYC59, DR9BXFWMQB, 0201Q4P2B5, RSRAY0Q68S, KY7SB854VH]
about: [3MSGFJM2NX, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%E2%80%93Milman_theorem
---

## Statement

Let $n \ge 1$ and let $K \subseteq \R^n$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Let $\operatorname{ext} K$ be the set of [[extreme points|3MSGFJM2NX]] of $K$.
Then $K$ is the [[convex hull|0FQSDC2EQ2]] of $\operatorname{ext} K$:
$$K = \operatorname{conv}(\operatorname{ext} K).$$
Moreover, every point of $K$ is a [[convex combination|21SXYJYC59]] of at most $n + 1$ extreme points of $K$.

## Remarks

Proof idea: induct on the dimension of $K$.
If $x$ lies on the relative boundary of $K$, the [[supporting hyperplane theorem|DR9BXFWMQB]] gives a hyperplane $H$ through $x$.
Then $K \cap H$ is a [[face|KY7SB854VH]] of lower dimension whose extreme points are extreme points of $K$.
If $x$ lies in the relative interior, a line through $x$ meets $K$ in a segment with both endpoints on the relative boundary.
Then $x$ is a convex combination of these endpoints.
The bound $n + 1$ then follows from [[Carathéodory's theorem|0201Q4P2B5]].

Example: a filled triangle is the convex hull of its three vertices, and a closed disc is the convex hull of its boundary circle.

Both hypotheses on $K$ are needed.
The closed half-plane $\set{(x, y) : y \ge 0}$ is closed and convex but has no extreme points.
The open disc is bounded and convex but has no extreme points either.

## Explanations

### L1 human

A compact convex shape, that is, a closed and bounded one, is filled in by its corners.
Here a corner means an extreme point, a point not in the middle of any segment of the shape.
For a polygon the corners are the vertices; for a disc every boundary point counts.
In $\R^n$, every point of the shape is a weighted average of at most $n + 1$ corners, for example at most three in the plane.

### L2 human

This is the finite-dimensional case of the [[Krein–Milman theorem|RSRAY0Q68S]].
In $\R^n$ no closure is needed: the convex hull of $\operatorname{ext} K$ is already all of $K$, although $\operatorname{ext} K$ itself need not be closed when $n \ge 3$.
It explains why a linear function on a compact convex set attains its maximum at an extreme point, which is the basis of the simplex method in linear programming.
Applied to polytopes, it says that a bounded intersection of finitely many half-spaces is the convex hull of its vertices.
