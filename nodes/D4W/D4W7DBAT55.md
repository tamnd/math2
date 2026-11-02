---
tag: D4W7DBAT55
kind: definition
name: Polyharmonic spline
msc: [41A15, 41A05, 41A63]
defines: XJ0JGPBC8R
uses: [ZBSXSTQM2J, XZ33P3HBB9, K2NK9A8M5F, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Polyharmonic_spline
---

## Definition

Let $d \ge 1$ and $m \ge 1$ be integers with $2m > d$.
Define $\varphi \colon [0, \infty) \to \R$ by
$$\varphi(r) = \begin{cases} r^{2m-d} \log r & \text{if } d \text{ is even}, \\ r^{2m-d} & \text{if } d \text{ is odd}, \end{cases}$$
with $\varphi(0) = 0$.
Let $\Pi_{m-1}$ be the space of polynomials on $\R^d$ of total degree at most $m - 1$.
A *polyharmonic spline* of order $m$ with distinct centres $x_1, \dots, x_N \in \R^d$ is a function
$$s(x) = \sum_{i=1}^{N} w_i\, \varphi(\norm{x - x_i}) + p(x),$$
where $p \in \Pi_{m-1}$ and the real weights satisfy $\sum_{i=1}^{N} w_i\, q(x_i) = 0$ for every $q \in \Pi_{m-1}$.

## Remarks

Suppose the centres are unisolvent for $\Pi_{m-1}$, that is, the only $q \in \Pi_{m-1}$ vanishing at all $x_i$ is $0$.
Then for any data $y_1, \dots, y_N$ there is exactly one polyharmonic spline with $s(x_i) = y_i$.
This is [[radial basis function interpolation|XZ33P3HBB9]] with the [[radial basis function|ZBSXSTQM2J]] $\varphi$.
Up to a constant factor, $\varphi(\norm{x})$ is a [[fundamental solution|K2NK9A8M5F]] of $\Delta^m$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]], so $s$ satisfies $\Delta^m s = 0$ away from the centres.
The interpolant minimizes the seminorm $\sum_{\abs{\alpha} = m} \frac{m!}{\alpha!} \int_{\R^d} (\partial^\alpha f)^2$ among suitable functions with $f(x_i) = y_i$.
Example: $d = 1$, $m = 2$ gives $\varphi(r) = r^3$ and $s(x) = \sum w_i \abs{x - x_i}^3 + a + bx$ with $\sum w_i = \sum w_i x_i = 0$; this is a natural cubic spline.
Non-example: in the same setting, $s(x) = \abs{x}^3$ (one centre $0$, $w_1 = 1$) violates the side condition $\sum w_i = 0$, and indeed it is not linear outside the centres.
For $d = 2$, $m = 2$ one gets $\varphi(r) = r^2 \log r$, the thin plate spline.
