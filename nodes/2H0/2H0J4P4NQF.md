---
tag: 2H0J4P4NQF
kind: definition
name: Local regression
msc: [62G08, 62J02]
defines: TQFFFSH0BQ
uses: [H5CGZHBR58, 0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/Local_regression
---

## Definition

Let $(x_1, y_1), \dots, (x_n, y_n)$ be data with $x_i, y_i \in \R$.
Let $p \ge 0$ be an integer, the degree, and let $h > 0$ be a number, the bandwidth.
Let $K \colon \R \to [0, \infty)$ be a weight function, for example the tricube function $K(u) = (1 - \abs{u}^3)^3$ for $\abs{u} < 1$ and $K(u) = 0$ otherwise.
For a point $x \in \R$, let $\hat\beta(x) = (\hat\beta_0(x), \dots, \hat\beta_p(x))$ be a minimiser of
$$\sum_{i=1}^{n} K\Big(\frac{x_i - x}{h}\Big) \Big( y_i - \sum_{j=0}^{p} \beta_j (x_i - x)^j \Big)^2$$
over $\beta \in \R^{p+1}$.
The *local polynomial regression estimate* of degree $p$ at $x$ is $\hat m(x) = \hat\beta_0(x)$.

## Remarks

The minimisation is a [[weighted least squares|H5CGZHBR58]] problem with weights $w_i = K((x_i - x)/h)$.
It has a unique solution when at least $p + 1$ distinct points $x_i$ have $w_i > 0$.
In LOESS the bandwidth depends on $x$: $h(x)$ is the distance from $x$ to its $\lceil \alpha n \rceil$-th nearest point $x_i$, for a fixed fraction $\alpha \in (0, 1]$ called the span.
LOWESS adds rounds of reweighting that lower the weights of points with large residuals.

Example: take $p = 1$ and data that lie on a line, $y_i = a + b x_i$.
Then $\beta = (a + bx, b)$ makes every residual $y_i - \beta_0 - \beta_1 (x_i - x)$ zero, so it is a minimiser and $\hat m(x) = a + bx$; local linear regression reproduces lines exactly.

Non-example: ordinary least squares with a global polynomial uses the same weight for every point at every $x$.
Its weights do not depend on the distance $\abs{x_i - x}$, so it is not a local fit.

For $p = 0$ the estimate is the weighted average $\sum_i w_i y_i / \sum_i w_i$, the Nadaraya–Watson estimate of [[kernel regression|710VV73909]].
