---
tag: XXA9JSGW2C
kind: definition
name: Degree of exactness of a quadrature rule
msc: [65D32, 41A55]
defines: ZYT1JNT1Y0
uses: [ADSVMCY77A, MAM9H3SY3Y, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_integration
---

## Definition

Let $Q(f) = \sum_{i=1}^{n} w_i f(x_i)$ be a [[quadrature rule|ADSVMCY77A]] on $[a, b]$, and let $I(f) = \int_a^b f(x)\, dx$.
The rule has *degree of exactness* $d \ge 0$ if:

1. $Q(p) = I(p)$ for every real [[polynomial|MAM9H3SY3Y]] $p$ of [[degree|0DPF6WRZW6]] at most $d$;
2. $Q(p) \ne I(p)$ for some polynomial $p$ of degree $d + 1$.

## Remarks

By linearity, clause 1 holds if and only if $Q(x^k) = I(x^k)$ for $k = 0, 1, \dots, d$.
The degree of exactness of an $n$-node rule is at most $2n - 1$: for $p(x) = \prod_i (x - x_i)^2$, of degree $2n$, one has $Q(p) = 0 < I(p)$.
A rule has degree of exactness at least $n - 1$ if and only if it is interpolatory.
Example: the midpoint rule $Q(f) = (b - a) f(m)$ with $m = (a + b)/2$ has degree $1$: it is exact for $1$ and $x - m$, while for $(x - m)^2$ it gives $0$ instead of $(b - a)^3/12$.
Non-example: the left endpoint rule $Q(f) = (b - a) f(a)$ does not have degree $1$, since for $p(x) = x - a$ it gives $0$ instead of $(b - a)^2/2$; its degree is $0$.
Some authors call it the degree of precision or the algebraic degree of accuracy.
