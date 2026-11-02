---
tag: 7BVX2KF3QC
kind: definition
name: Fixed-point iteration
msc: [47J25, 65H05, 40A05]
defines: K6ZF91051B
uses: [0QE8STGJH2, 06JYPJ4WHH, 0P27W9RW0G, 0VK6VEH345, 0QN69YA357]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_iteration
---

## Definition

Let $X$ be a set, let $f \colon X \to X$ be a map, and let $x_0 \in X$.
The *fixed-point iteration* of $f$ starting at $x_0$ is the [[sequence|0QE8STGJH2]] $(x_n)_{n \ge 0}$ defined by
$$x_{n+1} = f(x_n) \quad \text{for } n \ge 0.$$
A *fixed point* of $f$ is a point $x^* \in X$ with $f(x^*) = x^*$.

## Remarks

If $X$ is a metric space, $f$ is [[continuous|0P27W9RW0G]], and the iteration [[converges|06JYPJ4WHH]] to $x^*$, then $x^*$ is a fixed point, since $f(x^*) = \lim f(x_n) = \lim x_{n+1} = x^*$.
Example: for $f(x) = x/2 + 1/x$ on $(0, \infty)$ and $x_0 = 1$, the iterates are $1, 1.5, 1.41\overline{6}, \ldots$, and they converge to $\sqrt{2}$, the fixed point, since $x = x/2 + 1/x$ means $x^2 = 2$.
Non-example of convergence: for $f(x) = 2x$ on $\R$ and $x_0 = 1$, the iterates $2^n$ diverge, although $0$ is a fixed point.
The [[Banach fixed point theorem|0VK6VEH345]] says the iteration converges to the unique fixed point when $f$ is a [[contraction|0QN69YA357]] of a nonempty complete metric space.
If $q < 1$ is the contraction constant, the error after $n$ steps is at most $q^n d(x_1, x_0) / (1 - q)$.
The sequence is also written $x_n = f^n(x_0)$, the $n$-th iterate of $f$ applied to $x_0$.
