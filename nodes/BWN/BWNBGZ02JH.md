---
tag: BWNBGZ02JH
kind: definition
name: Heath–Jarrow–Morton framework
msc: [91G30, 60H10]
defines: 1KF6521YRA
uses: [22735FGJV6, Y99MCTGZHZ, 858BHBY2BD, 7TZ87AS1MW, KA4EA7GTAF]
sources:
  - url: https://en.wikipedia.org/wiki/Heath%E2%80%93Jarrow%E2%80%93Morton_framework
---

## Definition

Let $W$ be a $d$-dimensional [[Brownian motion|22735FGJV6]] under a probability measure $Q$.
For each maturity $T > 0$ let the forward rate $f(t, T)$, for $0 \le t \le T$, satisfy
$$df(t, T) = \alpha(t, T) \, dt + \sigma(t, T) \cdot dW_t,$$
with an observed initial curve $f(0, T)$ and adapted processes $\alpha(t, T) \in \R$ and $\sigma(t, T) \in \R^d$.
Bond prices are $P(t, T) = \exp(-\int_t^T f(t, u) \, du)$, and the short rate is $r_t = f(t, t)$.
This is an *HJM model* if $Q$ is a [[risk-neutral measure|858BHBY2BD]] for the bonds, that is, every discounted bond price $e^{-\int_0^t r_s \, ds} P(t, T)$ is a $Q$-martingale.

## Remarks

Under integrability conditions, $Q$ is risk-neutral exactly when the HJM drift condition holds:
$$\alpha(t, T) = \sigma(t, T) \cdot \int_t^T \sigma(t, u) \, du.$$
Example: $d = 1$ and $\sigma(t, T) = \sigma$ constant give $\alpha(t, T) = \sigma^2 (T - t)$; this is the continuous-time Ho–Lee model.
Non-example: $\sigma$ constant with $\alpha = 0$ violates the drift condition, so the discounted bond prices are not martingales and the bonds admit arbitrage.
With $\sigma(t, T) = \sigma e^{-a(T - t)}$ the framework gives the [[Hull–White model|KA4EA7GTAF]].
In general the short rate of an HJM model is not a Markov process.
