---
tag: 55V8WAJXXJ
kind: definition
name: Inverse distance weighting
msc: [65D05, 41A05, 41A63]
defines: QHN67MSH8S
uses: [BM703GV34G, 0VKD1TP7F3, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_distance_weighting
---

## Definition

Let $(X, \delta)$ be a [[metric space|0VKD1TP7F3]], usually $\R^d$ with the [[Euclidean distance|0NPPGHQNXQ]].
Let $x_1, \dots, x_N \in X$ be pairwise distinct, let $u_1, \dots, u_N \in \R$, and let $p > 0$.
For $x \in X$ and $i = 1, \dots, N$ with $x \ne x_i$, put $w_i(x) = \delta(x, x_i)^{-p}$.
The *inverse distance weighting interpolant* of the data is the function $u \colon X \to \R$ given as follows.
If $x$ is not one of the $x_i$, then
$$u(x) = \frac{\sum_{i=1}^{N} w_i(x) \, u_i}{\sum_{i=1}^{N} w_i(x)}.$$
At the data points, $u(x_i) = u_i$ for $i = 1, \dots, N$.

## Remarks

The interpolant reproduces the data by definition, and it is continuous at each $x_i$, because $w_i(x) \to \infty$ as $x \to x_i$ while the other weights stay bounded.
Each value $u(x)$ is a convex combination of the $u_i$, so $\min_i u_i \le u(x) \le \max_i u_i$.
This scheme is also called Shepard's method.
It is the case of constant fits with weight $r^{-p}$ in [[moving least squares|T0JZN6WP5X]].

Example: on $\R$ with $p = 2$, data $u_1 = 10$ at $x_1 = 0$ and $u_2 = 40$ at $x_2 = 3$, at $x = 1$ the weights are $1$ and $1/4$.
So $u(1) = \frac{10 + 40/4}{1 + 1/4} = 16$, which lies between $10$ and $40$.

Non-example: the plain average $\sum_i u_i / N$ with equal weights does not depend on the distances and does not reproduce the data; for the same data it gives $25 \ne 10$ at $x_1$.
