---
tag: RGT7WEZG8X
kind: definition
name: Spline interpolation
msc: [41A15, 65D07, 41A05]
defines: D59HBKKRP9
uses: [84TJ8KQ926, SS1YMS2NPC]
sources:
  - url: https://en.wikipedia.org/wiki/Spline_interpolation
---

## Definition

Let $n \ge 1$, let $a = x_0 < x_1 < \cdots < x_k = b$ with $k \ge 1$, and let $y_0, \dots, y_k \in \R$.
A *spline interpolant of degree $n$* of the data $(x_i, y_i)$ is a [[spline|84TJ8KQ926]] $s$ of degree $n$ with knots $x_0, \dots, x_k$ such that $s(x_i) = y_i$ for $i = 0, \dots, k$.

## Remarks

The splines of degree $n$ with these knots form a space of dimension $n + k$, and the interpolation conditions are $k + 1$ equations.
So $n - 1$ further conditions are needed for uniqueness.
For $n = 1$ the interpolant is unique: it is the broken line through the data.
For $n = 3$ two end conditions are added.
Examples are $s''(a) = s''(b) = 0$ for the natural [[cubic spline|V42H0R3EKX]], and prescribed values of $s'(a)$ and $s'(b)$ for the clamped cubic spline.
Each of these choices gives a unique interpolant.

Example: data $(0, 0)$, $(1, 1)$, $(2, 0)$ with $n = 1$.
The broken line $s(x) = x$ on $[0, 1]$ and $s(x) = 2 - x$ on $[1, 2]$ is continuous, linear on each piece and takes the values $0, 1, 0$, so it is the spline interpolant of degree $1$.

Non-example: for the same data, $s(x) = 2x - x^2$ takes the values $0, 1, 0$.
But it is not a spline of degree $1$, because its pieces have degree $2$.
It is a [[polynomial interpolant|SS1YMS2NPC]], not a linear spline interpolant.
