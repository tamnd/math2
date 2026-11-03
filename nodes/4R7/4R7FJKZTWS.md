---
tag: 4R7FJKZTWS
kind: definition
name: Heston model
msc: [91G20, 60H10]
defines: 6PA46G33BB
uses: [2KQF3JSAQ7, Y99MCTGZHZ, 22735FGJV6, NH54DP03BD]
sources:
  - url: https://en.wikipedia.org/wiki/Heston_model
---

## Definition

Let $W^S$ and $W^v$ be [[Brownian motions|22735FGJV6]] with correlation $\rho \in [-1, 1]$.
Let $\mu \in \R$ and $\kappa, \theta, \xi > 0$ be constants.
The *Heston model* is the [[stochastic volatility|2KQF3JSAQ7]] model
$$dS_t = \mu S_t \, dt + \sqrt{v_t} \, S_t \, dW^S_t, \qquad dv_t = \kappa (\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW^v_t,$$
with $S_0 > 0$ and $v_0 > 0$.
Here $\theta$ is the long-run variance, $\kappa$ is the speed of mean reversion and $\xi$ is the volatility of the variance.

## Remarks

The variance equation is the same as the [[Cox–Ingersoll–Ross|NH54DP03BD]] equation, so $v_t \ge 0$ for all $t$.
If the Feller condition $2 \kappa \theta \ge \xi^2$ holds, then $v_t > 0$ for all $t$ almost surely.
Example: $\kappa = 2$, $\theta = 0.04$, $\xi = 0.3$ satisfy the Feller condition, since $2 \cdot 2 \cdot 0.04 = 0.16 \ge 0.09$.
Non-example: with $\kappa = 0.5$, $\theta = 0.04$, $\xi = 1$ the Feller condition fails, since $0.04 < 1$, and the variance can touch $0$.
The variance has mean $E[v_t] = \theta + (v_0 - \theta) e^{-\kappa t}$.
