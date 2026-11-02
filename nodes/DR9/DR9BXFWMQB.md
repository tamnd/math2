---
tag: DR9BXFWMQB
kind: statement
role: theorem
name: Supporting hyperplane theorem
msc: [52A20, 52A07]
uses: [0XPR1E85W0, 02AS45T3H9, 05D5EGMFYV, K7N565NKCV, 0S52TNNTH9, 6GWMGFGFJJ]
about: [K7N565NKCV, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Supporting_hyperplane
---

## Statement

Let $n \ge 1$, let $S \subseteq \R^n$ be a [[convex set|02AS45T3H9]], and let $x_0$ be a point of the [[boundary|05D5EGMFYV]] of $S$.
Then there is a [[supporting hyperplane|K7N565NKCV]] of $S$ through $x_0$.
That is, there is a vector $a \in \R^n$ with $a \ne 0$ such that $a \cdot x \le a \cdot x_0$ for all $x \in S$, where $a \cdot x$ is the [[dot product|0S52TNNTH9]].

## Remarks

Proof idea: since $x_0$ is a boundary point of the convex set $S$, it is not an interior point of the closure $\overline{S}$, so there are points $y_k \notin \overline{S}$ with $y_k \to x_0$.
For each $k$, the nearest point of $\overline{S}$ to $y_k$ gives a unit vector $a_k$ with $a_k \cdot x \le a_k \cdot y_k$ for all $x \in S$.
A subsequence of the unit vectors $a_k$ converges to a unit vector $a$, and passing to the limit gives $a \cdot x \le a \cdot x_0$ for all $x \in S$.

Example: for the square $[0, 1]^2$ and the corner $x_0 = (1, 1)$, every $a = (a_1, a_2) \ne 0$ with $a_1, a_2 \ge 0$ works, so the supporting line at a corner is not unique.

Convexity is needed: for the annulus $\set{x \in \R^2 : 1 \le \abs{x} \le 2}$, the inner boundary point $(1, 0)$ has no supporting line, since every line through it has points of the annulus on both sides.
A partial converse holds: a closed set with nonempty interior that has a supporting hyperplane at each of its boundary points is convex.

## Explanations

### L1 human

Take a convex shape and any point on its edge.
The theorem says you can always lay a flat wall against the shape at that point, with the whole shape on one side.
For a smooth shape the wall is the tangent plane; at a corner there may be many possible walls.
This fails for shapes with dents, where the wall would have to cut through the shape.

### L2 human

The theorem is the finite-dimensional, boundary-point form of the separation theorems; the general version is the [[Hahn–Banach separation theorem|6GWMGFGFJJ]].
It is used to prove that a compact convex set in $\R^n$ is the convex hull of its extreme points.
That proof passes to the face cut out by a supporting hyperplane and inducts on dimension.
It gives the existence of subgradients of a convex function at interior points of its domain, by applying it to the epigraph.
In optimisation it is the geometric root of Lagrange multipliers and of the Karush–Kuhn–Tucker conditions.
