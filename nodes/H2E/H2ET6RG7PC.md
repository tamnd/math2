---
tag: H2ET6RG7PC
kind: definition
name: Geometric Brownian motion
msc: [60J65, 91G30]
defines: D48DR46B97
uses: [552AWX3QXN, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_Brownian_motion
---

## Definition

Let $(W_t)_{t \ge 0}$ be a [[Wiener process|552AWX3QXN]], and let $\mu \in \R$, $\sigma > 0$ and $s_0 > 0$.
The *geometric Brownian motion* with drift $\mu$, volatility $\sigma$ and initial value $s_0$ is the process $(S_t)_{t \ge 0}$ given by
$$S_t = s_0 \exp\Bigl(\bigl(\mu - \tfrac{\sigma^2}{2}\bigr) t + \sigma W_t\Bigr).$$

## Remarks

By [[Itô's lemma|2J1RVQB0CM]], $S$ is the unique strong solution of $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$ with $S_0 = s_0$.
Check: with $f(t, x) = s_0 \exp((\mu - \sigma^2/2) t + \sigma x)$, Itô's lemma gives $dS_t = (\mu - \sigma^2/2) S_t \, dt + \sigma S_t \, dW_t + \tfrac{1}{2} \sigma^2 S_t \, dt$, which simplifies to the equation above.
The arithmetic process $s_0 + \mu t + \sigma W_t$ is not a geometric Brownian motion: it takes negative values with positive probability, while $S_t > 0$ always.
For each $t$, $\log S_t$ is normal with mean $\log s_0 + (\mu - \sigma^2/2) t$ and variance $\sigma^2 t$, so $S_t$ is [[log-normal|4W40NHWPQT]].
Its mean is $E[S_t] = s_0 e^{\mu t}$, and for $\mu = 0$ the process is a martingale.
