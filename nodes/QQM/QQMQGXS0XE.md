---
tag: QQMQGXS0XE
kind: definition
name: Saddle point of a Lagrangian
msc: [90C46, 49J35, 49K99]
defines: 5ENHTF01Z8
sources:
  - url: https://en.wikipedia.org/wiki/Saddle_point
---

## Definition

Let $C \subseteq \R^n$ be a set, and let $f, g_1, \dots, g_m \colon C \to \R$ be functions.
Consider the problem of minimizing $f(x)$ over $x \in C$ subject to $g_i(x) \le 0$ for $i = 1, \dots, m$.
Its *Lagrangian* is the function $L \colon C \times [0, \infty)^m \to \R$ given by
$$L(x, \lambda) = f(x) + \sum_{i=1}^m \lambda_i g_i(x).$$
A pair $(x^*, \lambda^*) \in C \times [0, \infty)^m$ is a *saddle point of the Lagrangian* if
$$L(x^*, \lambda) \le L(x^*, \lambda^*) \le L(x, \lambda^*) \quad \text{for all } x \in C \text{ and } \lambda \in [0, \infty)^m.$$

## Remarks

The function $L$ is minimal in the first variable and maximal in the second at $(x^*, \lambda^*)$, as for a saddle point of any function on a product.
The numbers $\lambda^*_i$ play the role of [[Lagrange multipliers|0VKKP8X6Q6]].
If $(x^*, \lambda^*)$ is a saddle point, the left inequality forces $g_i(x^*) \le 0$ for all $i$ and $\lambda^*_i g_i(x^*) = 0$ for all $i$.
The right inequality then gives $f(x^*) = L(x^*, \lambda^*) \le L(x, \lambda^*) \le f(x)$ for every feasible $x$, so $x^*$ is optimal.
This needs no convexity; the converse needs convexity of $f$, $g_i$ and $C$ and a constraint qualification such as Slater's condition.

Example: minimize $x^2$ over $C = \R$ subject to $g(x) = 1 - x \le 0$, with $L(x, \lambda) = x^2 + \lambda (1 - x)$.
The pair $(1, 2)$ is a saddle point.
For every $\lambda \ge 0$, $L(1, \lambda) = 1 = L(1, 2)$.
For every $x$, $L(x, 2) = (x - 1)^2 + 1 \ge 1$.

Non-example: the pair $(1, 1)$ for the same problem.
The right inequality fails, since $L(\tfrac12, 1) = \tfrac34 < 1 = L(1, 1)$.
