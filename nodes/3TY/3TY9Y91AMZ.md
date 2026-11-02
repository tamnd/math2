---
tag: 3TY9Y91AMZ
kind: definition
name: K-function
msc: ["33B15"]
defines: TXCA43CMYR
uses: [0H5SYBSED9, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/K-function
---

## Definition

Let $\Gamma$ be the [[gamma function|0H5SYBSED9]] and $\ln$ the [[natural logarithm|04DXAFN2ES]].
For a real number $x > 0$, the *K-function* is
$$K(x) = (2\pi)^{-(x-1)/2} \exp\left(\binom{x}{2} + \int_0^{x-1} \ln \Gamma(t + 1)\, dt\right),$$
where $\binom{x}{2} = \frac{x(x-1)}{2}$.

## Remarks

Raabe's formula $\int_a^{a+1} \ln \Gamma(u)\, du = \frac12 \ln 2\pi + a \ln a - a$ for $a > 0$ gives
$$K(x + 1) = x^x K(x) \qquad (x > 0).$$

Example: $\int_0^1 \ln \Gamma(t+1)\, dt = \int_0^1 (\ln t + \ln \Gamma(t))\, dt = -1 + \frac12 \ln 2\pi$.
Hence $K(2) = (2\pi)^{-1/2} \exp(1 - 1 + \frac12 \ln 2\pi) = 1$.
The recurrence then gives $K(3) = 2^2 = 4$, $K(4) = 4 \cdot 3^3 = 108$, and in general $K(n + 1) = \prod_{k=1}^n k^k$.

Non-example: the function $x \mapsto x^x$ does not satisfy the recurrence; for instance $3^3 = 27 \ne 2^2 \cdot 2^2 = 16$.

The formula above is stated for $x > 0$, where $t + 1 > 0$ on the path of integration.
The same formula, with the principal branch of $\ln \Gamma$, defines $K$ as a holomorphic function on $\C \setminus (-\infty, 0]$.
