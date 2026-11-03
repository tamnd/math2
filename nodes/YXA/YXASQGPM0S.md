---
tag: YXASQGPM0S
kind: definition
name: Stochastic volatility
msc: [91G20, 60H10]
defines: 2KQF3JSAQ7
uses: [Y99MCTGZHZ, 22735FGJV6, D48DR46B97]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_volatility
---

## Definition

Let $W$ and $Z$ be two [[Brownian motions|22735FGJV6]] with correlation $\rho \in [-1, 1]$, that is, $d\langle W, Z \rangle_t = \rho \, dt$.
A *stochastic volatility model* for an asset price $S$ is a system of [[stochastic differential equations|Y99MCTGZHZ]]
$$dS_t = \mu S_t \, dt + \sqrt{v_t} \, S_t \, dW_t, \qquad dv_t = \alpha(v_t, t) \, dt + \beta(v_t, t) \, dZ_t,$$
with $S_0 > 0$ and $v_0 > 0$.
Here $\mu$ is the drift and $\alpha, \beta$ are functions such that $v_t \ge 0$ for all $t$.
The process $v$ is the *variance*, and $\sqrt{v_t}$ is the volatility.

## Remarks

Example: the Heston model takes $\alpha(v, t) = \kappa(\theta - v)$ and $\beta(v, t) = \xi \sqrt{v}$ with constants $\kappa, \theta, \xi > 0$.
Non-example: if $\beta = 0$ and $\alpha = 0$, then $v_t = v_0$ is constant and $S$ is a [[geometric Brownian motion|D48DR46B97]]; the volatility is no longer random.
The market with $S$ and a bank account alone is not complete, because there are two sources of risk and one risky asset.
So the risk-neutral measure is not unique, and a pricing model must also fix a market price of volatility risk.
Some authors model the volatility $\sigma_t$ instead of the variance $v_t = \sigma_t^2$.
