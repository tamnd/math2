---
tag: GFJ20FBYF8
kind: definition
name: Appell series
msc: [33C65]
defines: QG9VDK1HN9
uses: [YZHM3HSM0F, 428M453CR2, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Appell_series
---

## Definition

Let $a, a', b, b', c, c'$ be complex numbers, with every lower parameter $c, c'$ outside $\set{0, -1, -2, \dots}$.
Write $(x)_n$ for the [[Pochhammer symbol|YZHM3HSM0F]].
The four *Appell series* are the double power series in two complex variables $x, y$:

1. $F_1(a; b, b'; c; x, y) = \sum_{m, n \ge 0} \frac{(a)_{m + n} (b)_m (b')_n}{(c)_{m + n}\, m!\, n!} x^m y^n$, convergent for $\abs{x} < 1$ and $\abs{y} < 1$;
2. $F_2(a; b, b'; c, c'; x, y) = \sum_{m, n \ge 0} \frac{(a)_{m + n} (b)_m (b')_n}{(c)_m (c')_n\, m!\, n!} x^m y^n$, convergent for $\abs{x} + \abs{y} < 1$;
3. $F_3(a, a'; b, b'; c; x, y) = \sum_{m, n \ge 0} \frac{(a)_m (a')_n (b)_m (b')_n}{(c)_{m + n}\, m!\, n!} x^m y^n$, convergent for $\abs{x} < 1$ and $\abs{y} < 1$;
4. $F_4(a; b; c, c'; x, y) = \sum_{m, n \ge 0} \frac{(a)_{m + n} (b)_{m + n}}{(c)_m (c')_n\, m!\, n!} x^m y^n$, convergent for $\sqrt{\abs{x}} + \sqrt{\abs{y}} < 1$.

## Remarks

Setting $y = 0$ leaves the terms with $n = 0$, and each series becomes a Gauss [[hypergeometric series|428M453CR2]] in $x$; for instance $F_1(a; b, b'; c; x, 0) = {}_2F_1(a, b; c; x)$.
Example: with $b = c$ and $b' = c'$, the series $F_2$ becomes $\sum_{m, n} \frac{(a)_{m + n}}{m!\, n!} x^m y^n = \sum_{N \ge 0} \frac{(a)_N}{N!} (x + y)^N = (1 - x - y)^{-a}$, by the binomial theorem; this converges when $\abs{x} + \abs{y} < 1$.
Non-example: for $a = 1$ the same series at $x = y = \frac12$ is $\sum_N 1$, which diverges; the point lies on the boundary $\abs{x} + \abs{y} = 1$ of the region of convergence.
For $\operatorname{Re} c > \operatorname{Re} a > 0$, with $\Gamma$ the [[gamma function|0H5SYBSED9]], $F_1$ has Picard's integral representation
$$F_1(a; b, b'; c; x, y) = \frac{\Gamma(c)}{\Gamma(a)\Gamma(c - a)} \int_0^1 t^{a - 1} (1 - t)^{c - a - 1} (1 - xt)^{-b} (1 - yt)^{-b'}\, dt.$$
