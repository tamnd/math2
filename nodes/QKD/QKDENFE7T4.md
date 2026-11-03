---
tag: QKDENFE7T4
kind: definition
name: Hull–White model
msc: [91G30, 60H10]
defines: KA4EA7GTAF
uses: [7TZ87AS1MW, QXHQ57B0R2, 22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Hull%E2%80%93White_model
---

## Definition

Let $W$ be a [[Brownian motion|22735FGJV6]] and let $a, \sigma > 0$ be constants.
Let $\theta \colon [0, \infty) \to \R$ be a deterministic function.
The *Hull–White model* (one-factor) is the [[short-rate model|7TZ87AS1MW]]
$$dr_t = (\theta(t) - a r_t) \, dt + \sigma \, dW_t.$$
The function $\theta$ is chosen so that the model bond prices $P(0, T)$ equal the observed ones for all $T > 0$.

## Remarks

If $f^M(0, T)$ is the observed instantaneous forward curve and it is differentiable, the fit gives
$$\theta(t) = \frac{\partial f^M(0, t)}{\partial t} + a f^M(0, t) + \frac{\sigma^2}{2a}\left(1 - e^{-2at}\right).$$
Example: a constant $\theta(t) = ab$ gives $dr_t = a(b - r_t) \, dt + \sigma \, dW_t$, the [[Vasicek model|QXHQ57B0R2]].
Non-example: $dr_t = (\theta(t) - a r_t) \, dt + \sigma \sqrt{r_t} \, dW_t$ is not a Hull–White model in this sense, since its volatility depends on $r_t$.
As in the Vasicek model, $r_t$ is normal and can be negative.
Some authors also let $a$ and $\sigma$ depend on time.
