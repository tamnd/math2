---
tag: 8K9YQ1YGVS
kind: definition
name: Beta function
msc: [33B15]
defines: QHNWVSC6AQ
uses: [0VCTBJMEJF, 0V3FZMVB4K]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_function
---

## Definition

The *beta function* is the function $B \colon (0, \infty) \times (0, \infty) \to \R$ given by the [[improper integral|0VCTBJMEJF]]
$$B(x, y) = \int_0^1 t^{x - 1} (1 - t)^{y - 1}\, dt.$$
The integral converges for all real $x > 0$ and $y > 0$.

## Remarks

Example: $B(\frac12, \frac12) = \int_0^1 \frac{dt}{\sqrt{t(1-t)}}$.
The substitution $t = \sin^2 \theta$ gives $dt = 2 \sin\theta \cos\theta\, d\theta$ and $\sqrt{t(1-t)} = \sin\theta\cos\theta$, so $B(\frac12, \frac12) = \int_0^{\pi/2} 2\, d\theta = \pi$.

Non-example of a valid argument: for $x = 0$ and $y = 1$ the integral is $\int_0^1 t^{-1}\, dt = \infty$, so $(0, 1)$ is outside the domain.

The beta function is symmetric, $B(x, y) = B(y, x)$, and it satisfies $B(x, y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}$, where $\Gamma$ is the [[gamma function|0V3FZMVB4K]].
For positive integers $m, n$ this gives $B(m, n) = \frac{(m-1)!\,(n-1)!}{(m + n - 1)!}$.
The same integral defines $B(x, y)$ for complex $x, y$ with positive real parts.
