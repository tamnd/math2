---
tag: 9S18DSRFND
kind: statement
role: theorem
name: Uniqueness of best approximation in strictly convex spaces
msc: [41A52, 46B20, 41A65]
uses: [GDTKW9KPH8, 7N4988HN3P, 02AS45T3H9]
about: [7N4988HN3P, GDTKW9KPH8]
sources:
  - url: https://en.wikipedia.org/wiki/Strictly_convex_space
---

## Statement

Let $X$ be a [[strictly convex|GDTKW9KPH8]] normed space, let $C \subseteq X$ be a nonempty [[convex set|02AS45T3H9]], and let $x \in X$.
Then $x$ has at most one [[best approximation|7N4988HN3P]] from $C$.
In particular, if $V \subseteq X$ is a finite-dimensional linear subspace, every $x \in X$ has exactly one best approximation from $V$.

## Remarks

The idea of the proof: let $d = \inf_{c \in C} \norm{x - c}$ and suppose $c_1 \ne c_2$ in $C$ both have $\norm{x - c_i} = d$.
Then $d > 0$, since otherwise $c_1 = x = c_2$.
The midpoint $m = (c_1 + c_2)/2$ lies in $C$, and $x - m$ is the midpoint of $x - c_1$ and $x - c_2$, two different vectors of norm $d$.
Strict convexity gives $\norm{x - m} < d$, which contradicts the definition of $d$.
The second sentence follows with the existence of best approximations from finite-dimensional subspaces.

Example: every Hilbert space and every $L^p$ space with $1 < p < \infty$ is strictly convex, so least squares and $L^p$ polynomial approximations are unique.

Strict convexity cannot be dropped.
In $\R^2$ with the maximum norm, every point $(t, 0)$ with $\abs{t} \le 1$ is a best approximation of $(0, 1)$ from the horizontal axis.
The space $C[a, b]$ with the supremum norm is not strictly convex either; there uniqueness of best polynomial approximation needs the Haar condition instead.

Convexity of $C$ is also needed: from the centre of a circle in the Euclidean plane, all points of the circle are nearest.

## Explanations

### L1 human

If the unit ball of a space has no flat pieces on its boundary, then from any point there cannot be two equally near points in a convex set.
If there were, the point halfway between them would be strictly nearer.
This is why least squares problems have unique solutions.

### L2 human

The theorem separates the geometry of the norm from the approximating set.
For finite-dimensional subspaces, it says that strictly convex spaces make every such subspace a Chebyshev set.
In non-strictly convex spaces such as $C(K)$ and $L^1$, uniqueness depends on the subspace, and Haar's theorem characterizes the finite-dimensional subspaces of $C(K)$ with unique best approximations.
