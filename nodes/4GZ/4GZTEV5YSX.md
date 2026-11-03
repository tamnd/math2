---
tag: 4GZTEV5YSX
kind: definition
name: LIBOR market model
msc: [91G30, 91G20, 60H10]
defines: 609V9CMN6Z
uses: [22735FGJV6, 0D0GBNDKDH, D48DR46B97]
sources:
  - url: https://en.wikipedia.org/wiki/LIBOR_market_model
---

## Definition

Let $0 < T_0 < T_1 < \cdots < T_n$ be dates and let $\delta_i = T_{i+1} - T_i$.
Let $P(t, T)$ be the price at time $t$ of the zero-coupon bond paying $1$ at time $T$.
For $i = 0, \dots, n - 1$ and $t \le T_i$, the *forward LIBOR rate* is
$$L_i(t) = \frac{1}{\delta_i}\left( \frac{P(t, T_i)}{P(t, T_{i+1})} - 1 \right).$$
The forward measure $Q^{i+1}$ is the measure under which prices divided by $P(t, T_{i+1})$ are [[martingales|0D0GBNDKDH]].
For each $i$ let $\sigma_i$ be a deterministic function and let $W^{i+1}$ be a [[Brownian motion|22735FGJV6]] under $Q^{i+1}$.
A *LIBOR market model* is a model in which $dL_i(t) = \sigma_i(t) L_i(t) \, dW^{i+1}_t$ for each $i$.

## Remarks

Under $Q^{i+1}$ each $L_i$ is a driftless [[geometric Brownian motion|D48DR46B97]] with time-dependent volatility, so $L_i(T_i)$ is lognormal.
Example: a caplet paying $\delta_i (L_i(T_i) - K)^+$ at $T_{i+1}$ has price $P(0, T_{i+1}) \delta_i \big( L_i(0) N(d_1) - K N(d_2) \big)$, Black's formula.
Here $N$ is the standard normal distribution function, $v^2 = \int_0^{T_i} \sigma_i(t)^2 \, dt$, $d_1 = (\ln(L_i(0)/K) + v^2/2)/v$ and $d_2 = d_1 - v$.
Non-example: the model $dL_i(t) = \sigma_i \, dW^{i+1}_t$ with constant $\sigma_i$ is not a LIBOR market model, since there $L_i(T_i)$ is normal rather than lognormal and can be negative.
Under the measure of the last bond, $L_i$ acquires a drift that depends on the other rates and on the correlations of the Brownian motions.
