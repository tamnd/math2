---
tag: VDWNESBV8R
kind: definition
name: SABR volatility model
msc: [91G20, 91G30, 60H10]
defines: NBKVXCVQJE
uses: [2KQF3JSAQ7, Y99MCTGZHZ, 22735FGJV6, D48DR46B97]
sources:
  - url: https://en.wikipedia.org/wiki/SABR_volatility_model
---

## Definition

Let $W$ and $Z$ be [[Brownian motions|22735FGJV6]] with correlation $\rho \in (-1, 1)$.
Let $\beta \in [0, 1]$ and $\alpha \ge 0$ be constants.
The *SABR model* for a forward price $F$ and its volatility $\sigma$ is the system
$$dF_t = \sigma_t F_t^{\beta} \, dW_t, \qquad d\sigma_t = \alpha \sigma_t \, dZ_t,$$
with $F_0 > 0$ and $\sigma_0 > 0$.
Here $\alpha$ is the volatility of the volatility.

## Remarks

The volatility is a driftless [[geometric Brownian motion|D48DR46B97]]: $\sigma_t = \sigma_0 \exp(\alpha Z_t - \alpha^2 t / 2)$.
Example: $\beta = 1$ and $\alpha = 0$ give $dF_t = \sigma_0 F_t \, dW_t$, the lognormal model behind Black's formula.
Example: $\beta = 0$ and $\alpha = 0$ give $dF_t = \sigma_0 \, dW_t$, a normal model in which $F$ can become negative.
Non-example: $\beta = 2$ is outside the model, since $\beta$ must lie in $[0, 1]$.
For $0 < \beta < 1$ a boundary condition at $F = 0$ must be added, usually absorption.
Some authors write $\nu$ for the volatility of volatility and $\alpha$ for the initial volatility $\sigma_0$.
