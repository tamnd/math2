---
tag: RFTWT7KEW5
kind: definition
name: Central path
msc: [90C51, 90C05, 90C25]
defines: AFQTYDNDGH
uses: [1W1BXJN9ER, 59ZC4Z9611, 07GR3TNW4H, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Interior-point_method
---

## Definition

Consider a [[convex optimization|1W1BXJN9ER]] problem: minimise $f_0(x)$ over $x \in \R^n$ subject to $f_i(x) \le 0$ for $i = 1, \dots, m$, where $f_0, \dots, f_m \colon \R^n \to \R$ are differentiable [[convex functions|07GR3TNW4H]].
Assume that some $x$ satisfies $f_i(x) < 0$ for all $i$.
Let $\varphi(x) = -\sum_{i=1}^m \ln(-f_i(x))$ be the logarithmic [[barrier function|59ZC4Z9611]], defined where all $f_i(x) < 0$.
Assume that for every $t > 0$ the function $t f_0 + \varphi$ has a unique minimiser $x^*(t)$.
The *central path* is the curve $\set{x^*(t) : t > 0}$.

## Remarks

Example: minimise $x$ subject to $-x \le 0$ on $\R$.
Here $\varphi(x) = -\ln x$ on $x > 0$, and $t x - \ln x$ has derivative $t - 1/x$, which vanishes only at $x = 1/t$; so $x^*(t) = 1/t$, and $x^*(t) \to 0$, the optimum.

Non-example: for "minimise $0$ subject to $-x \le 0$", the function $t \cdot 0 - \ln x$ has no minimiser on $x > 0$, so the assumption fails and no central path is defined.

Each point of the central path gives a dual feasible point, and $f_0(x^*(t)) - p^* \le m / t$, where $p^*$ is the optimal value.

Take a [[linear program|VNMXB0J2KA]] "minimise $c^T x$ subject to $A x = b$, $x \ge 0$".
Its dual is "maximise $b^T y$ subject to $A^T y + s = c$, $s \ge 0$".
The primal-dual central path is the set of points $(x(\mu), y(\mu), s(\mu))$, $\mu > 0$, with these properties.
They satisfy $A x = b$, $A^T y + s = c$, $x > 0$, $s > 0$ and $x_i s_i = \mu$ for every $i$.
It exists and is unique for each $\mu > 0$ when both problems have strictly feasible points and $A$ has full row rank.
