---
tag: SZ6XCSQA5H
kind: definition
name: Gaussian quadrature
msc: [65D32, 41A55, 33C45]
defines: FP37BTP93K
uses: [ADSVMCY77A, ZYT1JNT1Y0, 8TXASARQN1]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_quadrature
---

## Definition

Let $(a, b)$ be an interval, bounded or not, and let $w$ be a weight function on $(a, b)$.
This means that $w$ is integrable, $w > 0$ almost everywhere, and every moment $\int_a^b x^k w(x)\,dx$ is finite.
Let $n \ge 1$.
Consider a [[quadrature rule|ADSVMCY77A]]
$$\int_a^b f(x)\, w(x)\,dx \approx \sum_{i=1}^{n} w_i f(x_i)$$
with distinct nodes $x_1, \dots, x_n$ in $(a, b)$ and real weights $w_1, \dots, w_n$.
It is an $n$-point *Gaussian quadrature* rule for $w$ if it is an equality for every polynomial $f$ of degree at most $2n - 1$.

## Remarks

For each $w$ and $n$ such a rule exists and is unique.
Its nodes are the zeros of the degree $n$ [[orthogonal polynomial|8TXASARQN1]] $p_n$ for the inner product $\langle f, g \rangle = \int_a^b f g\, w\,dx$, and its weights are positive.
No $n$-point rule is exact for all polynomials of degree $2n$: the polynomial $\prod_{i}(x - x_i)^2$ has a positive integral but vanishes at every node.
So $2n - 1$ is the largest possible [[degree of exactness|ZYT1JNT1Y0]].

Example: $w = 1$ on $(-1, 1)$ and $n = 1$.
The rule $\int_{-1}^{1} f \approx 2 f(0)$ is exact for $f = 1$ (both sides are $2$) and for $f = x$ (both sides are $0$), so it is the one-point Gaussian rule, the midpoint rule.

Non-example: the trapezoidal rule $\int_{-1}^{1} f \approx f(-1) + f(1)$ has two nodes but fails for $f = x^2$, since the left side is $2/3$ and the right side is $2$.
So it is not exact up to degree $3$ and is not a Gaussian rule.

The rule for $w = 1$ on $(-1, 1)$ is [[Gauss–Legendre quadrature|RGGXDRCJVE]].
