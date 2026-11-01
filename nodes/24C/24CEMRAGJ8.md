---
tag: 24CEMRAGJ8
kind: definition
name: Schur-convex function
msc: [26B25, 26D15]
defines: A72XTVF2GK
uses: [5K7VT2VKZT, 0BQMWCNS8S]
sources:
  - url: https://en.wikipedia.org/wiki/Schur-convex_function
---

## Definition

Let $n \ge 1$.
For $x \in \R^n$, let $x_{[1]} \ge x_{[2]} \ge \dots \ge x_{[n]}$ be the entries of $x$ in decreasing order.
A vector $y \in \R^n$ *majorizes* $x \in \R^n$, written $x \prec y$, if
$$\sum_{i=1}^{k} x_{[i]} \le \sum_{i=1}^{k} y_{[i]} \quad \text{for } k = 1, \dots, n - 1, \qquad \sum_{i=1}^{n} x_{[i]} = \sum_{i=1}^{n} y_{[i]};$$
see [[majorization|5K7VT2VKZT]].
A function $f \colon \R^n \to \R$ is *Schur-convex* if $f(x) \le f(y)$ for all $x, y \in \R^n$ with $x \prec y$.
It is *Schur-concave* if $-f$ is Schur-convex.

## Remarks

A Schur-convex function is symmetric: if $y$ is obtained from $x$ by a [[permutation|0BQMWCNS8S]] of the entries, then $x \prec y$ and $y \prec x$, so $f(x) = f(y)$.
Every symmetric convex function is Schur-convex.
For a symmetric $f$ with continuous partial derivatives on $\R^n$, the Schur–Ostrowski criterion says that $f$ is Schur-convex if and only if $(x_i - x_j)\big(\partial_i f(x) - \partial_j f(x)\big) \ge 0$ for all $x$ and all $i, j$.

Example: $f(x) = \max_i x_i = x_{[1]}$.
If $x \prec y$, the case $k = 1$ of the definition gives $x_{[1]} \le y_{[1]}$, so $f(x) \le f(y)$.

Non-example: $f(x_1, x_2) = x_1$ on $\R^2$.
The vectors $(1, 0)$ and $(0, 1)$ majorize each other, but $f(1, 0) = 1 > 0 = f(0, 1)$.
