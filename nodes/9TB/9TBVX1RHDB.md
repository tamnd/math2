---
tag: 9TBVX1RHDB
kind: definition
name: Non-uniform rational B-spline
msc: [65D17, 68U07, 41A15]
defines: Y8B2N9ERPE
uses: [62AFX32JGT, NEXBTGYYRG, FS9FRJ17D2]
sources:
  - url: https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline
---

## Definition

Let $k \ge 1$ be an order, let $t_1 \le t_2 \le \cdots \le t_{n+k}$ be a knot vector with $t_k < t_{n+1}$, and let $B_{1,k}, \dots, B_{n,k}$ be the [[B-splines|62AFX32JGT]] of order $k$ for these knots.
Let $P_1, \dots, P_n \in \R^d$ be control points and let $w_1, \dots, w_n > 0$ be weights.
The *NURBS curve* with these data is the map $C \colon [t_k, t_{n+1}] \to \R^d$,
$$C(u) = \frac{\sum_{i=1}^{n} w_i\, B_{i,k}(u)\, P_i}{\sum_{i=1}^{n} w_i\, B_{i,k}(u)}.$$
A *NURBS surface* is defined in the same way with tensor products $B_{i,k}(u) B_{j,l}(v)$, control points $P_{ij}$ and positive weights $w_{ij}$.

## Remarks

The denominator is positive on $[t_k, t_{n+1})$, because the B-splines are nonnegative and do not all vanish there; so $C(u)$ is a convex combination of the control points.
At $u = t_{n+1}$, where the right-continuous B-splines may all vanish, $C$ is defined by its limit from the left, as usual.
In [[homogeneous coordinates|FS9FRJ17D2]], $C$ is the central projection of the polynomial B-spline curve with control points $(w_i P_i, w_i)$ in $\R^{d+1}$.
If all weights are equal, $C$ is the ordinary B-spline curve $\sum_i B_{i,k}(u) P_i$.
Example: take $k = 3$, knots $0, 0, 0, 1, 1, 1$, points $(1, 0)$, $(1, 1)$, $(0, 1)$ and weights $1$, $1/\sqrt{2}$, $1$.
Then $C$ is a rational quadratic [[Bézier curve|NEXBTGYYRG]], and $C(1/2) = (1/\sqrt{2}, 1/\sqrt{2})$.
In fact $C$ traces the quarter of the unit circle in the first quadrant.
Non-example: the same data with weight $w_2 = -1$ fail the positivity clause, and then the denominator $(1-u)^2 - 2u(1-u) + u^2 = (2u - 1)^2$ vanishes at $u = 1/2$, so $C$ is not defined on all of $[0, 1]$.
