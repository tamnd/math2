---
tag: KZDMD3SDJA
kind: definition
name: Anderson–Darling test
msc: [62G10, 62G30]
defines: N9ZB0KMV0B
uses: [A05WR6TEK5, 087P03NEND, 0MXMS3AE13, 0AJN7WHBJZ, 58NHGZDSRE]
sources:
  - url: https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with [[empirical distribution function|A05WR6TEK5]] $F_n$.
Let $F_0$ be a fixed continuous [[cumulative distribution function|0MXMS3AE13]].
The *Anderson–Darling statistic* is
$$A^2 = n \int_{-\infty}^{\infty} \frac{\big(F_n(x) - F_0(x)\big)^2}{F_0(x)\big(1 - F_0(x)\big)} \, dF_0(x).$$
The *Anderson–Darling test* of $H_0 \colon$ "the $X_i$ have distribution function $F_0$" rejects $H_0$ when $A^2$ is large.
The critical value comes from the null law of $A^2$.

## Remarks

With the [[order statistics|58NHGZDSRE]] $X_{(1)} \le \dots \le X_{(n)}$ and $U_i = F_0(X_{(i)})$,
$$A^2 = -n - \frac{1}{n} \sum_{i=1}^{n} (2i - 1) \big( \ln U_i + \ln(1 - U_{n+1-i}) \big).$$
Under $H_0$ the law of $A^2$ does not depend on $F_0$.
When parameters of $F_0$ are estimated from the data, for example in a test of normality, other tables of critical values are used.

Example: $n = 1$, $X_1 = 1/2$ and $F_0(x) = x$ on $[0, 1]$.
The integral is $\int_0^{1/2} \frac{x}{1 - x} \, dx + \int_{1/2}^{1} \frac{1 - x}{x} \, dx = 2\big(\ln 2 - \tfrac12\big) = 2\ln 2 - 1$.
The formula gives $-1 - 2\ln(1/2) = 2 \ln 2 - 1 \approx 0.386$, the same value.

Non-example: the [[Cramér–von Mises statistic|G14XJXPKFS]] $n \int (F_n - F_0)^2 \, dF_0$ lacks the weight $1/(F_0(1 - F_0))$, so it is a different statistic that gives less weight to the tails.
