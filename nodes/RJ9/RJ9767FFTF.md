---
tag: RJ9767FFTF
kind: definition
name: Black–Scholes equation
msc: [35Q91, 91G20]
defines: ZFTNJ2YREG
uses: [1CCTH8X2FT, 09EGC6F8PT, D48DR46B97]
sources:
  - url: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_equation
---

## Definition

Let $\sigma > 0$ and $r \ge 0$ be constants and let $T > 0$.
The *Black–Scholes equation* is the [[parabolic equation|1CCTH8X2FT]] for a function $V(S, t)$ with $S > 0$ and $0 \le t < T$:
$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0.$$
Here $S$ is the price of the underlying asset, modelled by [[geometric Brownian motion|D48DR46B97]] with volatility $\sigma$.
The constant $r$ is the risk-free interest rate, and $V$ is the price of a derivative security.
It is solved with a terminal condition $V(S, T) = \Phi(S)$ given by the payoff $\Phi$.

## Remarks

Example: $V(S, t) = S$ is a solution: $V_t = 0$, $V_{SS} = 0$, and $r S \cdot 1 - r S = 0$.
It is the value of holding one share.
Another solution is $V(S, t) = K e^{-r(T - t)}$, the value of a bond paying $K$ at time $T$: $V_t - r V = 0$.
Non-example: $V(S, t) = S^2$ fails, since $\frac{1}{2}\sigma^2 S^2 \cdot 2 + r S \cdot 2S - r S^2 = (\sigma^2 + r) S^2 \ne 0$.
With $x = \log S$ and $\tau = T - t$, the equation becomes a heat equation with constant drift and decay terms, so it is backward parabolic in $t$.
