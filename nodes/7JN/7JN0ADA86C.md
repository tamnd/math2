---
tag: 7JN0ADA86C
kind: definition
name: Smoothing spline
msc: [65D10, 41A15, 62G08]
defines: BNEXZF75QC
uses: [V42H0R3EKX, 0BYTQ4X1HC, 0Y9D2FJRQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothing_spline
---

## Definition

Let $n \ge 2$, let $a \le x_1 < x_2 < \cdots < x_n \le b$ be real nodes, let $y_1, \dots, y_n$ be real numbers, and let $\lambda > 0$.
Let $W$ be the space of functions $f \colon [a, b] \to \R$ such that $f'$ is absolutely continuous and $f''$ is square integrable.
The *smoothing spline* for these data is the function $f \in W$ that minimizes
$$J_\lambda(f) = \sum_{i=1}^{n} \big(y_i - f(x_i)\big)^2 + \lambda \int_a^b f''(x)^2 \, dx.$$

## Remarks

The minimizer exists and is unique, and it is a natural [[cubic spline|V42H0R3EKX]] with knots $x_1, \dots, x_n$: a cubic on each $[x_i, x_{i+1}]$, of class $C^2$, and linear on $[a, x_1]$ and $[x_n, b]$.
Uniqueness uses $n \ge 2$: then a function with $f'' = 0$ that vanishes at all nodes is zero.
Example: if the data lie on a line, $y_i = \alpha + \beta x_i$, then $f(x) = \alpha + \beta x$ gives $J_\lambda(f) = 0$, so it is the smoothing spline for every $\lambda$.
Non-example: take $n \ge 3$ data not on a line, and let $g$ be the natural cubic spline through them.
Its [[second derivative|0Y9D2FJRQ4]] penalty is positive, and moving $g$ slightly toward a line lowers $J_\lambda$, so $g$ is not the minimizer.
As $\lambda \to 0$ the smoothing spline tends to the natural interpolating cubic spline, and as $\lambda \to \infty$ it tends to the [[least squares|0BYTQ4X1HC]] regression line.
In practice $\lambda$ is often chosen by generalized cross-validation.
