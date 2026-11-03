---
tag: Q53QEEDE2S
kind: definition
name: Cox–Ingersoll–Ross model
msc: [91G30, 60H10, 60J60]
defines: NH54DP03BD
uses: [7TZ87AS1MW, 22735FGJV6, Y99MCTGZHZ]
sources:
  - url: https://en.wikipedia.org/wiki/Cox%E2%80%93Ingersoll%E2%80%93Ross_model
---

## Definition

Let $W$ be a [[Brownian motion|22735FGJV6]] and let $a, b, \sigma > 0$ be constants.
The *Cox–Ingersoll–Ross model* is the [[short-rate model|7TZ87AS1MW]]
$$dr_t = a (b - r_t) \, dt + \sigma \sqrt{r_t} \, dW_t, \qquad r_0 > 0.$$
Here $b$ is the long-run mean, $a$ is the speed of mean reversion and $\sigma$ scales the volatility.

## Remarks

The equation has a unique strong solution, and $r_t \ge 0$ for all $t$.
If the Feller condition $2ab \ge \sigma^2$ holds, then $r_t > 0$ for all $t$ almost surely.
Example: $a = 0.5$, $b = 0.04$, $\sigma = 0.1$ satisfy it, since $2 \cdot 0.5 \cdot 0.04 = 0.04 \ge 0.01$.
Non-example: $a = 0.1$, $b = 0.04$, $\sigma = 0.2$ fail it, since $0.008 < 0.04$, and then the rate reaches $0$ with positive probability.
The mean is $E[r_t] = b + (r_0 - b) e^{-at}$, the same as in the Vasicek model.
Given $r_0$, the variable $r_t$ is a constant multiple of a noncentral chi-squared variable.
Bond prices have the exponential-affine form $P(t, T) = A(t, T) e^{-B(t, T) r_t}$ with explicit deterministic $A$ and $B$.
