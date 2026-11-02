---
tag: P3A4EAA3RA
kind: definition
name: Least squares approximation
msc: [41A10, 65D10, 41A50]
defines: 2QV28WYQTQ
uses: [0QVNCJXRY3, 0B8KZRT28M, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Least-squares_function_approximation
---

## Definition

Let $H$ be a real or complex [[inner product space|0QVNCJXRY3]] with inner product $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Let $V \subseteq H$ be a finite-dimensional subspace and let $f \in H$.
A *least squares approximation* of $f$ from $V$ is an element $v^* \in V$ such that
$$\norm{f - v^*} = \min_{v \in V} \norm{f - v}.$$
In the main case, $w$ is a positive weight on $[a, b]$ and $H$ is the space $L^2_w$ of functions with $\int_a^b w \abs{f}^2 < \infty$.
Its inner product is $\ip{f}{g} = \int_a^b w(x) f(x) \overline{g(x)} \, dx$, and $V$ is the space of polynomials of degree at most $n$.

## Remarks

The least squares approximation exists, is unique, and is the [[orthogonal projection|0B8KZRT28M]] of $f$ onto $V$.
It is characterised by $\ip{f - v^*}{v} = 0$ for all $v \in V$.
If $\varphi_0, \dots, \varphi_n$ is an orthogonal basis of $V$, then $v^* = \sum_{k=0}^{n} \frac{\ip{f}{\varphi_k}}{\ip{\varphi_k}{\varphi_k}} \varphi_k$.
For a general basis, the coefficients solve the normal equations, whose matrix is the Gram matrix $(\ip{\varphi_j}{\varphi_k})$.

Example: $f(x) = x^2$ on $[-1, 1]$ with $w = 1$ and $V$ the polynomials of degree at most $1$.
With the orthogonal basis $1, x$, one gets $\ip{f}{1} / \ip{1}{1} = (2/3)/2 = 1/3$ and $\ip{f}{x} = 0$, so $v^* = 1/3$.
Check: $\int_{-1}^{1} (x^2 - 1/3) \, dx = 0$ and $\int_{-1}^{1} (x^2 - 1/3) x \, dx = 0$.

Non-example: the uniform best line for $x^2$ on $[-1, 1]$ is $1/2$, not $1/3$.
It minimises the largest error, not the integral of the squared error, so it fails the defining condition.

A discrete version replaces the integral by a weighted sum $\sum_i w_i \abs{f(x_i) - v(x_i)}^2$ over data points; this is curve fitting.
