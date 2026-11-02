---
tag: 6ZP4DJ7JMF
kind: example
name: Divergent asymptotic series
msc: [41A60, 40A05, "30E15"]
instance_of: [2HVC5G0H5K]
uses: [0JWMJSTBSG, 1YR53GZEPT]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Example

For $x > 0$ let
$$F(x) = \int_0^\infty \frac{e^{-t}}{1 + x t}\,dt.$$
Then, as $x \to 0^+$,
$$F(x) \sim \sum_{n \ge 0} (-1)^n n!\, x^n = 1 - x + 2x^2 - 6x^3 + \cdots,$$
and this series is a [[divergent series|0JWMJSTBSG]] for every $x \ne 0$.

Check of the expansion: for $N \ge 0$ and $t \ge 0$,
$$\frac{1}{1 + x t} = \sum_{n=0}^{N} (-x t)^n + \frac{(-x t)^{N+1}}{1 + x t}.$$
Integrating against $e^{-t}$ and using $\int_0^\infty t^n e^{-t}\,dt = n!$ gives
$$F(x) - \sum_{n=0}^{N} (-1)^n n!\, x^n = R_N(x), \qquad \abs{R_N(x)} \le x^{N+1} \int_0^\infty t^{N+1} e^{-t}\,dt = (N + 1)!\, x^{N+1}.$$
So the error is $O(x^{N+1})$ for each $N$, which is the condition of a [[Poincaré asymptotic series|2HVC5G0H5K]] at $0$.

Check of divergence: for $x \ne 0$ the ratio of consecutive terms is $(n + 1) \abs{x} \to \infty$, so the terms do not tend to $0$.

## Remarks

For a fixed small $x$ the terms $n!\, x^n$ first decrease and then grow, and the smallest one is near $n \approx 1/x$.
Stopping there, which is [[optimal truncation|1YR53GZEPT]], gives an error of order $\sqrt{2\pi/x}\, e^{-1/x}$ by Stirling's formula, which is extremely small for small $x$.
The function $F$ is the Borel sum of the series, and $F(x) = \frac1x e^{1/x} E_1(1/x)$, where $E_1$ is the [[exponential integral|EV6ZDQ0NDY]].

## Explanations

### L1 human

The series $1 - x + 2x^2 - 6x^3 + 24x^4 - \cdots$ has coefficients that grow like factorials, so it diverges for every nonzero $x$.
Yet for $x = 0.1$ its first ten or so terms give $F(0.1)$ to about three decimal places.
Each partial sum is a good approximation; only the infinite sum is meaningless.
This is typical of the series that come out of asymptotic analysis, and it is why one studies asymptotic series and not only convergent ones.
