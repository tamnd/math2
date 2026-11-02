---
tag: B7HPB2Z6GC
kind: definition
name: Cramér–von Mises criterion
msc: [62G10, 62G30]
defines: G14XJXPKFS
uses: [A05WR6TEK5, 087P03NEND, 0MXMS3AE13, 0AJN7WHBJZ, 58NHGZDSRE]
sources:
  - url: https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93von_Mises_criterion
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with [[empirical distribution function|A05WR6TEK5]] $F_n$.
Let $F_0$ be a fixed continuous [[cumulative distribution function|0MXMS3AE13]].
The *Cramér–von Mises statistic* is
$$T = n \int_{-\infty}^{\infty} \big(F_n(x) - F_0(x)\big)^2 \, dF_0(x).$$
The *Cramér–von Mises test* of $H_0 \colon$ "the $X_i$ have distribution function $F_0$" rejects $H_0$ when $T$ is large.
The critical value comes from the null law of $T$.

## Remarks

With the [[order statistics|58NHGZDSRE]] $X_{(1)} \le \dots \le X_{(n)}$, the integral can be computed exactly:
$$T = \frac{1}{12 n} + \sum_{i=1}^{n} \Big( \frac{2i - 1}{2n} - F_0(X_{(i)}) \Big)^2.$$
Under $H_0$ the law of $T$ does not depend on $F_0$, since $F_0(X_i)$ is uniform on $[0, 1]$.
As $n \to \infty$ it converges to the law of $\int_0^1 B(t)^2 \, dt$ for a [[Brownian bridge|3MCVMBAGD1]] $B$.

Example: $n = 1$, $X_1 = 0.5$ and $F_0(x) = x$ on $[0, 1]$.
The integral is $\int_0^{1/2} x^2 \, dx + \int_{1/2}^{1} (1 - x)^2 \, dx = 1/24 + 1/24 = 1/12$.
The formula gives the same value: $1/12 + (1/2 - 1/2)^2 = 1/12$.

Non-example: $n \int (F_n - F_0)^2 \, dx$, with Lebesgue measure in place of $dF_0$, is not the criterion.
Its null law depends on $F_0$, for example on its scale, so it gives no distribution-free test.

The Anderson–Darling statistic is a weighted variant of $T$.
