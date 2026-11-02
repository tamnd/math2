---
tag: TZ3CT1YA9B
kind: concept
name: Complementary error function
msc: ["33B20"]
sources:
  - url: https://en.wikipedia.org/wiki/Error_function
    locator: Complementary error function
---

## Summary

The complementary error function is $\operatorname{erfc} x = 1 - \operatorname{erf} x$, where $\operatorname{erf}$ is the [[error function|7Y56QCZSZJ]].
It equals $\frac{2}{\sqrt{\pi}} \int_x^\infty e^{-t^2}\, dt$, the scaled area of the tail of the Gaussian curve.
It is the natural function for small tail probabilities of the [[normal distribution|05AQE0QR0D]], where computing $1 - \operatorname{erf} x$ directly would lose precision.

## Explanations

### L1 human

The error function measures the area under the bell curve from $0$ up to $x$.
The complementary error function measures what is left: the area beyond $x$.
It starts at $1$ for $x = 0$ and drops very fast to $0$ as $x$ grows.
For example, $\operatorname{erfc} 3 \approx 2.2 \times 10^{-5}$, a tiny tail.
