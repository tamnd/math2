---
tag: ENZF7KF1TC
kind: definition
name: Bézier curve
msc: [65D17, 68U07, 41A10]
defines: NEXBTGYYRG
uses: [0C4VWBFY73, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zier_curve
---

## Definition

Let $n \ge 1$ and let $P_0, P_1, \dots, P_n$ be points of $\R^d$, the control points.
The *Bézier curve* of degree $n$ with these control points is the map $B \colon [0, 1] \to \R^d$,
$$B(t) = \sum_{k=0}^{n} \binom{n}{k} (1 - t)^{n-k}\, t^k\, P_k.$$

## Remarks

The coefficients $\binom{n}{k}(1-t)^{n-k} t^k$ are the [[Bernstein basis polynomials|0C4VWBFY73]] of degree $n$; they are nonnegative on $[0, 1]$ and sum to $1$.
So $B(t)$ lies in the [[convex hull|0FQSDC2EQ2]] of the control points, $B(0) = P_0$, $B(1) = P_n$, $B'(0) = n(P_1 - P_0)$ and $B'(1) = n(P_n - P_{n-1})$.
Example: $n = 2$ with $P_0 = (0, 0)$, $P_1 = (1, 2)$, $P_2 = (2, 0)$ gives $B(t) = (2t, 4t - 4t^2)$, an arc of the parabola $y = 2x - x^2$.
Non-example: no arc of a circle of positive length is a Bézier curve.
Indeed, a polynomial map $t \mapsto (x(t), y(t))$ with $x^2 + y^2 = 1$ must be constant.
If $x$ and $y$ had top degree $m \ge 1$, the coefficient of $t^{2m}$ in $x^2 + y^2$ would be a positive sum of squares.
A rational Bézier curve adds positive weights, $B(t) = \sum_k w_k b_{k,n}(t) P_k / \sum_k w_k b_{k,n}(t)$, and does represent circular arcs.
