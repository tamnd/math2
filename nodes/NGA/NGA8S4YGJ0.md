---
tag: NGA8S4YGJ0
kind: definition
name: Vasicek model
msc: [91G30, 60H10]
defines: QXHQ57B0R2
uses: [7TZ87AS1MW, HZM2ASCDY4, 22735FGJV6, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Vasicek_model
---

## Definition

Let $W$ be a [[Brownian motion|22735FGJV6]] and let $a, \sigma > 0$ and $b \in \R$ be constants.
The *Vasicek model* is the [[short-rate model|7TZ87AS1MW]]
$$dr_t = a (b - r_t) \, dt + \sigma \, dW_t, \qquad r_0 \in \R.$$
Here $b$ is the long-run mean, $a$ is the speed of mean reversion and $\sigma$ is the volatility.

## Remarks

The solution is $r_t = r_0 e^{-at} + b (1 - e^{-at}) + \sigma \int_0^t e^{-a(t - s)} \, dW_s$, an [[Ornstein–Uhlenbeck process|HZM2ASCDY4]] with mean $b$.
So $r_t$ has a [[normal distribution|05AQE0QR0D]] with mean $b + (r_0 - b) e^{-at}$ and variance $\frac{\sigma^2}{2a}(1 - e^{-2at})$.
Example: with $a = 0.5$, $b = 0.04$, $r_0 = 0.06$, the mean of $r_1$ is $0.04 + 0.02 e^{-0.5} \approx 0.052$.
Non-example: $dr_t = a(b - r_t) \, dt + \sigma \sqrt{r_t} \, dW_t$ is not a Vasicek model, because its volatility depends on the rate; it is the Cox–Ingersoll–Ross model.
Since $r_t$ is normal, $P(r_t < 0) > 0$ for every $t > 0$.
Bond prices are $P(t, T) = A(t, T) e^{-B(t, T) r_t}$ with $B(t, T) = (1 - e^{-a(T - t)}) / a$ and an explicit deterministic $A(t, T)$.
