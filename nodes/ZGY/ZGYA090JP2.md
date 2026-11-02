---
tag: ZGYA090JP2
kind: definition
name: Complementary error function
msc: ["33B20"]
defines: TZ3CT1YA9B
uses: [7Y56QCZSZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Error_function
    locator: Complementary error function
---

## Definition

Let $\operatorname{erf}$ be the [[error function|7Y56QCZSZJ]].
The *complementary error function* is the function $\operatorname{erfc} \colon \R \to \R$ given by
$$\operatorname{erfc} x = 1 - \operatorname{erf} x.$$

## Remarks

Since $\frac{2}{\sqrt{\pi}} \int_0^\infty e^{-t^2}\, dt = 1$, the definition is equivalent to
$$\operatorname{erfc} x = \frac{2}{\sqrt{\pi}} \int_x^\infty e^{-t^2}\, dt.$$

Example: $\operatorname{erfc} 0 = 1$, and $\operatorname{erfc}(-x) = 2 - \operatorname{erfc} x$ because $\operatorname{erf}$ is odd.

Non-example: $x \mapsto 1 + \operatorname{erf} x$ is not $\operatorname{erfc}$; it tends to $2$ rather than $0$ as $x \to \infty$.

For large $x > 0$, $\operatorname{erfc} x \sim \frac{e^{-x^2}}{x\sqrt{\pi}}$.
The definition extends to complex $z$ by $\operatorname{erfc} z = 1 - \operatorname{erf} z$, which is an entire function.
The scaled function $e^{x^2} \operatorname{erfc} x$ is often used in numerical work.
