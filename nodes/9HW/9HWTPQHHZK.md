---
tag: 9HWTPQHHZK
kind: definition
name: Moving least squares
msc: [65D10, 41A63, 65D05]
defines: T0JZN6WP5X
uses: [H5CGZHBR58, 07GNX8GCYP, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Moving_least_squares
---

## Definition

Let $d \ge 1$ and $m \ge 0$, and let $\Pi_m$ be the space of [[polynomials in $d$ variables|07GNX8GCYP]] of total degree at most $m$.
Let $x_1, \dots, x_N \in \R^d$ be pairwise distinct, let $f_1, \dots, f_N \in \R$, and let $\theta \colon [0, \infty) \to [0, \infty)$ be a weight function.
For $x \in \R^d$, let $p_x \in \Pi_m$ minimise the [[weighted least squares|H5CGZHBR58]] error
$$\sum_{i=1}^{N} \theta(\norm{x - x_i}) \, \bigl(p(x_i) - f_i\bigr)^2$$
over $p \in \Pi_m$, where $\norm{\cdot}$ is the Euclidean norm.
The *moving least squares approximation* of the data is the function $\hat f(x) = p_x(x)$, defined at every $x$ where this minimiser is unique.

## Remarks

The minimiser is unique when the points $x_i$ with $\theta(\norm{x - x_i}) > 0$ include a [[unisolvent set|5276MDSDQV]] for $\Pi_m$.
In general $\hat f$ only approximates the data; singular weights, such as in the example below, make it interpolate.
If the data come from a polynomial in $\Pi_m$, then $\hat f$ reproduces that polynomial.

Example: $m = 0$ and $\theta(r) = r^{-p}$ for $r > 0$, with $p > 0$, at a point $x$ that is not a data point.
Then $p_x$ is the constant $\sum_i \theta_i f_i / \sum_i \theta_i$, where $\theta_i = \theta(\norm{x - x_i})$.
Extended by the data values at the data points, this is [[inverse distance weighting|QHN67MSH8S]].

Non-example: with constant weights $\theta = 1$ the fit is an ordinary least squares fit.
It gives the same polynomial $p_x = p$ at every $x$, so the result is one global polynomial.
The dependence of the weights on $x$, the "moving" feature, is lost.
