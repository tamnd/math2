---
tag: 7EWX5ECNRR
kind: definition
name: Ornstein–Uhlenbeck process
msc: [60J70, 60G15]
defines: HZM2ASCDY4
uses: [552AWX3QXN, 05AQE0QR0D, DT0QXJE705]
sources:
  - url: https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process
---

## Definition

Let $(W_t)_{t \ge 0}$ be a [[Wiener process|552AWX3QXN]], let $X_0$ be a real random variable independent of $W$, and let $\theta > 0$, $\sigma > 0$ and $\mu \in \R$.
The *Ornstein–Uhlenbeck process* with these parameters is the solution $(X_t)_{t \ge 0}$ of the stochastic differential equation
$$dX_t = \theta (\mu - X_t) \, dt + \sigma \, dW_t$$
with initial value $X_0$.
Explicitly,
$$X_t = \mu + (X_0 - \mu) e^{-\theta t} + \sigma \int_0^t e^{-\theta (t - s)} \, dW_s.$$

## Remarks

The explicit formula solves the equation: Itô's lemma applied to $e^{\theta t} X_t$ gives $d(e^{\theta t} X_t) = \theta \mu e^{\theta t} \, dt + \sigma e^{\theta t} \, dW_t$, which integrates to the formula.
If $X_0$ is constant, $X_t$ is [[normal|05AQE0QR0D]] with mean $\mu + (X_0 - \mu) e^{-\theta t}$ and variance $\frac{\sigma^2}{2\theta}(1 - e^{-2\theta t})$.
If $X_0$ is normal with mean $\mu$ and variance $\sigma^2 / (2\theta)$, the process is [[stationary|DT0QXJE705]], with covariance $\frac{\sigma^2}{2\theta} e^{-\theta \abs{t - s}}$.
For $\theta = 0$, which the definition excludes, the equation gives $X_0 + \sigma W_t$, a Brownian motion with no mean reversion and no stationary law.
Up to linear changes of space and time variables, it is the only non-trivial process that is stationary, Gaussian and Markov.
