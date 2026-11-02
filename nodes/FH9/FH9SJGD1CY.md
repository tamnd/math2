---
tag: FH9SJGD1CY
kind: definition
name: Abel transform
msc: [44A15, 44A12]
defines: QMW1MWQH6J
uses: [DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_transform
---

## Definition

Let $f \colon [0, \infty) \to \C$ be measurable, and let $y \ge 0$ be such that $\int_y^\infty \frac{\abs{f(r)}\, r}{\sqrt{r^2 - y^2}}\, dr < \infty$.
The *Abel transform* of $f$ at $y$ is the [[Lebesgue integral|DWJF7ABPR1]]
$$F(y) = 2 \int_y^\infty \frac{f(r)\, r}{\sqrt{r^2 - y^2}}\, dr.$$

## Remarks

The integrand has an integrable singularity at $r = y$, of order $(r - y)^{-1/2}$, when $f$ is bounded near $y$ and $y > 0$.
If $f$ is continuously differentiable and decays fast enough at infinity, the transform can be inverted by
$$f(r) = -\frac{1}{\pi} \int_r^\infty \frac{F'(y)}{\sqrt{y^2 - r^2}}\, dy.$$

Example: $f(r) = e^{-r^2}$.
The substitution $s = r^2 - y^2$, $ds = 2r\, dr$, gives $F(y) = \int_0^\infty \frac{e^{-y^2 - s}}{\sqrt s}\, ds = e^{-y^2}\, \Gamma(1/2) = \sqrt{\pi}\, e^{-y^2}$.

Non-example: $f(r) = 1$ for all $r$.
Then $\frac{r}{\sqrt{r^2 - y^2}} \ge 1$ for $r > y$, so the integral diverges for every $y$ and $f$ has no Abel transform.
