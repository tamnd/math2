---
tag: ZH4V0WHSXT
kind: definition
name: Green's function
msc: [34B27, 34B05]
defines: SH6JY9RN2E
uses: [0QQRP17Z7S, TM8VQJWGHZ, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_function
---

## Definition

Let $a < b$ and let $p_0, \ldots, p_{n-1}$ be [[continuous functions|0X3WGX95FE]] on $[a, b]$, with $n \ge 1$.
Let $L y = y^{(n)} + p_{n-1} y^{(n-1)} + \cdots + p_0 y$ be the [[linear differential operator|0QQRP17Z7S]] on $[a, b]$.
Let $B_1, \ldots, B_n$ be linear forms of the shape $B_i y = \sum_{j=0}^{n-1} \left( \alpha_{ij}\, y^{(j)}(a) + \beta_{ij}\, y^{(j)}(b) \right)$ with real constants $\alpha_{ij}, \beta_{ij}$.
Assume that the [[boundary value problem|TM8VQJWGHZ]] $L y = 0$, $B_1 y = \cdots = B_n y = 0$ has only the solution $y = 0$.
A *Green's function* of this problem is a function $G \colon [a, b] \times [a, b] \to \R$ with the following property.
For every continuous $f$ on $[a, b]$, the function
$$y(x) = \int_a^b G(x, s)\, f(s)\, ds$$
is a solution of $L y = f$, $B_1 y = \cdots = B_n y = 0$.

## Remarks

Under the assumption, the Green's function exists, and the solution above is the only one.
For fixed $s$, the function $x \mapsto G(x, s)$ solves $L y = 0$ on $[a, s)$ and on $(s, b]$ and satisfies the boundary conditions.
Its derivatives of order up to $n - 2$ are continuous at $x = s$, and its derivative of order $n - 1$ jumps by $1$ there.
Formally, $L_x G(x, s) = \delta(x - s)$.

Example: for $L y = y''$ on $[0, 1]$ with $y(0) = y(1) = 0$, take $G(x, s) = x (s - 1)$ for $x \le s$ and $G(x, s) = s (x - 1)$ for $x \ge s$.
It vanishes at $x = 0$ and $x = 1$, it is linear in $x$ on each side of $s$, and $\partial_x G$ jumps from $s - 1$ to $s$, a jump of $1$.
For $f = 1$ it gives $y(x) = \frac{x (x - 1)}{2}$, and indeed $y'' = 1$ and $y(0) = y(1) = 0$.

Non-example: for $L y = y''$ on $[0, 1]$ with $y'(0) = y'(1) = 0$, the constants solve the homogeneous problem, so the assumption fails.
There is no Green's function: $y'' = 1$ has no solution with these conditions, since $y'(1) - y'(0) = \int_0^1 y'' = 1$.
